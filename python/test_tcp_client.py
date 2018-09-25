#!/usr/bin/env python3
import unittest
from p2_app_protocol import TcpClient



class TestTcpClient(unittest.TestCase):
    def setUp(self):
        pass

    def test_ping_not_connected(self):
        tc = TcpClient()
        self.assertFalse(tc.ping())



if __name__ == '__main__':
    unittest.main()
