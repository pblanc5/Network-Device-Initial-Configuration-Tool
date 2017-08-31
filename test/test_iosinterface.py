# Author: Patrick Blanchard
# Contact: pblanc5@lsu.edu --or-- patrickblanchard.dev@gmail.com
# Description: Unit test for iosinterface.py
#

from ndictool import iosinterface
import unittest
from testserver

class TestIOSInterface(unittest.TestCase):

    def test_update(self):
        port = 41
        expect = ['configure termial', 'interface vlan 1']
        dev = iosinterface.IOSInterface("127.0.0.1", port, "test.net")
        dev.update()
