# pod config

- environment 
```
export HUGGINGFACE_HUB_CACHE=/workspace/.cache/huggingface/hub
export HUGGINGFACE_ASSETS_CACHE=/workspace/.cache/huggingface/assets
```

NOTE: restart IPython kernel after a package installation



# Jupyter + venv

- create `python -m venv myenv`
- activate `source myenv/bin/activate`

- install `pip install --user ipykernel`
- add `python -m ipykernel install --user --name=myenv`



# Links

- bitsandbytes: https://huggingface.co/blog/hf-bitsandbytes-integration
