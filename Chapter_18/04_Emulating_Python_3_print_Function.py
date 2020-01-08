# Emulating the Python 3.X print Function

import sys


def print3(*args, **kargs):
    sep = kargs.get('sep', ' ')  # Keyword arg defaults
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print3(1, 2, 3)
print3(1, 2, 3, sep='')  # Suppress seperator
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...')  # Various object types
print3(4, 5, 6, sep='', end='')  # Suppress newline
print3(7, 8, 9)
print3()  # Add newline (or blank line)

print3(1, 2, 3, sep='??', end='\n', file=sys.stderr)  # Redirect to file

# Using Keyword-Only Arguments


def print4(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print4('test', sep='--', end='\t')


def print5(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('Extra Keywords: %s' % kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)


print('\n')

print5('1', '2', '3', sep='??', end='\t')
