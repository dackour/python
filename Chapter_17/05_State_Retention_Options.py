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