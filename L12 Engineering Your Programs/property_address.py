"""
Here are your instructions:

Create a Python3_Homework12 project and assign it to your Python3_Homework working set. In the Python3_Homework12/src folder, copy property_address.py and test_property_address.py from the last project. Modify property_address.py to accept the following options if called directly, with the five address values used to instantiate an Address class if no parser errors are thrown.


option

default

address?

task

-l/--level INFO yes Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL 
-n/--name Throws a parser error if empty yes Sets the name value of the Address object 
-a/--address Throws a parser error if empty yes Sets the street_address value of the Address object 
-c/--city Throws a parser error if empty yes Sets the city value of the Address object 
-s/--state Throws a parser error if empty yes Sets the state value of the Address object 
-z/--zip_code Throws a parser error if empty yes Sets the zip_code value of the Address object 

If you run your code with the following command-line arguments:

property_address.py -n Tom -a "my street" -c "San Diego" -s "CA" -z 21045

...you should see something like this in property_address.log:

2010-10-11 14:48:59,794 - INFO - __init__ - Creating a new address 
Note: When you use the ${string_prompt} or direct input option in the Eclipse run configuration, you can't use single 
quotes ('). If your input requires quotes, use double quotes ("), so the full string is parsed rather than breaking at
white space.
	    
If you run your code without command-line arguments, you should see:


Usage: property_address.py [options]property_address.py: error: options -n, -a, -c, -s, -z are required 
If you run your code with the following command-line arguments:
property_address.py -l WARNING -n Tom -a "my street" -c "San Diego" -s "CA" -z "EZ 123"
...you should see:


usage: property_address.py [options]property_address.py: error: option -z requires a valid 5-digit US zip code ...AND 
you should see something like this in property_address.log:

content appended to property_address.log

2010-10-11 17:10:32,702 - ERROR - ZipCodeError - ZIPCODE exception 
Note: Your date and time values will vary.

Now, modify your propertyaddress.py program to use the configparser library to load the settings from the following 
property_address.cfg config file: 


propertyaddress.cfg

[log]format = %(asctime)s - %(name)s - %(levelname)s - %(message)soutput = homework12.log[validators]zip_code =
\d{5}\-\d{4}$state = [A-Z]{3}$
As you can see, the log formatting, log output, and Address validators are different from what you currently have.

Your project must meet the following conditions:

Change the tests in test_property_address.py so they run correctly. Also, the results of your logfile should appear
as below:


content appended to homework12.log

2010-10-11 17:34:38,968 - root - ERROR - STATE exception2010-10-11 17:34:39,098 - root - ERROR - ZIPCODE 
exception2010-10-11 17:34:39,112 - root - INFO - Creating a new address2010-10-11 17:34:39,113 - root - ERROR - NAME
exception2010-10-11 17:34:39,113 - root - INFO - Creating a new address2010-10-11 17:34:39,113 - root - INFO - 
Creating a new address 
Note: Your date and time values will vary.

Submit property_address.py, and test_property_address.py, and property_address.cfg when your programs are working to 
your satisfaction.
"""

##################################################################################################################################################################################3

import re
import os
import logging
import configparser
from optparse import OptionParser


config_filename = os.path.join(os.path.dirname(__file__), 'property_address.cfg')
config = configparser.RawConfigParser() 
config.read(config_filename)

LOG_FILENAME  = config.get('log', 'output')
LOG_FORMAT    = config.get('log', 'format')
STATE_REGEX   = config.get('validators', 'state')
ZIPCODE_REGEX = config.get('validators', 'zip_code')

DEFAULT_LOG_LEVEL = "WARNING"
LEVELS = {'DEBUG'    : logging.DEBUG,
          'INFO'     : logging.INFO,
          'WARNING'  : logging.WARNING,
          'ERROR'    : logging.ERROR,
          'CRITICAL' : logging.CRITICAL}

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)
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
    

    @street_address.setter
    def street_address(self, value):
        self._street_address = value

    @city.setter
    def city(self, value):
        self._city = value

    @state.setter
    def state(self, value):
        result = re.match(STATE_REGEX, value)
        if not result:
            logging.error('STATE exception')
            raise StateError('Invalid state')
        else:
            self._state = value

    @zip_code.setter
    def zip_code(self, value):
        result = re.match(ZIPCODE_REGEX, value)
        if not result:
            logging.error('ZIPCODE exception')
            raise ZipCodeError('Invalid zip code')
        else:
            self._zip_code = value
            
class StateError(Exception):
    pass

class ZipCodeError(Exception):
    pass

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-l", "--level"   , dest="level"   , action="store", help="set the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL", default="INFO")
    parser.add_option("-n", "--name"    , dest="name"    , action="store", help="set the name value of the Address")
    parser.add_option("-a", "--address" , dest="address" , action="store", help="set the street_address value of the Address")
    parser.add_option("-c", "--city"    , dest="city"    , action="store", help="set the city value of the Address")
    parser.add_option("-s", "--state"   , dest="state"   , action="store", help="set the state value of the Address")
    parser.add_option("-z", "--zip_code", dest="zip_code", action="store", help="set the zip_code value of the Address")
    (options, args) = parser.parse_args()
    
    if not options.name and not options.address and not options.city and not options.state and not options.zip_code:
        parser.error("options -n, -a, -c, -s, -z are required")
    else:
        errors = []
        if not options.name:
            errors.append("option -n requires a name for the address")
        if not options.address:
            errors.append("option -a requires a street address for the address")
        if not options.city:
            errors.append("option -c requires a city for the address")       
        if not options.state:
            errors.append("option -s requires a state for the address")
        if not options.zip_code:
            errors.append("option -z requires a zip code for the address")
        if errors:
            parser.error(errors)

    start_logging(level=options.level)
    try:
        home = Address(name           = options.name,
                       street_address = options.address,
                       city           = options.city,
                       state          = options.state,
                       zip_code       = options.zip_code)
    except StateError:
        parser.error("option -s requires a valid state")
    except ZipCodeError:
        parser.error("option -z requires a valid zip code")
