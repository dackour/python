# Numbers
print(2 ** 16)  # 2 raised to the power 16
print(2 / 5, 2 / 5.0)  # Integer / truncates in 2.x, but not 3.x

# Strings
print('spam' + 'eggs')  # Concatenation
S= 'ham'
print('eggs ' + S)
print(S * 5)  # Repetition
print(S[:0])  # An empty slice at the front -- [0:0] Empty of smae type as object sliced
print('green %s and %s' % ('eggs', S))  # Formatting
print('green {0} and {1}'.format('eggs', S))

# Tuples
print(('x',)[0])  # Indexing a nsingle item tuple
print(('x', 'y')[1])  # Indexing a 2 item tuple

# Lists
L = [1, 2, 3] + [4, 5, 6]  # List operations
print(L, L[:], L[:0], L[-2], L[-2:])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print([L[2], L[3]])  # Fetch from offsets; store in a list
print(L)
L.reverse()  # Method reverse list in place
print(L)
L.sort()  # Method sort list in place
print(L)
print(L.index(4))  # Method offset of first four (search)

# Dictionaries
print({'a': 1, 'b': 2}['b'])  # Index dictionary by key
D = {'x': 1, 'y': 2, 'z': 3}
D['w'] = 0  # Create a new entry
print(D['x'] + D['w'])
print(D)
D[(1, 2, 3)] = 4  # A tuple used as a key (immutable)
print(D)
print(list(D.keys()), list(D.values()), (1, 2, 3) in D)  # Method key test

# Empties
print([[]], ['', [], (), {}, None])  # Lots of nothing: empty objects

# Indexing and slicing
L = [1, 2, 3, 4]
#print(L[4])  # Error
print(L[-1000:100])
print(L[3:1])  # Python scales out boundries L[3:3]
print(L)
L[3:1] = ['?']
print(L)

# Indexing, slicening and del
L = [1, 2, 3, 4]
L[2] = []
print(L)
L[2:3] = []
print(L)
del L[0]
print(L)
del L[1:]
print(L)
#L[1:2] = 1  # Error

# Tuple assignment
X = 'spam'
Y = 'eggs'
X, Y = Y, X
print(X)
print(Y)

# Dictionaries keys
D = {}
D[1] = 'a'
D[2] = 'b'
D[(1, 2, 3)] = 'c'
print(D)

# Dictionary indexing
D = {'a': 1, 'b': 2, 'c':3}
print(D['a'])
#print(D['d'])  # Error
D['d'] = 4
print(D)
L = [0, 1]
#L[2]  # Error
#L[2] = 3  # Error

# Generic operations
# 'x' + 1  # Error not the same type
# {} + {}  # Dictionaries are not sequences
[].append(9)
#''.append('s')  # Error append assumes target is mutable. strings are not
print(list({}.keys()))  # list() needed in 3.x, not 2.x
#[].keys()  # Error
print([][:])
print(''[:])

# String indexing
S = 'spam'
print(S[0][0][0][0][0])
L = ['s', 'p']
print(L[0][0][0])

# Immutable types
S = 'spam'
S = S[0] + 'l' + S[2:]
print(S)
S = S[0] + 'l' + S[2] + S[3]
print(S)

# Nesting
me = {'name': ('John', 'Q', 'Doe'), 'age': '?', 'job': 'engineer'}
print(me['job'])
print(me['name'][2])

# Files
file = open('exercise.txt', 'w')
file.write('Hello file word!\n')  # Or open().write()
file.close()

file = open('exercise.txt')  # 'r' is default open mode
print(file.read())  # Or print(open().read())