a = 3
b = a

a = 3
b = a
a = 'spam'

a = 3
b = a
a = a + 2

L1 = [2, 3, 4]
L2 = L1
L1 = 24

L1 = [2, 3, 4]  # A mutable object
L2 = L1  # Make a reference to same object
L1[0] = 24 # An in place change
print(L1)  # L1 is different
print(L2)  # But so is L2!

L1 = [2, 3, 4]
L2 = L1[:]  # Make a copy of L1 (or list(L1), copy.copy(L1), etc.# )
L1[0] = 24
print(L1)
print(L2)  # L2 is not changed

import copy
Y = [0, 1, 2]
X = copy.copy(Y)  # Make top-level "shallow" copy of any object Y
X = copy.deepcopy(Y)  # Make deep copy of an object Y: copy all nested parts

x = 42
x = 'shrubbery'  # Reclaim 42 now?

L = [1, 2, 3]
M = L  # L and M reference the same object
print(L == M)  # Same values
print(L is M)  # Same objects

L = [1, 2, 3]
M = [1, 2, 3]  # L and M reference different objects
print(L == M)  # Same values
print(L is M)  # Different objects

X = 42
Y = 42  # Should be two different objects
print(X == Y)
print(X is Y)  # Same object anyhow: coaching at work!

import sys
print(sys.getrefcount(1))  # 100 pointers to this shared piece of memory
