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