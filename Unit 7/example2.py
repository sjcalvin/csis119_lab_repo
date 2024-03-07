import json
import pandas as pd

with open('example.json', 'r') as file:

    # json_raw = json.loads(file)
    json_df = pd.read_json(file)

# print(json_raw)
print(json_df)