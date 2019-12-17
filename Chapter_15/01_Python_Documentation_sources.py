# Python Documentation Sources
import sys
print(dir(sys))

print(len(dir(sys)))  # Number names in sys
print(len([x for x in dir(sys) if not x.startswith('__')]))  # Non __X names only
print(len([x for x in dir(sys) if not x[0] == '_']))  # Non underscore names

print(dir([]))
print(dir(''))

print(len(dir([])), len([x for x in dir([]) if not x.startswith('__')]))
print(len(dir('')), len([x for x in dir('') if not x.startswith('__')]))

print([a for a in dir(list) if not a.startswith('__')])
print([a for a in dir(dict) if not a.startswith('__')])


def dir1(x): return print([a for a in dir(x) if not a.startswith('__')])

dir1(tuple)

print(dir(str) == dir(''))  # Same result, type name or literal
print(dir(list) == dir([]))

# Docstrings
import docstrings

print(docstrings.square(4))
print(docstrings.square.__doc__)

print(docstrings.__doc__)
print(docstrings.square.__doc__)
print(docstrings.Employee.__doc__)

print(sys.__doc__)
print(sys.getrefcount.__doc__)
print(int.__doc__)
print(map.__doc__)