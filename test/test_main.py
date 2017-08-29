# Author: Patrick Blanchard
# Contact: pblanc5@lsu.edu --or-- patrickblanchard.dev@gmail.com
# Description: Unit test for main.py
#

from ndictool import main
import unittest
import os

class TestMain(unittest.TestCase):

    def test_read_yaml(self):
        res = main.read_yaml(os.path.join(os.path.dirname(__file__), "test.yml"))
        print res
        expected = {"console_server":"10.0.0.1", "domain_name":"test.net", "ios_interface": [41,42], "comware_interface":None}
        self.assertDictEqual(expected, res)

if __name__ == "__main__":
    unittest.main()
