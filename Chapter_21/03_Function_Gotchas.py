# Function Gotchas
# Local names are Detected Statically

X = 99


def selector():  # X used but not assigned
    print(X)  # X found in global scope


selector()


def selector():
    print(X)  # Does not yet exist
    X = 88  # X classified as local name (everywhere)
# Can also happen for "import X", "def X"...


#selector()  # UnboundLocalError


def selector():
    global X  # Force X to be global (everywhere)
    print(X)
    X = 88


selector()

X = 99


def selector():
    import __main__  # Import enclosing module
    print(__main__.X)  # Qualify to get to global version of name
    X = 88  # unqualified X classified as local
    print(X)  # Prints local version of name


selector()

# Default and Mutable Objects


def saver(x=[]):  # Saves away a list object
    x.append(1)  # Changes same object each time!
    print(x)


saver([2])  # Default not used
saver()  # Default used
saver()  # Grows on each call!
saver()


def saver(x=None):
    if x is None:  # No argument passed?
        x = []  # Rune code to make a new list each time
    x.append(1)  # Changes new list object
    print(x)


saver([2])
saver()
saver()


def saver():
    saver.x.append(1)
    print(saver.x)


saver.x = []
saver()
saver()
saver()

# Functions without returns


def proc(x):
    print(x)  # No return is a None return


x = proc('testing 123...')
print(x)

L = [1, 2, 3]
L = L.append(4)  # append is a procedure
print(L)  # Append changes list in place
