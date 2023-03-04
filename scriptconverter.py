import json
import yaml

with open('inputjson.json') as f:
    data = json.load(f)

yaml_data = yaml.dump(data, default_flow_style=False)

with open('outputyaml.yaml', 'w') as f:
    f.write(yaml_data)