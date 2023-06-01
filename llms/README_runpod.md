# Example of a start script for a runPod.net host

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
