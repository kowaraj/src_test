import torch
import torch.nn as nn

import transformers 
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer
from transformers.models.llama.modeling_llama import LlamaModel,LlamaConfig
from transformers.modeling_outputs import BaseModelOutputWithPast

from safetensors.torch import load_file as safe_load

from .quant import make_quant


def init_modules():
    def noop(*args, **kwargs):
        pass

    torch.nn.init.kaiming_uniform_ = noop
    torch.nn.init.uniform_ = noop
    torch.nn.init.normal_ = noop

    transformers.modeling_utils._init_weights = False


def find_layers(module, layers=[nn.Conv2d, nn.Linear], name=''):
    if type(module) in layers:
        return {name: module}
    res = {}
    for name1, child in module.named_children():
        res.update(find_layers(
            child, layers=layers, name=name + '.' + name1 if name != '' else name1
        ))
    return res


class GPTQModel(object):

    def __init__(self, model_path, model_file, **args):
        self.model_path = model_path
        self.model_file = model_file

        self.wbits = args.get("wbits", 4)
        self.exclude_layers = args.get("exclude_layers", ['lm_head'])
        self.groupsize = args.get("groupsize", -1)
        self.seqlen = args.get("seqlen", 2048)


    def load(self, device='cuda:0'):
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        
        # Load model
        config = AutoConfig.from_pretrained(self.model_path)

        init_modules()
        torch.set_default_dtype(torch.half)
        model = AutoModelForCausalLM.from_config(config)
        torch.set_default_dtype(torch.float)
        model = model.eval()

        # Make it quantized

        layers = find_layers(model)
        for lname in self.exclude_layers:
            del layers[lname]

        make_quant(
            model, 
            names=layers, 
            bits=self.wbits, 
            groupsize=self.groupsize,
            faster=False,
            kernel_switch_threshold=128 
        )

        # Load checkpoint state
        model.load_state_dict(safe_load(self.model_file), strict=False)
        model.seqlen = self.seqlen

        # Send to device
        model = model.to(torch.device(device))
        self.model = model