# code 

NOTE: make sure the env is setup to point to /workspace/.cache instead of /root/.cache
```
(myenv2) root@f82c0e00ba7e:~# du -sh /workspace/.cache/huggingface/*
512	/workspace/.cache/huggingface/assets
2.9G	/workspace/.cache/huggingface/hub
```


```py
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




```py
prompt = """USER: How much is 4+7?
ASSISTANT:"""


tokenized = tokenizer(prompt, return_tensors="pt")
print(tokenizer.decode(tokenized['input_ids'][0]))

prompt = """USER: How much is 4+7?
ASSISTANT:"""

inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"].to(device)


generation_config = GenerationConfig( temperature=0, num_beams=1, )
with torch.no_grad():
    generation_output = model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
        max_new_tokens=100,
    )
    s = generation_output.sequences[0]
    output = tokenizer.decode(s)

print(output)


```


