import json
import yaml

with open('inputjson.json') as f:
    data = json.load(f)

results = []

for item in data:
    a = item['a']
    b = item['b']
    op = item['operation']
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        raise ValueError(f"Unknown operation '{op}'")
    
    results.append({
        'a': a,
        'b': b,
        'operation': op,
        'result': result
    })

with open('data.yaml', 'w') as f:
    yaml.dump(results, f)