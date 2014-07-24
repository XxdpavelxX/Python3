import unittest
from coconuts2 import *

class TestCoconut(unittest.TestCase):
    
    def test_coconut_type(self):
        south_asian_coconut    = Coconuts("South_Asian")
        middle_eastern_coconut = Coconuts("Middle_Eastern")
        american_coconut       = Coconuts("American")
        self.assertNotEqual(south_asian_coconut.weight, middle_eastern_coconut.weight, "South Asian and Middle Eastern coconuts have the same weight")
        self.assertNotEqual(south_asian_coconut.weight, american_coconut.weight, "South Asian and American coconuts have the same weight")
        self.assertNotEqual(middle_eastern_coconut.weight, american_coconut.weight, "Middle Eastern and Middle Eastern coconuts have the same weight")
    
    def test_inventory_attribute(self):
        inv = Inventory()
        self.assertRaises(AttributeError, inv.add_coconut, "South_Asian")
    
    def test_inventory_total_weight(self):
        south_asian_coconut    = Coconuts("South_Asian")
        middle_eastern_coconut = Coconuts("Middle_Eastern")
        american_coconut       = Coconuts("American")
        inventory = Inventory()
        inventory.add_coconut(south_asian_coconut)
        inventory.add_coconut(south_asian_coconut)
        inventory.add_coconut(middle_eastern_coconut)
        inventory.add_coconut(american_coconut)
        inventory.add_coconut(american_coconut)
        inventory.add_coconut(american_coconut)
        
        self.assertEqual(inventory.total_weight(), 19, "Coconuts weigh %f together but 19 is what their weight should be." % inventory.total_weight())
        
if __name__ == "__main__":
    unittest.main()
