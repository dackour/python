# Other Iteration Contexts
for line in open('script2.py'):  # Use file iterators
    print(line.upper(), end='')

uppers = [line.upper() for line in open('script2.py')]
print(uppers)

map(str.upper, open('script2.py'))  # map is itself an iterable in 3.x
print(list(map(str.upper, open('script2.py'))))

print(sorted(open('script2.py')))

print(list(zip(open('script2.py'), open('script2.py'))))

print(list(enumerate(open('script2.py'))))

print(list(filter(bool, open('script2.py'))))  # noneempty = True

import functools, operator

print(functools.reduce(operator.add, open('script2.py')))

print(list(open('script2.py')))
print(tuple(open('script2.py')))
print('&&'.join(open('script2.py')))

a, b, c, d = open('script2.py')  # Sequence assignment
print(a, d)

a, *b = open('script2.py')  # 3.x extended form
print(a, b)

print('y = 2\n' in open('script2.py'))  # Membership test
print('x = 2\n' in open('script2.py'))

L = [11, 22, 33, 44]  # Slice assignment
L[1:3] = open('script2.py')
print(L)

L = [11]
L.extend(open('script2.py'))  # List extend method
print(L)

L = [11]
L.append(open('script2.py'))  # List.append does not iterate
print(L)
print(list(L[1]))

print(set(open('script2.py')))

C = {line for line in open('script2.py')}
print(C)

print(list(enumerate(open('script2.py'))))
D = {ix: line for ix, line in enumerate(open('script2.py'))}
print(D)

S = {line for line in open('script2.py') if line[0] == 'p'}
print(S)

D = {ix: line for (ix, line) in enumerate(open('script2.py')) if line[0] == 'p'}
print(D)

print(list(line.upper() for line in open('script2.py')))  # See Chapter 20

print(sum([3, 2, 4, 1, 5, 0]))  # Sum expects numbers only

print(any(['spam', '', 'ni']))

print(all(['spam', '', 'ni']))

print(max([3, 2, 4, 1, 5, 0]))

print(min([3, 2, 4, 1, 5, 0]))

print(max(open('script2.py')))  # Line with max/min string value

print(min(open('script2.py')))


def f(a, b, c, d): print(a, b, c, d, sep='&')

f(1, 2, 3, 4)
f(*[1, 2, 3, 4])  # Unpacks into arguments
f(*open('script2.py'))  # Iterates by lines too!

X = (1, 2)
Y = (3, 4)

print(list(zip(X, Y)))  # Zip tuples: returns an iterable

A, B = zip(*zip(X, Y))
print(A)
print(B)
