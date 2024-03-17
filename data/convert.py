import pandas as pd
import numpy as np
import json
 
# 读取Parquet文件
df = pd.read_parquet('./hotpotqa/0001.parquet')
 
# 将DataFrame保存为JSON文件
df.to_json('output.json', orient='records')

with open("/root/workspace/output.json", 'r', encoding='UTF-8') as f:
    j = json.load(f)
    for line in j:
        with open('hotpot.json', "a", encoding='UTF-8') as ff:
            ff.write(json.dumps(line)+ '\n')
