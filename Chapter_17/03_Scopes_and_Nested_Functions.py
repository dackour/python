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