# Iterations first look
for x in [1, 2, 3, 4]: print(x ** 2, end=' ')
print('\n')
for x in (1, 2, 3, 4): print(x ** 3, end=' ')
print('\n')
for x in 'spam': print(x * 2, end=' ')
print('\n')

print(open('script2.py').read())

f = open('script2.py')  # Read a four-line script in this directory
print(f.readline())  # Readline loads one line on each call
print(f.readline())
print(f.readline())
print(f.readline())  # Last lines may have a \n or not
print(f.readline())  # Returns empty string at the end of file

f = open('script2.py')  # __next__ loads one line on each call too
f.__next__()  # But raises an exception at end of file
f.__next__()  # Use f.next() in 2.x or next(f) in 2.x or 3.x
f.__next__()
f.__next__()
#f.__next__()

for line in open('script2.py'):  # Use file iterators to read lines
    print(line.upper(), end='')  # Calls __next__ catches StopIteration

print('\n')

for line in open('script2.py').readlines():
    print(line.upper(), end='')

print('\n')

f = open('script2.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')

print('\n')

# Manual Iteration: iter and next

f = open('script2.py')
print(f.__next__(), end='')  # Call iteration method directly
print(f.__next__(), end='')

f = open('script2.py')
print(next(f), end='')  # The next(f) built-in calls f.__next__() in 3.x
print(next(f), end='')  # next(f) => [3.x: f.__next__()], [2.x: f.next()]

L = [1, 2, 3]
I = iter(L)  # Obtain a iterator object from iterable
print(I.__next__())  # Call iterators next to advance to next item
print(I.__next__())  # Or use I.next() in 2.x, next(I) in either line
print(I.__next__())
#print(I.__next__())

f = open('script2.py')
print(iter(f) is f)
print(iter(f) is f.__iter__())
print(f.__next__())

L = [1, 2, 3]
print(iter(L) is L)
#L.__next__()  #Err

I = iter(L)
print(I.__next__())
print(next(I))  # Same as I.__next__()

L = [1, 2, 3]
for X in L:  # Automatic iteration
    print(X ** 2, end=' ')  # Obtains iter, calls __next__, catches exceptions

print('\n')

I = iter(L)  # Manual iteration: what for loops usually do
while True:
    try:  # try statement catches exceptions
        X = next(I)  # Or call I.__next__() in 3.x
    except StopIteration:
        break
    print(X ** 2, end=' ')

print('\n')

# Other built-in Type Iterables

D = {'a': 1, 'b': 2, 'c': 3}
for key in D.keys():
    print(key, D[key])

I = iter(D)
print(next(I))
print(next(I))
print(next(I))
#print(next(I))  #Err

for key in D:
    print(key, D[key])

import os
P = os.popen('dir')
print(P.__next__())
print(P.__next__())
#print(next(P))  #Err

P = os.popen('dir')
I = iter(P)
print(next(I))
print(I.__next__())

R = range(5)
print(R)  # Ranges are iterables in 3.x
I = iter(R)  # Use iteration protocol to produce results
print(next(I))
print(next(I))
print(list(range(5)))  # Or use list to collect all results at once

E = enumerate('spam')  # Enumerate is iterable too
print(E)
I = iter(E)
print(next(I))  # Generate results with iteration protocol
print(next(I))  # Or use list to force generation to run
print(list(enumerate('spam')))


