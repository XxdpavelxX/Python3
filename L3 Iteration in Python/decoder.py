"""Create a Python3_Homework03 project and assign it to your Python3_Homework working set. In the 
Python3_Homework03/src folder, create a file named decoder.py, which contains an iterator named alphabator. 
When passed a list, simply return objects as-is unless they are integers between 1 and 26, in which case it 
should convert that number to the corresponding letter. The integer-to-letter correspondence is 1=A, 2=B, 3=C, 4=D, 
and so on.

You may use any technique you've learned in lesson 3 to execute this project.

Your alphabator iterator must pass the unittest below:


test_decoder.py


from string import ascii_uppercase
import unittest

from decoder import alphabator

class TestAlpha(unittest.TestCase):

    def test_easy_26(self):
        a = alphabator(range(1,27))
        self.assertEqual(list(ascii_uppercase), list(a))

    def test_upper_range(self):
        a = alphabator(range(40,50))          
        self.assertEqual(list(range(40, 50)), list(a))

    def test_various_objects(self):
        l = ['python', object, ascii_uppercase, 10, alphabator]
        a = list(alphabator(l))
        self.assertNotEqual(l[3], a[3])
        self.assertEqual("J", a[3])
        self.assertTrue(isinstance(a[1], object))

if __name__ == "__main__":
    unittest.main()


Submit decoder.py and test_decoder.py when they are working to your satisfaction.
"""
####################################################################################################################################################################


def alphabator(lst):
    for num in lst:
        if num in range(1,27):
            yield chr(num+64)
        else:
            yield num
    
