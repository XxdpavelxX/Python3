"""Here are your instructions:


Create a Python3_Homework04 project and assign it to your Python3_Homework working set. In the Python3_Homework04/src
folder, create a program named find_regex.py that takes the following text and finds the start and end positions of the 
phrase, "Regular Expressions".


Text to use in find_regex.py
In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theoryin a set of models 
using a notation called "regular sets" as a method to do pattern matching. Activeusage of this system, called Regular 
Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky,
Ken Thompson, and Henry Spencer.

Your project should meet the following conditions:
•Your code must return 231 as the start and 250 as the end. 
•You must include a separate test_find_regex.py program that confirms that your code functions as instructed.

Submit find_regex.py and test_find_regex.py when they are working to your satisfaction."""

##############################################################################################################################################################

import re

a = """In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory 
in a set of models using a notation called "regular sets" as a method to do pattern matching. Activeusage of this system,
called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, 
Ivan P. Polonsky, Ken Thompson, and Henry Spencer."""
def searcher():
    match = re.search("Regular Expressions", a)
    beginning = match.start()
    ending = match.end()
    return (("Starts at:%d, Ends at:%d")%(beginning, ending))
print (searcher())

