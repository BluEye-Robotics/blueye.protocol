#!/usr/bin/env python3
import hashlib
import json
import pickle


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


data = json.loads(open(protocol_json_path).read())
data_pickle = pickle.dumps(data)

data_file = f"""import pickle
_data_pickle = {data_pickle}
json_hash = {md5("protocol.json")}
generator_hash = {md5("generator_python.py")}
protocol_data = pickle.loads(_data_pickle)"""
