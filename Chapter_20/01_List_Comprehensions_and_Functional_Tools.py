# List Comprehensions and Functional Tools
# List Comprehensions Versus map

print(ord('s'))

res = []
for x in 'spam':
    res.append(ord(x))  # Manual result collection

print(res)

res = list(map(ord, 'spam'))  # apply function to sequence (or other)
print(res)

res = [ord(x) for x in 'spam']  # Apply expression to sequence (or other)
print(res)

# Adding Tests and Nested Loops: filter

print([x for x in range(5) if x % 2 == 0])

print(list(filter((lambda x: x % 2 == 0), range(5))))

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

print(res)

print([x ** 2 for x in range(10) if x % 2 == 0])

print(list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))

# Formal comprehension syntax

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

print(res)

res = []
res = [x + y for x in 'spam' for y in 'SPAM']
print(res)

res = []
res = [x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')]
print(res)

res = []
res = [x + y + z for x in 'spam' if x in 'sm'
       for y in 'SPAM' if y in ('P', 'A')
       for z in '123' if z > '1']
print(res)

res = []
res = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(res)

res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))

print(res)

# Example: List Comprehensions and Matrixes

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print(M[1])  # Row 2

print(M[1][2])  # Row 2, item 3

res = []
res = [row[1] for row in M]  # Column 2
print(res)

res = []
res = [M[row][1] for row in (0, 1, 2)]  # Using offsets
print(res)

res = []
res = [M[i][i] for i in range(len(M))]  # Diagonal
print(res)

res = []
res = [M[i][len(M)-1-i] for i in range(len(M))]
print(res)

L = [[1, 2, 3], [4, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])):  # Update in place
        L[i][j] += 10

print(L)

res = []
res = [col + 10 for row in M for col in row]  # Assign to M to retain new value
print(res)

res = []
res = [[col + 10 for col in row] for row in M]
print(res)

res = []
for row in M:  # Statement equivalents
    for col in row:  # Indent parts further right
        res.append(col + 10)

print(res)

res = []
for row in M:
    tmp = []
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)

print(res)

res = []
res = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
print(res)

res = []
res = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
print(res)

res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)

print(res)

res = []
res = [[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)]
print(res)

res = []
for (row1, row2) in zip(M, N):
    tmp = []
    for (col1, col2) in zip(row1, row2):
        tmp.append(col1 * col2)
    res.append(tmp)

print(res)

# Don't Abuse List Comprehensions: KISS
