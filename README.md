# SPA(Side Plugin Adaption)

This is the official repository of the paper: SPA: Towards A Computational Friendly Cloud-Base and On-Devices Collaboration Seq2seq Personalized Generation.

![Framework of SPA.](SPA.png)

## How to Use

- Prepare well for your dataset, adjust it to the form:

```bash
{"instruction":... ,"input": ... , "output": ...}
```

- clone the repo

```bash
git clone git@github.com:OceannTwT/ra-isf.git
```

- replace the code on LlamaForCausalLM with model/modeling_SPA.py

- add your dataset on SPA/data/dataset_info.json

- tune and get the SPA model!


```bash
bash train.sh
```

- inference the model by running llama_SPA_predict.py, remember change the dir on your additional parameters.

## What could it do?

- This repository is served for on-devices personalized LLMs, it could contribute to fast and reliable on-devices LLMs. 

## Acknowledgement

- We thank for the contributions of all co-authors and siri-china teams in this work. 