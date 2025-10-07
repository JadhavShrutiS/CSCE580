import json

# Credit: Created with help of ChatGPT


def get_all_json_keys(json_object, parent_key='', keys=None):
    if keys is None:
        keys = []

    if isinstance(json_object, dict):
        for key, value in json_object.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            keys.append(full_key)
            get_all_json_keys(value, full_key, keys)

    elif isinstance(json_object, list):
        if json_object:
            # Just handle the first element to get the structure
            get_all_json_keys(json_object[0], parent_key, keys)

    return keys

file = './data/R1PF1.json'
