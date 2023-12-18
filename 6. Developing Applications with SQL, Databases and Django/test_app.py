import unittest
from app import returnString

class MyTest(unittest.TestCase):
    def test_returnString(self):
        result = returnString()
        self.assertNotEqual(result, "How are you", "They are equal")