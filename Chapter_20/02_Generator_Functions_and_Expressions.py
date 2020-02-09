# Generator Functions and Expressions


def gensquares(N):
    for i in range(N):
        yield i ** 2  # Resume here later


for i in gensquares(5):  # Resume function
    print(i, end=' : ')  # Print last yielded value

print('\n')

x = gensquares(4)
print(x)

print(next(x))  # Same as x.__next__() in 3.x
print(next(x))  # Use x.next() or next() in 2.x
print(next(x))
print(next(x))
#print(next(x))  # StopIteration exeception

y = gensquares(5)  # returns a generator which is its own iterator
print(iter(y) is y)  # iter() is not required: a no-op here
print(next(y))  # Can run next() immediately

# Why generator functions?


def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res


for x in buildsquares(5): print(x, end=' : ')

print('\n')

for x in [n ** 2 for n in range(5)]:
    print(x, end=' : ')

print('\n')

for x in map((lambda n: n ** 2), range(5)):
    print(x, end=' : ')

print('\n')


def ups(line):
    for sub in line.split(','): # Substring generator
        yield sub.upper()


T = tuple(ups('aaa,bbb,ccc'))  # All iteration contexts
print(T)

D = {i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))}
print(D)

# Extended generator function protocol: send versus next

