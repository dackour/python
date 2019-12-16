# New Iterables in Python 3.x
print(zip('abc', 'xyz'))  # An iterable in Python 3.x (a list in 2.x)

print(list(zip('abc', 'xyz')))  # Force list of results in 3.x to display

Z = zip((1, 2), (3, 4))  # Unlike 2.x lists, cannot index, etc
#print(Z[0])

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
#print(next(M)) Err StopIteration

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

