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
    x = y + z  # No need to declare y,z LEGB rule


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
# thismod.py
var = 99  # GGlobal variable == module attribute


def local():
    var = 0  # Change local var


def glob1():
    global var  # Declare global (normal)
    var += 1  # Change globar var


def glob2():
    var = 0  # Change local var
    #import thismod  # Import myself
    #thismod.var  # change global var

def glob3():
    var = 0  # Change local var
    import sys  # Import system table
    #glob = sys.modules['thismod']  # Get module object (or use __name__)
    #glob.var += 1  # Change global var


def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)
