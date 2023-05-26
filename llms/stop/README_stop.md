# code 

NOTE: make sure the env is setup to point to /workspace/.cache instead of /root/.cache
```
(myenv2) root@f82c0e00ba7e:~# du -sh /workspace/.cache/huggingface/*
512	/workspace/.cache/huggingface/assets
2.9G	/workspace/.cache/huggingface/hub
```


```
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer, GenerationConfig
device = 'cuda'

tokenizer = LlamaTokenizer.from_pretrained("ehartford/WizardLM-7B-Uncensored")
model = LlamaForCausalLM.from_pretrained(
    "ehartford/WizardLM-7B-Uncensored",
    load_in_8bit=False,
    torch_dtype=torch.float16,
    device_map="auto",
)
```

