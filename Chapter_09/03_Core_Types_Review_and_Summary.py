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


