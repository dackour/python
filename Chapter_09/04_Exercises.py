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