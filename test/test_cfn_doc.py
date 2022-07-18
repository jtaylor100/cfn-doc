import unittest
import cfn_doc.cfn_doc


class MainTest(unittest.TestCase):
    def test_returns_hello_world(self):
        self.assertEqual("Hello world", cfn_doc.cfn_doc.get_output())
