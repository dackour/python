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