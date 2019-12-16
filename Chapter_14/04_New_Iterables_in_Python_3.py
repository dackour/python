# New Iterables in Python 3.x
print(zip('abc', 'xyz'))  # An iterable in Python 3.x (a list in 2.x)

print(list(zip('abc', 'xyz')))  # Force list of results in 3.x to display

Z = zip((1, 2), (3, 4))  # Unlike 2.x lists, cannot index, etc
# print(Z[0])

Z = list(zip((1, 2), (3, 4)))
print(Z[0])

M = map(lambda x: 2 ** x, range(3))
for i in M: print(i)

for i in M: print(i)  # Unlike 2.x lists, one pass only (zip too)

# The range iterable

R = range(10)  # Range returns an iterable, not a list
print(R)

I = iter(R)  # Make an iterator from the range iterable
print(next(I))  # Advance too the next result
print(next(I))  # What happens in for loops, comprehensions etc
print(next(I))

print(list(range(10)))  # to force a list if required

len(R)  # range also does len and indexing, but no others
print(R[0])
print(R[-1])
print(next(I))  # Continue taking from iterator, where left off
print(I.__next__())  # .next() becomes .__next__(), but use new next()

# The map, zip and filter iterables

M = map(abs, (-1, 0, 1))  # map returns an iterable, not a list
print(M)
print(next(M))  # Use iterator manually: exhausts results
print(next(M))  # These do not support len() or indexing
print(next(M))
# print(next(M)) Err StopIteration

for x in M: print(x)  # map iterator is now empty: one pass only

M = map(abs, (-1, 0, 1))  # Make a new iterable/iterator to scan again
for x in M: print(x)  # Iteration context auto call next()

print(list(map(abs, (-1, 0, 1))))  # Can force a real list if needed

Z = zip((1, 2, 3), (10, 20, 30))  # zip is the same: a one -pass iterator
print(Z)
print(list(Z))

for pair in Z: print(pair)  # Exhausted after one pass

Z = zip((1, 2, 3), (10, 20, 30))
for pair in Z: print(pair)  # Iterator used automatically or manually

Z = zip((1, 2, 3), (10, 20, 30))  # Manual iteration (iter() not needed)
print(next(Z))
print(next(Z))

print(filter(bool, ['spam', '', 'ni']))
print(list(filter(bool, ['spam', '', 'ni'])))

F = [x for x in ['spam', '', 'ni'] if bool(x)]
print(F)

F = [x for x in ['spam', '', 'ni'] if x]
print(F)

# Multiple vs Single Pass Iterators
R = range(3)  # Range allows multiple iterators
# next(R)  # Err range object is not an iterator

I1 = iter(R)
print(next(I1))
print(next(I1))
I2 = iter(R)  # Two iterators on one range
print(next(I2))
print(next(I1))  # I1 is at a different spot than I2

Z = zip((1, 2, 3), (10, 20, 30))
I1 = iter(Z)  # Two iterators on one zip
I2 = iter(Z)
print(next(I1))
print(next(I1))
print(next(I2))  # (3.x) I2 is at same spot as I1!

M = map(abs, (-1, 0, 1))  # Ditto for map (and filter)
I1 = iter(M); I2 = iter(M)
print(next(I1), next(I1), next(I1))
# next(I2)  # Err StopIteration (3.x) Single scan exhausted!

R = range(3)  # But range allows many iterators
I1, I2 = iter(R), iter(R)
print(next(I1), next(I1), next(I1))
print(next(I2))  # Multiple active scans, like 2.x lists

# Dictionary view Iterables

D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()  # A view object in 3.x, not a list
print(K)
# next(K)  #TypeError Views are not iterators themselves
I = iter(K)  # View iterables have an iterator
print(next(I))  # which can be used manually
print(next(I))  # but does not support len(), index

for k in D.keys(): print(k, end=' ')  # All iteration contexts use auto

print('\n')

K = D.keys()
print(list(K))  # Can still force a real list if needed

V = D.values()  # Ditto for values() and items() views
print(V)

# print(V[0])  # TypeError
print(list(V)[0])

print(list(D.items()))

for (k, v) in D.items(): print(k, v, end=' ')
print('\n')

print(D)  # Dictionaries still produce an iterator
I = iter(D)  # Returns next key on each iteration
print(next(I))
print(next(I))

for key in D: print(key, end=' ')  # Still no need to call keys() to iterate
print('\n')  # But keys is an iterable in 3.x too!

print(D)
for k in sorted(D.keys()): print(k, D[k], end=' ')
print('\n')

for k in sorted(D): print(k, D[k], end=' ')  # Best practice key sorting
print('\n')

# Other Iteration Topics
