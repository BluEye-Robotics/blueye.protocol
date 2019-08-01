#!/usr/bin/env python3
import unittest
import os
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()



class TestAppProtocol(unittest.TestCase):
    def test_protocol_data_import(self):
        from p2_app_protocol import protocol_data

    def test_protocol_data_hash(self):
        from p2_app_protocol import _json_hash, _generator_hash
        self.assertEqual(_json_hash, md5(os.path.join("../..", "protocol.json")))
        self.assertEqual(_generator_hash, md5(os.path.join("../..", "generate_python.py")))


if __name__ == '__main__':
    unittest.main()
