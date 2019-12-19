# Python Scope Basics
# Scope Example

# Global scope
X = 99  # X and func assigned in module: global


def func(Y):  # Y and Z assigned in function: locals
    # Local scope
    Z = X + Y  # X is a global
    return Z


print(func(1))  # func in module: result=100

# The builtin scope

import builtins
print(dir(builtins))

print(zip)  # The normal way

import builtins  # The hard way for customizations
print(builtins.zip)

print(zip is builtins.zip)  # Same object, different lookups

print(len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith('__')]))

X = 88  # Global X

def func1():
    X = 99  # Local X: hides global, but we want this here

func1()
print(X)  # Prints 88 unchanged
