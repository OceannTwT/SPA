import torch
import time
import os
import json
from transformers import LlamaTokenizer, LlamaForCausalLM, AutoConfig
from peft import PeftModel
model_path = '/mnt/task_runtime/llama-7b'
add_state_model_dir = "/mnt/task_runtime/output_gbl_normal2"
# for i in range(100):
#     pre = time.time()
#     print(time.time() - pre)
adapter_len = 32
config = config = AutoConfig.from_pretrained(model_path, trust_remote_code=True, adapter_len = adapter_len)
model = LlamaForCausalLM.from_pretrained(
    model_path, config = config, torch_dtype=torch.float16, device_map='auto',
)
tokenizer = LlamaTokenizer.from_pretrained(model_path)
add_state_dict = torch.load(os.path.join(add_state_model_dir, "pytorch_model.bin"))
model.load_state_dict(add_state_dict, strict=False)

tot = 0
acc = 0

with open("/mnt/task_runtime/llama_tune/data/gbl_50k_l.json", "r", encoding="utf-8-sig") as f:
    for line in f.readlines():
        tot = tot + 1
        enc = json.loads(line)
        prompt = enc["instruction"]
        res = enc["output"]
        inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
        generate_ids = model.generate(**inputs, max_length=128)
        generate_ids = generate_ids[0][len(inputs["input_ids"][0]):-1]
        infer_res = tokenizer.decode(generate_ids)
        if infer_res == res:
            acc = acc + 1
        print(infer_res, res, acc / tot, tot)
        # print("prompt: ",prompt, "\nresult: ", infer_res)
