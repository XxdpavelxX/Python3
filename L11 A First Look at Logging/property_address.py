"""
Here are your instructions:


Create a Python3_Homework11 project and assign it to your Python3_Homework working set. In the Python3_Homework11/src
folder, copy property_address.py and test_property_address.py from the last project.

Your project should meet the following conditions:

property_address.py must append messages such as the following to a logfile named property_address.log each time
test_property_address.py is run:


property_address.log:

2011-12-05 19:36:14,970 - ERROR - state - STATE exception 
 2011-12-05 19:36:14,970 - INFO - __init__ - Creating a new address 
 2011-12-05 19:36:14,986 - ERROR - zip_code - ZIPCODE exception 
 """
 
 #######################################################################################################################################################################
 
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
