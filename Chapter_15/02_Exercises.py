# Part 3 Exercises

# 1
S = 'spam'

for c in S:
    print(ord(c))

x = 0
for c in S:
    x += ord(c)  # Or x = x + ord(c)

print(x)

x = []
for c in S:
    x.append(ord(c))

print(x)
print(list(map(ord, S)))  # List required in 3.x not 2.x
print([ord(c) for c in S])  # map and list comprehensions automate list builders

# 2
for i in range(50):
    print('hello %d\n\a' % i)

# 3
D = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
print(D)

keys = list(D.keys())  # list() required in 3.X, not in 2.X
keys.sort()
for key in keys:
    print(key, '=>', D[key])

for key in sorted(D):  # Better, in more recent Pythons
    print(key, '=>', D[key])

# 4a
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    i += 1
else:
    print(X, 'not found')

# 4b
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for p in L:
    if (2 ** X) == p:
        print((2 ** X), 'was found at', L.index(p))
        break
else:
    print(X, 'not found')

# 4c
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# 4d
L = []
X = 5

for i in range(7): L.append(2 ** i)
print(L)

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# 4e
X = 5
L = list(map(lambda x: 2**x, range(7)))
print(L)

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')
