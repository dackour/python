# The Global Statement
X = 88  # Global X


def func():
    global X
    X = 99  # Global X outside def


func()
print(X)  # Prints 99

y, z = 1, 2  # Global variables in module


def all_global():
    global x  # Declare global assigned
    x = y + z  # No need to declar y,z LEGB rule


# Program Design Minimize Global Variables
# Program Design Minimize Cross-File Changes

# first.py
X = 99  # This code doesnt know about second.py

# second.py
#import first
#print(first.X)  # OK references a name in another file
#first.X = 88  # But changing it can be too subtle and implicit

# first.py
X = 99


def setX(new):  # accessor make eternal changes explit
    global X  # and can manage access in a single place
    X = new

# second.py
#import first
#first.setX(88)  #Call the function intead of changing directly

# Other Ways to Access Globals
