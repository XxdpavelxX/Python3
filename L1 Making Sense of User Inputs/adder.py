"""Here are your instructions:


Create a Python3_Homework01 project and assign it to your Python3_Homework working set. In the Python3_Homework01/src folder,
create a program named adder.py; in it, create a function that takes two objects and adds them together only if they are
both of the integer type. Raise a TypeError otherwise.  Then, create a test_adder.py file that tests the correctness of 
this function.

When they are working to your satisfaction, submit adder.py and test_adder.py."""

######################################################################################################################################################################################################################################################################################################################################################################################################################

def addition(a,b):
    if isinstance(a,int) and isinstance(b,int): 
        return a+b
        
    else :
        raise TypeError("Please use two numbers")
