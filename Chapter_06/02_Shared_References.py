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