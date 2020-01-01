# Scopes and nested Functions
X = 99  # Global scope name: not used


def f1():
    X = 88  # Enclosing def local
    def f2():
        print(X)  # Reference made in nested def
    f2()


f1()  # Prints 88: enclosing def local


def f1():
    X = 88
    def f2():
        print(X)  # Remembers X in enclosing def scope
    return f2  # Return f2 but dont call it


action = f1()  # Make a return function
action()  # Call it now: prints 88

# Factory functions: Closures


def maker(N):
    def action(X):  # Make and return action
        return X ** N  # action retains N from enclosing scope
    return action


f = maker(2)  # Pass to argument N
print(f)
print(f(3))  # Pass 3 to X, N remembers 2: 3 ** 2
print(f(4))  # 4 ** 2

g = maker(3)  # g remembers 3, f remembers 2
print(g(4))  # 4 ** 3
print(f(4))  # 4 ** 2


def maker(N):
    return lambda X: X ** N  # lambda functions retain state too


h = maker(3)
print(h(4))  # 4 ** 3 again

# Retaining Enclosing Scope State with defaults


def f1():
    x = 88
    def f2(x=x):  # Remember enclosing scope X with defaults
        print(x)
    f2()


f1()  # Prints 88


def f1():
    x = 88  # Pass along instead of nesting
    f2(x)  # Forward reference OK


def f2(x):
    print(x)  # Flat is still often better than nested

f1()


def func():
    x = 4
    action = (lambda n: x ** n)  # x remembered from enclosing def
    return action


x = func()
print(x(2))  # prints 16, 4 ** 2


def func():
    x = 4
    action = (lambda n, x=x: x ** n)  # Pass x in manually
    return action


def makeActions():
    acts = []
    for i in range(5):  # Tries to remember each i
        acts.append(lambda x: i ** x)  # But all remember same last it
    return acts


acts = makeActions()
print(acts[0])

print(acts[0](2))  # All are 4 ** 2, 4=value of last i
print(acts[1](2))  # This should be 1 ** 2 (1)
print(acts[2](2))  # This should be 2 ** 2 (4)
print(acts[4](2))  # Only this should be 4 ** 2 (16)

