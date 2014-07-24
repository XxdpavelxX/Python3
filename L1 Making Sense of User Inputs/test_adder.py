import unittest
from adder import addition


class Test(unittest.TestCase):


    def testName(self):
        self.assertEqual(addition(1,2),1+2)
        self.assertEqual(addition(5,3),3+5)        
        self.assertRaises(TypeError,addition, 2.1, 2.1)
        self.assertRaises(TypeError,addition, 'abc', 'def')
        self.assertRaises(TypeError,addition, 'abc',1)
        self.assertRaises(TypeError,addition, 2.1,'def')


if __name__ == "__main__":
    unittest.main()
