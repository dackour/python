# Sets
X = set('spam')  # Make a set out of a sequence in 2.x and 3.x
print(X)
Y = {'h', 'a', 'm'}  # Make a set with set literals in 3.x and 2.7
print(Y)
print(X, Y)  # A tuple of two sets without parentheses
print(X & Y)  # Intersection
print(X | Y)  # Union
print(X - Y)  # Difference
print(X > Y)  # Superset

setcomp = {n ** 2 for n in [1, 2, 3, 4]}  # Set comprehensions in 3.x and 2.7
print(setcomp)

print(list(set([1, 2, 1, 3, 1])))  # Filtering out duplicates (possibly reordered)
print(set('spam') - set('ham'))  # Finding differences in collections
print(set('spam') == set('asmp'))  # Order-neutral equality tests (== is False)
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

print(1 / 3)  # Floating point (add .0 in Python 2.0)
print((2 / 3) + (1 / 2))

import decimal  # Decimals fixed precision

d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

from fractions import Fraction  # Fraction numerator+denominator

f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))

print(1 > 2, 1 < 2)  # Booleans
print(bool('spam'))  # object's boolean value

X = None  # None placeholder
print(X)

L = [None] * 100  # Initializes al list of 100 Nones
print(L)

# How to break your codes flexibility

print(type(L))  # Types: type of L list type object
print(type(type(L)))  # Even types are objects

if type(L) == type([]):  # Type testing if you must...
    print('yes')

if type(L) == list:  # Using the type name
    print('yes')

if isinstance(L, list):  # Object oriented test
    print('yes')


# User-Defined Classes

class Worker:
    def __init__(self, name, pay):  # Initialize when created
        self.name = name  # self is a new object
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]  # Split string on blanks

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)  # Update pay in place


bob = Worker('Bob Smith', 50000)  # Make two instances
sue = Worker('Sue Jones', 60000)  # Each has the name and pay attrs

print(bob.lastName())  # Call method bob is self
print(sue.lastName())  # Sue is the self subject

sue.giveRaise(.10)  # Update sue pay
print(sue.pay)