print('\nSequence Operations\n')

L = [123, 'spam', 1.23]     # A list of three different-type objects
print(len(L))               # Number of items in list

print(L)
print(L[0])                 # Indexing by position
print(L[:-1])               # Slicing a list returns a new list

print(L + [4, 5, 6])        # Concat/repeat make new lists too

print(L * 2)

print(L)                    # We are not changing orginal list

print('\nType-Specific Operations\n')

print(L.append('NI'))       # Growing add object at end of list
print(L)

print(L.pop(2))             # Shrinking: delete an item in the middle
print(L)                    # del L[2] deletes from a list too

M = ['bb', 'aa', 'cc']
print(M)
M.sort()
print(M)
M.reverse()
print(M)

print('\nNesting\n')

M = [[1, 2, 3],             # A 3x3 matrix as nested list
     [4, 5, 6],             # Code can span lines if bracketed
     [7, 8, 9]]

print(M)

print(M[1])                 # Get row 2
print(M[1][2])              # Get row 2, then get item 3

print('\nComprehensions\n')

col1 = [row[0] for row in M]    # Collect the items in column 1
col2 = [row[1] for row in M]    # Give me row[1] for each row in matrix M
col3 = [r[2] for r in M]
print(col1)
print(col2)
print(col3)

newColumn = [row[1] + 1 for row in M]   # Add 1 to each item in column 2
print(newColumn)

myFilter = [row[1] for row in M if row[1] % 2 == 0]   # filter out odd items
print(myFilter)

myDiag1 = [M[i][i] for i in [0, 1, 2]]  # Collect diagonal from matrix
print(myDiag1)

myDiag2 = [M[i][j] for i,j in [(0, 2), (1, 1), (2, 0)]]  # Collect reverse diagonal using tuple
print(myDiag2)

myDoubles = [c * 2 for c in 'spam']  # Repeat characters in a string
print(myDoubles)

print(list(range(4)))  # 0..3 (list() required in 3.X)
print(list(range(-6, 7, 2)))  # -6 to +6 by step of 2 (need list() in 3.X)

myValues1 = [[x ** 2, x ** 3] for x in range(4)]  # Multiple values "if" filters
print(myValues1)

myValues2 = [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0]  # Multiple values "if" filters
print(myValues2)


