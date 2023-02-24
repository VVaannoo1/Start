import yaml

def perform_operation(data):
    result = 0
    if data["operation"] == "+":
        result = data["a"] + data["b"]
    elif data["operation"] == "-":
        result = data["a"] - data["b"]
    elif data["operation"] == "*":
        result = data["a"] * data["b"]
    elif data["operation"] == "/":
        result = data["a"] / data["b"]
    return result

data_list = [
    {"a": 10, "b": 20, "operation": "+"},
    {"a": 10, "b": 20, "operation": "/"},
    {"a": 10, "b": 20, "operation": "*"},
    {"a": 1488, "b": 228, "operation": "-"}
]

with open("result.yaml", "w") as file:
    for data in data_list:
        result = perform_operation(data)
        output = {
            "data": data,
            "result": result
        }
        yaml.dump(output, file)