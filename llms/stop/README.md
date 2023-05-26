# pod config

- environment 
```
export HUGGINGFACE_HUB_CACHE=/workspace/.cache/huggingface/hub
export HUGGINGFACE_ASSETS_CACHE=/workspace/.cache/huggingface/assets
```

NOTE: restart IPython kernel after a package installation



# Jupyter + venv

Run the `/workspace/script.sh` after a Pod restart: 

```
#!/bin/bash 

# do once:
# python -m venv myenv

# activate
source /workspace/venv/myenv2/bin/activate

# do once: install kernel (the package)
# pip install --user ipykernel

# run kernel (the module)
python -m ipykernel install --user --name=myenvKernel
```

# Links

- bitsandbytes: https://huggingface.co/blog/hf-bitsandbytes-integration
