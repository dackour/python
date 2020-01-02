# Why nonlocals? State Retention Options


def tester(start):
    state = start  # Each call gets its own state
    def nested(label):
        nonlocal state  # Remembers state in enclosing scope
        print(label, state)
        state += 1  # Allowed to change it if nonlocal
    return nested


F = tester(0)
F('spam')  # State visible within closure only
#F.state  # Err

# States with globals a single copy only


def tester(start):
    global state
    state = start
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested


F = tester(0)
F('spam')  # Each call increments shared global state
F('eggs')

G = tester(42)  # Resets states single copy in global scope
G('toast')
G('bacon')
F('ham')  # But my counter has been overwritten!

# State with class


class Tester:  # Class based alternative
    def __init__(self, start):  # On object construction
        self.state = start  # save state explicit in new object
    def nested(self, label):
        print(label, self.state)  # Reference state explicitly
        self.state += 1  # Changes are always allowed


F = Tester(0)  # Create instance invoke __init__
F.nested('spam')  # F is passed to self
F.nested('ham')

G = Tester(42)  # Each instance gets new copy of state
G.nested('toast')  # Changing one does not impact others
G.nested('bacon')

F.nested('eggs')  # F's state is where it left off
print(F.state)  # state maybe accessed outside class


class Tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):  # Intercept direct instace calls
        print(label, self.state)  # So nested() not required
        self.state += 1


H = Tester(99)
H('juice')  # Invokes __call__
H('pancakes')

# state with function Attributes


def tester(start):
    def nested(label):
        print(label, nested.state)  # nested is in enclosing scope
        nested.state += 1  # Change attr, not nested itself
    nested.state = start  # Initial state after func defined
    return nested


F = tester(0)
F('spam')  # F is a nested with state attached
F('ham')
print(F.state)

G = tester(42)  # G hasown state, doesnt overwrite F
G('eggs')
F('ham')
F.state  # State is accessible and per-call
G.state
print(F is G)  # Different function objects

# state with mutables


def tester(start):
    def nested(label):
        print(label, state[0])  # Leverage in-place mutable change
        state[0] += 1  # Extra syntax deep magic
    state = [start]
    return nested

