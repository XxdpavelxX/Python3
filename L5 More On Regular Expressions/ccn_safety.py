"""Here are your instructions:


 
Create a Python3_Homework05 project and assign it to your Python3_Homework working set. In the Python3_Homework05/src 
folder, create a program named ccn_safety.py with a function that substitutes X for all but the last four digits of any
credit card numbers in a string, returning the updated string as its result. Use the following text as a sample:


Text to use in ccn_safety.py

Have you ever noticed, in television and movies, that phone numbers and credit cardsare obviously fake numbers like
555-123-4567 or 5555-5555-5555-5555? It is because a numberthat appears to be real, such as 1234-5678-1234-5678, 
triggers the attention of privacy and security experts.
Your project should meet the following conditions:
•For our purposes, it only needs to convert numbers of the form XXXX-XXXX-XXXX-XXXX.
•The program should return this text: "Have you ever noticed, in television and movies, that phone numbers and credit 
cards are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number that appears to be real, 
such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and security experts." Note that the phone numbers should 
not be replaced! 
•You should include a test_ccn_safety.py program in a separate file that confirms that your code functions as expected.

Submit ccn_safety.py and test_ccn_safety.py when they are working to your satisfaction.
"""

import re

text = """Have you ever noticed, in television and movies, that phone 
numbers and credit cards are obviously fake numbers like 555-123-4567 
or 5555-5555-5555-5555? It is because a number that appears to be real,
such as 1234-5678-1234-5678, triggers the attention of privacy and 
security experts."""

def converter(text):
    match=re.sub("[1-9]{4}-[1-9]{4}-[1-9]{4}", "XXXX-XXXX-XXXX", text)
    return match

if __name__ == "__main__":
    print (converter(text))
