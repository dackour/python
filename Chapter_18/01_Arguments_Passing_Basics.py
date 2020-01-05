# Arguments
# Arguments and Shared References


def f(a):  # a is assigned to (references) the passed object
    a = 99  # Changes local variable a only


b = 88
f(b)  # a and b both reference same 88 initally
print(b) # b is not changed


def changer(a, b):  # arguments assigned references to objects
    a = 2  # Changes local names value only
    b[0] = 'spam'  # Changes shared object in place


X = 1
L = [1, 2]  # Caller
changer(X, L) # Pass immutable and mutable objects
print(X, L)  # X is unchanged, L is different!

X = 1
a = X  # They share the same object
a = 2  # Resets a only X is still 1
print(X)

L = [1, 2]
b = L  # They share the same object
b[0] = 'spam'  # In-place change L sees the change too
print(L)

# Avoiding Mutable Argument Changes
L = [1, 2]
changer(X, L[:])  # Pass a copy so our L does not change


def changer(a, b):
    b = b[:]  # copy input list so we dont impact caller
    a = 2
    b[0] = 'spam'  # changes our list copy only

print(L)
print(b)

L = [1, 2]
# changer(X, tuple(L))  # Pass a tuple, so changes are errors

# Simulating Output Parameters and Multiple Results


def multiple(x, y):
    x = 2  # Changes local names only
    y = [3, 4]
    return x, y  # Return multiple new values in a tuple


X = 1
L = [1, 2]
X, L = multiple(X, L)  # Assign results to callers names
print(X, L)
