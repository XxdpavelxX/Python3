from find_regex import searcher
import unittest


class Test(unittest.TestCase):
    
    def test_regex(self):

        self.assertEqual(searcher(), "Starts at:231, Ends at:250")

if __name__ =="__main__":
    unittest.main()
