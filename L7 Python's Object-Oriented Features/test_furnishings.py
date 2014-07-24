import unittest
from furnishings import *

class TestFurnishings(unittest.TestCase):

    def test_map_the_home(self):
        home = []
        home.append(Bed('Bedroom'))
        home.append(Sofa('Living Room'))
        map_home = map_the_home(home)
        self.assertTrue(isinstance(map_home, dict))
        self.assertTrue('Bedroom' in map_home)
        self.assertTrue('Living Room' in map_home)
        self.assertTrue(isinstance(map_home['Bedroom'], list))
        self.assertTrue(isinstance(map_home['Living Room'], list))
        
if __name__ == "__main__":
    unittest.main()
