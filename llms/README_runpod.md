# runpod Settings -> Environment Variables

```
export HUGGINGFACE_HUB_CACHE=/workspace/.cache/huggingface/hub
export HUGGINGFACE_ASSETS_CACHE=/workspace/.cache/huggingface/assets
```


# Example of a start script for a runPod.net host

NOTE: restart IPython kernel after a package installation

```sh
#!/bin/bash 

# do once:
# python -m venv myenv_tests

# activate
source /workspace/venv/myenv_tests/bin/activate

# do once: install kernel (the package)
# pip install --user ipykernel

# run kernel (the module)
python -m ipykernel install --user --name=myenvKernelTests

# install the modules

# import torch 
# import transformers 

# update apt, install ffmpeg
apt-get update
apt install ffmpeg
```
