# For Loops

for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')

print('\n')

sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x

print(1 + 2 + 3 + 4)
print(sum)

prod = 1
for item in [1, 2, 3, 4]: prod *= item
print(prod)
print(1 * 2 * 3 * 4)

S = 'lumberjack'
T = ("and", "I'm", "okay")

for x in S: print(x, end=' ')  # Iterate over a string

print('\n')

for x in T: print(x, end=' ')  # Iterate over a tuple

print('\n')

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:  # Tuple assignment at work
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])  # Use dict keys iterator and index

print(list(D.items()))
for (key, value) in D.items():  # Iterate over both keys and values
    print(key, '=>', value)

print(T)
for both in T:
    a, b = both  # Manual assignment equivalent
    print(a, b)

((a, b), c) = ((1, 2), 3)  # Nested sequences work too
print(a, b, c)
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)
for ((a, b), c) in [((1, 2), 3), ['XY', 6]]: print(a, b, c)

a, b, c = (1, 2, 3)  # Tuple assignment
print(a, b, c)
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:  # Used in for loop
    print(a, b, c)

a, *b, c = (1, 2, 3, 4)  # Extended seq assignment
print(a, b, c)
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:  # Manual slicing in 2.x
    a, b, c = all[0], all[1:3], all[3]
    print(a, b, c)

items = ['aaa', 111, (4, 5), 2.01]  # A set of objects
tests = [(4, 5), 3.14]  # Keys to search for

for key in tests:  # for all keys
    for item in items:  # for all items
        if item == key:  # check for a match
            print(key, 'was found')
            break
    else:
        print(key, 'not found!')

for key in tests:  # for all keys
    if key in items:  # let python check for a match
        print(key, 'was found')
    else:
        print(key, 'not found')

seq1 = 'spam'
seq2 = 'scam'

res = []  # Start empty
for x in seq1:  # Scan first sequence
    if x in seq2:  # Common item?
        res.append(x)  # Add to a result end

print(res)

res2 = [x for x in seq1 if x in seq2]  # Let Python collect results
print(res2)

file = open('test.txt')
while True:
    char = file.read(1)  # Read by character
    if not char: break  # Empty strings means end-of-file
    print(char)

for char in open('test.txt').read():
    print(char)

file = open('test.txt')
while True:
    line = file.readline()  # Read line by line
    if not line: break
    print(line.rstrip())  # Line already has a \n

file = open('test.txt', 'rb')
while True:
    chunk = file.read(10)  # Read by chunk up to 10 bytes
    if not chunk: break
    print(chunk)

for line in open('test.txt').readlines():
    print(line.rstrip())

for line in open('test.txt'):  # Use iterators best for text input
    print(line.rstrip())

for line in reversed(open('test.txt').readlines()):
    print(line.rstrip())