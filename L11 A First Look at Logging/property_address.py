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
import logging
import os

LOG_FILENAME = "output.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "warning"
LEVELS = {'debug'    : logging.DEBUG,
          'info'     : logging.INFO,
          'warning'  : logging.WARNING,
          'error'    : logging.ERROR,
          'critical' : logging.CRITICAL}
        
def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
class Address:
    
    def __init__(self, name, street_address, city, state, zip_code):
        logging.info('Creating a new address')
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

    @street_address.setter
    def street_address(self, value):
        self._street_address = value

    @city.setter
    def city(self, value):
        self._city = value

    @state.setter
    def state(self, value):
        "State only allows 2 capital letters or it throws a StateError"
        result = re.match(r"^[A-Z]{2}$", value)
        if not result:
            logging.error('STATE exception')
            raise StateError("Not a state")
        else:
            self._state = value

    @zip_code.setter
    def zip_code(self, value):
        "Zip code must follow the simple US pattern (nnnnn) or it throws a ZipCodeError"
        result = re.match(r"^\d{5}$", value)
        if not result:
            logging.error('ZIPCODE exception')
            raise ZipCodeError("Invalid zip code")
        else:
            self._zip_code = value


class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass
