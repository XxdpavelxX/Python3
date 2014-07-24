"""Here are your instructions:


Create a Python3_Homework10 project and assign it to your Python3_Homework working set. In the Python3_Homework10/src 
folder, create a program named property_address.py, including the following:
•The custom exceptions StateError and ZipCodeError. 
•Class Address that takes name, street_address, city, state, and zip_code as string arguments, which must then be set as
attributes. You turn any or all of these attributes into properties in order to solve this assignment so long as they 
also meet these requirements: ◦After being set in __init__, the name attribute is read-only. Further attempts to modify
it will trigger an AttributeError. 
◦Zip code must follow the simple US pattern (nnnnn) or it throws a ZipCodeError 
◦State only allows 2 capital letters or it throws a StateError

•State and Zip code validation must be done by regular expressions. 
•Your project must include (and your program must pass!) the unittest test_property_address.py (listed below).



import unittest
from property_address import *
   
class TestAddresses(unittest.TestCase): 
   
    def setUp(self): 
        self.home = Address( name='Steve Holden', street_address='1972 Flying Circus', city='Arlington', state='VA', zip_code='12345' )
       
    def test_name(self): 
        self.assertEqual(self.home.name, 'Steve Holden') 
        self.assertRaises(AttributeError, setattr, self.home, 'name', 'Daniel Greenfeld')  
           
    def test_state(self): 
        self.assertEqual(self.home.state, 'VA') 
        self.assertRaises(StateError, setattr, self.home, 'state', 'Not a state')  
        self.home.state = 'CO' 
        self.assertEqual(self.home.state, 'CO')  
        
    def test_zip_code(self): 
        self.assertEqual(self.home.zip_code, '12345') 
        self.assertRaises(ZipCodeError, setattr, self.home, 'zip_code', '123456')   
        self.home.zip_code = '54321' 
        self.assertEqual(self.home.zip_code, '54321') 
       
if __name__ == "__main__": 
    unittest.main() 
Submit property_address.py and test_property_address.py when they are working to your satisfaction.
"""

#######################################################################################################################################################################################################

import re
class Address(object):
    
    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name 
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code
     
    @property
    def name(self):
        return self._name
    @property   
    def street_address(self):
        return self._street_address
    @property
    def city(self):
        return self._city
    @property
    def state(self):
        return self._state
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value):
        result = re.match(r"^[1-9]{5}$", value)
        if not result:
            raise ZipCodeError ("Invalid zip code")
        else:
            self._zip_code = value
    
    @state.setter        
    def state(self, value):
        result = re.match(r"^[A-Z]{2}$", value)
        if not result:
            raise StateError("Not a valid state abbreviation")
        else:
            self._state = value
            
class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass
