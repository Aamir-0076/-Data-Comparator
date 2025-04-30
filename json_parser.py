import json
from jsonpath_ng import parse

def load_json(file_path):
    with open(file_path) as file:
        return json.load(file)

def extract_data(json_data, json_path_expr):
    expr = parse(json_path_expr)
    matches = expr.find(json_data)
    return [match.value for match in matches]
