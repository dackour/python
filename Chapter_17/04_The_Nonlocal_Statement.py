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