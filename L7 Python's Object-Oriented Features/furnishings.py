"""Here are your instructions:



Create a Python3_Homework07 project and assign it to your Python3_Homework working set. In the Python3_Homework07/src 
folder, create a program named furnishings.py that includes a Furnishing class. During instantiation, this class should
ask for a "room" argument. Then, create the following classes that inherit from the Furnishing class: Sofa, Bookshelf, 
Bed, and Table.

Use the built-in list type to record the furniture in your own home that matches the classes above. So for example, you
might have:


>>> from furnishings import * >>> home = [] >>> home.append(Bed('Bedroom'))>>> home.append(Sofa('Living Room')) 
Now, write a map_the_home() function to convert that to a built-in dict type where the rooms are the individual keys and
the associated value is the list of furniture for that room. If we ran that code against what we display in our command
line, we might see:


>>> map_the_home(home){'Bedroom': [<furnishings.Bed object at 0x39f3b0>], 'Living Room': [<furnishings.Sofa object at 
0x39f3b0>]}  
Also write a counter() function that prints the types of furniture and how many there are of each type. The results, based
on our example:


>>> counter(home)Beds: 1Bookshelves: 0Sofas: 1Tables: 0Your project should meet the following conditions:•The program 
should be able to produce the same results as the list above. 
•You should include a test_furnishings.py program that tests the map_the_home() function.

Submit furnishings.py and test_furnishings.py when they are working to your satisfaction.
"""

######################################################################################################################################################################################################

class Furnishing:
    def __init__(self, room):
        self.room = room

class Sofa(Furnishing):
    pass

class Bookshelf(Furnishing):
    pass

class Bed(Furnishing):
    pass
    
class Table(Furnishing):
    pass

def map_the_home(home):
    rooms = {} 
    for item in home: 
        room = item.room
        if room in rooms:
            rooms[room].append(item)
        else:
            rooms[room] = [item]
    return rooms

def counter(home):
    rooms_dict = {'Bed'      : ['Beds'       , 0], 
                'Bookshelf': ['Bookshelves', 0], 
                'Sofa'     : ['Sofas'      , 0], 
                'Table'    : ['Tables'     , 0]}
    
    for item in home:
        rooms_dict[item.__class__.__name__][1] += 1
    
    for value in rooms_dict.values():
        print("%s: %d" % (value[0], value[1]))
        
if __name__ == "__main__":
    home = []
    home.append(Bed('Bedroom'))
    home.append(Sofa('Living Room'))
    print(map_the_home(home))
    counter(home)
