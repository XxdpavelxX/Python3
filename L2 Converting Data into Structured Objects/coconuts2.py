""""Here are your instructions:

Create a Python3_Homework02 project and assign it to your Python3_Homework working set. In the Python3_Homework02/src 
folder, create a file named coconuts.py, with an inventory class that tracks different types of coconuts from around the
world. The different types of coconuts must have these weight attribute values:


Type

Weight

South Asian 3 
Middle Eastern 2.5 
American 3.5 

The inventory class must have the following methods:
•add_coconut() accepts a coconut as an argument. Other types throw an AttributeError. 
•total_weight() provides the total weight of coconuts.

For this project, you may find the isinstance built-in useful.

You must Include a test_coconuts.py program to confirm all the Inventory class methods. The tests must check:
1.That different coconut types each have a different weight. 
2.That if a string object is passed to the Inventory.add_coconut method, an AttributeError is thrown. 
3.That if 2 South Asian, 1 Middle Eastern, and 3 American coconuts are added to the inventory, the Inventory.total_weight()
method returns 19.

When they are working, submit coconuts.py and test_coconuts.py."""

#########################################################################################################################################################################################################################################################################################################################################################

class Coconuts(object):
    coconuts_dct = {"South_Asian" : 3,
                    "Middle_Eastern" : 2.5,
                    "American" : 3.5
                    }

    def __init__(self, coconut_type):
        if coconut_type in Coconuts.coconuts_dct.keys():
            self.type   = coconut_type
            self.weight = Coconuts.coconuts_dct[coconut_type]
        else:
            raise AttributeError("'%s' is not one of the specified coconuts!" % coconut_type)                      
 
class Inventory(object):
    
    def __init__(self):
        self.inventory = []
    
    def add_coconut(self, coconut):

        if not isinstance(coconut, Coconuts):
            raise AttributeError("Please input one of the specified coconuts, not a '%s'" % coconut.__class__.__name__)
        self.inventory.append(coconut)
    
    def total_weight(self):
        total_weight = 0
        for coconut in self.inventory:
            total_weight += coconut.weight
        return total_weight
