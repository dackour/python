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

line = 'aa bbb c'
print(''.join(x for x in line.split() if len(x) > 1))  # Generator with if

print(''.join(filter(lambda x : len(x) > 1, line.split())))  # Similar to filter

print(''.join(x.upper() for x in line.split() if len(x) > 1))

print(''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))

print(''.join(x.upper() for x in line.split() if len(x) > 1))

res = ''
for x in line.split():  # Statement equivalent?
    if len(x) > 1:  # This is also a join
        res += x.upper()

print(res)

# Generator Functions Versus Generator Expressions

G = (c * 4 for c in 'SPAM')  # Generator expression
print(list(G))  # Force generator to produce all results


def timesfour(S):  # Generator function
    for c in S:
        yield c * 4

G = timesfour('spam')
print(list(G))  # Iterate automatically

G = (c * 4 for c in 'SPAM')
I = iter(G)  # Iterate manually (expression)
print(next(I))
print(next(I))

G = timesfour('spam')
I = iter(G)  # Iterate manually function
print(next(I))
print(next(I))

line = 'aa bbb c'

print(''.join(x.upper() for x in line.split() if len(x) > 1))  # Expression


def gensub(line):  # Function
    for x in line.split():
        if len(x) > 1:
            yield x.upper()


print(''.join(gensub(line)))  # But why generate

# Generators Are single-Iteration Objects

G = (c * 4 for c in 'SPAM')
print(iter(G) is G)  # My iterator is myself: G has __next__

G = (c * 4 for c in 'SPAM')  # Make a new generator
I1 = iter(G)  # Iterate manually
print(next(I1))
print(next(I1))
I2 = iter(G)  # Second iterator at same position!
print(next(I2))

print(list(I1))  # Collect the rest of I1's items
#print(next(I2))  # Other iterator exhausted too

I3 = iter(G)  # Ditto for new iterators
#print(next(I3))

I3 = iter(c * 4 for c in 'SPAM')  # New generator to start over
print(next(I3))


def timesthree(S):
    for c in S:
        yield c * 3


G = timesthree('spam')  # Generator functions work the same way
print(iter(G) is G)
I1, I2 = iter(G), iter(G)
print(next(I1))
print(next(I1))
print(next(I2))  # I2 at same position as I1

L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
print(next(I1))
print(next(I1))
print(next(I2))  # Lists support multiple iterators
del L[2:]  # Changes reflected in iterators
#print(next(I1))

# The Python 3.3 yield from Extension


def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i


print(list(both(5)))


def both2(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


print(list(both2(5)))

print(' : '.join(str(i) for i in both2(5)))

print('\n')

# Generation in Built-in Types, Tools, and Classes

D = {'a': 1, 'b': 2, 'c': 3}
x = iter(D)
print(next(x))
print(next(x))

for key in D:
    print(key, D[key])

for line in open('temp.txt'):
    print(line, end='')

print('\n')

# Generators and library tools: Directory walkers

import os
for (root, subs, files) in os.walk('..'):  # Directory walk generator
    for name in files:  # A python find operation
        if name.startswith('01_'):
            print(root, name)

G = os.walk(r'C:\Users\bsmela\PycharmProjects\python')
print(iter(G) is G)  # Single scan iterator: iter(G) optional
I = iter(G)
print(next(I))
print(next(I))
print(next(I))

# Generators and function application


def f(a, b, c): print('%s, %s, and %s' % (a, b, c))


f(0, 1, 2)  # Normal positionals
f(*range(3))  # Unpack range values: iterable in 3.x
f(*(i for i in range(3)))  # Unpack generator expressions values

D = dict(a='Bob', b='dev', c=40.5)
print(D)
f(a='Bob', b='dev', c=40.5)  # Normal keywords
f(**D)  # Unpack dict: key = value
f(*D)  # Unpack keys iterator
f(*D.values())  # Unpack view iterator: iterable in 3.X

for x in 'spam': print(x.upper(), end=' ')
print('\n')
list(print(x.upper(), end=' ') for x in 'spam')
print('\n')
print(*(x.upper() for x in 'spam'))

# Preview: User-defined iterables in classes
# Example Generating Scrambled Sequences
# Scrambling sequences

L, S = [1, 2, 3], 'spam'
for i in range(len(S)):  # For repeat counts 0..3
    S = S[1:] + S[:1]  # Move front item to the end
    print(S, end=' ')

print('\n')

for i in range(len(L)):
    L = L[1:] + L[:1]  # Slice so any sequence type works
    print(L, end=' ')

print('\n')

for i in range(len(S)):  # For positions 0..3
    X = S[i:] + S[:i]  # Rear part + front part (same effect)
    print(X, end=' ')

print('\n')


def scramble1(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res


print(scramble1('spam'))


def scramble2(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


print(scramble2('spam'))

for x in scramble2((1, 2, 3)):
    print(x, end=' ')

print('\n')

# Generator functions


def scramble3(seq):
    for i in range(len(seq)):
        seq = seq[i:] + seq[:i]  # Generator function
    yield seq  # Assignments work here


def scramble4(seq):
    for i in range(len(seq)):  # Generator function
        yield seq[i:] + seq[:i]  # yield one item per iteration


print(list(scramble4('spam')))  # List generates all results
print(list(scramble4((1, 2, 3))))  # Any sequence type works

for x in scramble4((1, 2, 3)):
    print(x, end=' ')

print('\n')

# Generator expressions

print(S)
G = (S[i:] + S[:i] for i in range(len(S)))  # Generator expression equivalent
print(list(G))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(F(S))
print(list(F(S)))
print(list(F([1, 2, 3])))

for x in F((1, 2, 3)):
    print(x, end=' ')
print('\n')

# Test client

def scramble5(seq):
    for i in range(len(seq)):  # Generator function
        yield seq[i:] + seq[:i]  # Yield one item per iteration


scramble6 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

# Dunno why it is not working there is no module inter2?
# from inter2 import intersect, union
#
#
# def tester(func, items, trace=True):
#     for args in scramble5(items):  # Use generator (or: scramble6(items))
#         if trace: print(args)
#         print(sorted(func(*args)))
#
#
# tester(intersect(), ('aab', 'abcde', 'ababab'))
# tester(intersect(), ([1, 2], [2, 3, 4], [1,6,2,7,,3]), False)

# Permutations: All possible combinations


def permute1(seq):
    if not seq:  # Shuffle any sequence: list
        return [seq]  # Empty sequence
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # Delete current node
            for x in permute1(rest):  # Permute the others
                res.append(seq[i:i+1] + x)  # Add node at front
        return res


def permute2(seq):
    if not seq:  # Shuffle any sequence: generator
        yield seq  # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]  # Delete current node
            for x in permute2(rest):  # Permute the others
                yield seq[i:i+1] + x  # Add node at front


print(list(scramble5('abc')))  # Simple scrambles: N

print(permute1('abc'))  # Permutations larger: N!

print(list(permute2('abc')))  # Generate all combinations

G = permute2('abc')  # Iterate (iter() not needed
print(next(G))
print(next(G))

for x in permute2('abc'): print(x)  # Automatic iteration

print(permute1('spam') == list(permute2('spam')))

print(len(list(permute2('spam'))), len(list(scramble5('spam'))))

print(list(scramble5('spam')))
print(list(permute2('spam')))


