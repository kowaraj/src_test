# TheBloke/alpaca-lora-65B-GPTQ-4bit

## Install tgui
```
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui/
pip install -r requirements.txt
```

## Install GPTQ support
```
mkdir repositories
cd repositories/
git clone https://github.com/qwopqwop200/GPTQ-for-LLaMa.git -b cuda
cd GPTQ-for-LLaMa/
python setup_cuda.py install
cd ../..
```

## Fetch model
```
sudo apt-get update && apt-get update && apt-get install git-lfs

cd models
git lfs install
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/TheBloke/alpaca-lora-65B-GPTQ-4bit
cd alpaca-lora-65B-GPTQ-4bit/
rm alpaca-lora-65B-GPTQ-4bit-128g.no-act-order.safetensors
wget https://huggingface.co/TheBloke/alpaca-lora-65B-GPTQ-4bit/resolve/main/alpaca-lora-65B-GPTQ-4bit-128g.no-act-order.safetensors
cd ../..
```

## Start server
```
python server.py --listen --listen-port 3000  --wbits 4 --groupsize 128 --model alpaca-lora-65B-GPTQ-4bit
```

# TheBloke/guanaco-65B-GPTQ

```
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/TheBloke/guanaco-65B-GPTQ
wget https://huggingface.co/TheBloke/guanaco-65B-GPTQ/resolve/main/Guanaco-65B-GPTQ-4bit.act-order.safetensors
python server.py --listen --listen-port 3000  --wbits 4 --groupsize 128 --model alpaca-lora-65B-GPTQ-4bit
```
