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

for line in open('script2.py').readlines():
    print(line.upper(), end='')


