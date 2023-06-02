#!/bin/bash 

# do once:
# python -m venv myenv

# activate
source /workspace/venv/myenv/bin/activate

# do once: install kernel (the package)
# pip install --user ipykernel

# run kernel (the module)
python -m ipykernel install --user --name=myenvKernel

# install the modules

# import torch 
# import transformers 

# update apt, install ffmpeg
# apt-get update
# apt install ffmpeg


echo "source /workspace/venv/myenv/bin/activate"
echo "NOTE: do not forget to setup the environment variable for the HF cache to /workspace/.cache/" 

