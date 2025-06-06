#!/usr/bin/env python3
import hashlib
import os


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class TestAppProtocol:
    def test_protocol_data_import(self):
        from blueye.legacyprotocol import protocol_data # noqa: F401

    def test_protocol_data_hash(self, request):
        from blueye.legacyprotocol import _generator_hash, _json_hash

        root_dir_path = request.fspath.dirname + "/../../"
        assert _json_hash == md5(
            os.path.join(root_dir_path, "ProtocolDefinitions", "udp_protocol.json")
        )
        assert _generator_hash == md5(
            os.path.join(root_dir_path, "generators", "generate_udp_protocol.py")
        )
