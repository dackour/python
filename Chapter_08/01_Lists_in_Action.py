print(len([1, 2, 3]))  # Length

print([1, 2, 3] + [4, 5, 6])  # Concatenation

print(['Ni!'] * 4)  # Repetition

print(str([1, 2]) + '34')  # Same as "[1, 2]" + "34"

print([1, 2] + list('34'))  # Same as [1, 2] + ['3', '4']

print(3 in [1, 2, 3])  # Membership

for x in [1, 2, 3]:
    print(x, end=' ')  # Iteration (2.X uses: print x,)

print('\n')

res = [c * 4 for c in 'SPAM']  # List comprehensions
print(res)

res = []
for c in 'SPAM':  # List comprehension equivalent
    res.append(c * 4)
print(res)

print(list(map(abs, [-1, -2, 0, 1, 2])))

L = ['spam', 'Spam', 'SPAM!']
print(L[2])  # Offset start at zero
print(L[-2])  # Negative count from the right
print(L[1:])  # Slicing fetches sections

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])
print(matrix[1][1])

L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs'  # Index assignment
print(L)

L[0:2] = ['eat', 'more'] # Slice assignment: delete+insert
print(L)                 # Replaces items 0, 1

L = [1, 2, 3]
L[1:2] = [4, 5]  # Replacement/insertion
print(L)
L[1:1] = [6, 7]  # Insertion replace nothing
print(L)
L[1:2] = []  # Deletion inserting nothing
print(L)

L = [1]
L[:0] = [2, 3, 4]  # Insert all at :0 an empty slice at front
print(L)
L[len(L):] = [5, 6, 7]  # Insert all at len(L) and empty slice at end
print(L)
L.extend([8, 9, 10])  # Insert all at end, named method
print(L)

L = ['eat', 'more', 'SPAM!']
L.append('please')  # Append method call add item at end
print(L)
L.sort()  # Sort list items ('S' < 'e')
print(L)

L = ['abc', 'ABD', 'aBe']
L.sort()  # Sort with mixed case
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower)  # Normalize to lower case
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)  # Change sort order
print(L)

L = ['abc', 'ABD', 'aBe']
print(sorted(L, key=str.lower, reverse=True))
print(L)
L = ['abc', 'ABD', 'aBe']
print(sorted([x.lower() for x in L], reverse=True))  # Pretransform items : differs!

L = [1, 2]
L.extend([3, 4, 5])  # Add many items at the end like in-place +
print(L)
print(L.pop())  # Delete and return last item (by default: -1)
print(L)
L.reverse()  # In place reversal method
print(L)
print(list(reversed(L)))  # Reversal built-in with a result (iterator)

L = []
L.append(1)  # Push on to stack
L.append(2)
print(L)
print(L.pop())  # Pop off stack
print(L)

L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))  # Index of an object (search/find)
L.insert(1, 'toast')  # Insert at position
print(L)
L.remove('eggs')  # Delete by value
print(L)
print(L.pop(1))  # Delete by position
print(L)
print(L.count('spam'))  # Number of occurrences

L = ['spam', 'eggs', 'ham', 'toast']
del L[0]  # Delete one item
print(L)
del L[1:]  # Delete an entire section
print(L)   # Same as L[1:] = []

L = ['Already', 'got', 'one']
L[1:] = []
print(L)
L[0] = []
print(L)
