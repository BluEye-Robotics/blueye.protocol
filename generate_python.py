#!/usr/bin/env python3
import json
import os
import pickle
import hashlib
from collections import OrderedDict

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

data = json.loads(open("protocol.json").read(), object_pairs_hook=OrderedDict)

data_file = """# -*- coding: utf-8 -*-
# This file is autogenerated. Please do not edit
from collections import OrderedDict
_json_hash = "%s"
_generator_hash = "%s"
protocol_data = %s

""" % (md5("protocol.json"), md5("generate_python.py"), str(data)) 

with open(os.path.join("python", "p2_app_protocol", "protocol_data.py"), "w") as f:
    f.write(data_file)