# The nonlocal statement in 3.x


def tester(start):
    state = start  # Referencing nonlocals works normally
    def nested(label):
        print(label, state)  # Remembers state in enclosing scope
    return nested


F = tester(0)
F('spam')
F('ham')


def tester(start):
    state = start  # Referencing nonlocals works normally
    def nested(label):
        print(label, state)
        #state += 1  # cannot change by default (never in 2.X)
    return nested


#F = tester(0)
#F('spam')


def tester(start):
    state = start  # Each call gets its own state
    def nested(label):
        nonlocal state  # Remembers state in enclosing scope
        print(label, state)
        state += 1  # Allowed to change it if nonlocal
    return nested


F = tester(0)
F('spam')  # Increments state on each call
F('ham')
F('eggs')

G = tester(42)  # Make a new tester that starts at 42
G('spam')
G('eggs')  # My state information updated to 43
F('bacon')  # But F's is where it left off at 3
# Each call has different state information

# Boundary cases

'''
def tester(start):
    def nested(label):
        nonlocal state  # Nonlocals must already exist in enclosing def!
        state = 0
        print(label, state)
    return nested
'''

def tester(start):
    def nested(label):
        global state  # Globals don't have to exist yet when declared
        state = 0  # This creates the name in the module now
        print(label, state)
    return nested


F = tester(0)
F('abc')
print(state)

'''
spam = 99
def tester():
    def nested():
        nonlocal spam  # Must be in def, not the module!
        print('Current=', spam)
        spam += 1
    return nested
'''
