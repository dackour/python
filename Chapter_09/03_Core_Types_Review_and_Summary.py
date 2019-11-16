L = ['abc', [(1, 2), ([3], 4)], 5]
print(L[1])
print(L[1][1])
print(L[1][1][0])
print(L[1][1][0][0])

X = [1, 2, 3]
L = ['a', X, 'b']  # Embed references to X object
D = {'x': X, 'y': 2}
print(L)

X[1] = 'surprise'  # Changes all three references!
print(L)
print(D)
L2 = L[:]
print(L)
print(L2)
L2[0] = 'b'
print(L)
print(L2)

L = [1, 2, 3]
D = {'a': 1, 'b': 2}

A = L[:]  # Instead of A = L (or list(L))
B = D.copy()  # Instead of B = D (ditto for sets)
A[1] = 'Ni'
B['c'] = 'spam'
print(L, D)
print(A, B)

X = [1, 2, 3]
L = ['a', X[:], 'b']  # Embed copies of X's object
D = {'x': X[:], 'y': 2}

Y = [1, [2, 3], 4]
import copy
X = copy.deepcopy(Y)  # Fully copy an arbitrarily nested object Y
print(X)
X2 = Y.copy()
print(X2)

L1 = [1, ('a', 3)]  # Same value unique objects
L2 = [1, ('a', 3)]

print(L1 == L2, L1 is L2)  # Equivalent? Same object?

S1 = 'spam'
S2 = 'spam'

print(S1 == S2, S1 is S2)

S1 = 'A very very very longer string'
S2 = 'A very very very longer string'

print(S1 == S2, S1 is S2)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
print(L1 < L2, L1 == L2, L1 > L2)  # Less, equal, greater: tuple of results

# Python27
#11 == '11'  # Equality does not convert non-numbers
#False
#11 >= '11'  # 2.X compares by type name string int,str
#False
#['11', '22'].sort()  # Ditto for sorts
#[11, '11'].sort()

#Python33
print(11 == '11')  # Equality works but magnitude does not
#11 >= '11'
#TypeError
['11', '22'].sort()  # Ditto for sorts
#[11, '11'].sort()
#TypeError
print(11 > 9.123)  # Mixed numbers convert to highest type
print(str(11) >= '11', 11 >= int('11'))  # Manual conversion force the issue

#Python27
D1 = {'a': 1, 'b': 2}
D2 = {'a': 1, 'b': 3}
#D1 == D2  # Dictionary equality: 2.x + 3.x
#False
#D1 < D2  # Dictionary magnitude: 2.x only

#Python33
#D1 = {'a': 1, 'b': 2}
#D2 = {'a': 1, 'b': 3}
#D1 == D2
#False
#D1 < D2
#TypeError


print(list(D1.items()))
print(sorted(list(D1.items())))

print(sorted(D1.items()) < sorted(D2.items()))  # Magnitude test in 3.X
print(sorted(D1.items()) > sorted(D2.items()))

L = [None] * 100
print(L)

print(bool(1))
print(bool('spam'))
print(bool({}))

print(type([1]) == type([1]))  # Compare to type of another list
print(type([1]) == list)  # Compare to list type name
print(isinstance([1], list))  # Test if list or customization thereof

import types  # types has names for other types
def f(): pass
type(f)  == types.FunctionType

L = [1, 2, 3]
M = ['X', L, 'Y']  # embed a eference to L
print(M)
L[1] = 0  # Changes M too
print(M)

L = [1, 2, 3]
M = ['X', L[:], 'Y']  # Embed a copy of L (or list(L) or L.copy())
L[1] = 0  # Changes only L not M
print(L)
print(M)

L = [4, 5, 6]
X = L * 4  # Like [4, 5, 6] + [4, 5, 6] + ...
Y = [L] * 4  # [L] + [L] + ... = [L, L,...]
print(X)
print(Y)
L[1] = 0  # Impacts Y but not X
print(X)
print(Y)

L = [4, 5, 6]
Y = [list(L)] * 4  # Embed a (shared) copy of L
L[1] = 0
print(Y)

Y[0][1] = 99  # All four copies are still the same
print(Y)

L = [4, 5, 6]
Y = [list(L) for i in range(4)]
print(Y)
Y[0][1] = 99
print(Y)

L = ['grail']  # append reference to same object
L.append(L)  # Generates cycle in  object [...]
print(L)