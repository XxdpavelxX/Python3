import unittest
from ccn_safety2 import converter
from ccn_safety2 import text

class Test(unittest.TestCase):
        
    def test_safety(self):
        self.assertEqual(converter("abcd 1111-2222-3333-4444 efg 1234-9876-6767-3424 123-4566-333"), "abcd CCN REMOVED FOR YOUR SAFETY efg CCN REMOVED FOR YOUR SAFETY 123-4566-333")
        self.assertEqual(converter(text),"""Have you ever noticed, in television and movies, that phone 
numbers and credit cards are obviously fake numbers like 555-123-4567 
or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real,
such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and 
security experts.""")
        
if __name__ =="__main__":
    unittest.main()
