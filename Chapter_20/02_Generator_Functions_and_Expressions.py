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


def gen():
    for i in range(10):
        X = yield  i
        print(X)


G = gen()
next(G)  # Must call next first to start generator
G.send(77)  # Advance and send value to yield expression
G.send(88)
next(G)  # next() and X.__next__() send None

# Generator Expressions: Iterables Meet Comprehensions

L = [x ** 2 for x in range(4)]  # List comprehension: build a list
print(L)

G = (x ** 2 for x in range(4))  # Generator expression: make an iterable
print(G)

L = list(x ** 2 for x in range(4))  # List comprehension equivalence
print(L)

G = (x ** 2 for x in range(4))
print(iter(G) is G)  # iter(G) optional: __iter__ returns self

print(next(G))  # Generator objects: automatic methods
print(next(G))
print(next(G))
print(next(G))
#print(next(G))  # StopIteration Error
print(G)

for num in (x ** 2 for x in range(4)):  # Calls next() automatically
    print('%s, %s' % (num, num / 2.0))

print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))

a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))
print(a, c)

print(sum(x ** 2 for x in range(4)))  # Parens optional
print(sorted(x ** 2 for x in range(4)))  # Parens optional
print(sorted((x ** 2 for x in range(4)), reverse=True))  # Parens optional

# Generator expressions versus map

L = list(map(abs, (-1, -2, 3, 4)))  # Map function on tuple
print(L)

L = list(abs(x) for x in (-1, -2, 3, 4))  # Generator expression
print(L)

L = list(map(lambda x: x * 2, (1, 2, 3, 4)))  # Non function case
print(L)

L = list(x * 2 for x in (1, 2, 3, 4))  # Simpler as generator?

line = 'aaa,bbb,ccc'
S = ''.join([x.upper() for x in line.split(',')])  # Makes a pointless list
print(S)

S = ''.join(x.upper() for x in line.split(','))  # Generates results
print(S)

S = ''.join(map(str.upper, line.split(',')))  # Generates results
print(S)

S = ''.join(x * 2 for x in line.split(','))  # Simpler as generator?
print(S)

S = ''.join(map(lambda x: x * 2, line.split(',')))
print(S)

L = [x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]]  # Nested comprehensions
print(L)

L = list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4))))  # Nested maps
print(L)

L = list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4)))  # Nested generators
print(L)

import math
L = list(map(math.sqrt, (x ** 2 for x in range(4))))  # Nested combinations
print(L)

L = list(map(abs, map(abs, map(abs, (-1, 0, 1)))))  # Nesting gone bad?
print(L)

L = list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1))))
print(L)

L = list(abs(x) * 2 for x in (-1, -2, 3, 4))  # Unnested equivalents
print(L)

L = list(math.sqrt(x ** 2) for x in range(4))  # Flat is often better
print(L)

L = list(abs(x) for x in (-1, 0, 1))
print(L)

# Generator expressions versus filter

