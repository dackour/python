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

setcomp = {n ** 2 for n in [1,2,3,4]}  # Set comprehensions in 3.x and 2.7
print(setcomp)

print(list(set([1, 2, 1, 3, 1])))  # Filtering out duplicates (possibly reordered)
print(set('spam') - set('ham'))  # Finding differences in collections
print(set('spam') == set('asmp'))  # Order-neutral equality tests (== is False)
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

print(1/3)  # Floating point (add .0 in Python 2.0)
print((2/3) + (1/2))

import decimal  # Decimals fixed precision
d = decimal.Decimal('3.141')
print(d + 1)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
