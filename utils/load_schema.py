import json
import os


def load_schema(path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, path)
    with open(file_path) as f:
        schema = json.load(f)
        return schema