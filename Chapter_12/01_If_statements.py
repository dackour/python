# If Statements
#a = int(input('Choose a number between 1-60: '))
a = 0

if a > 30:
    print('a > 30')
elif a < 30:
    print('a < 30')
else:
    print('a = 30')

if 1:
    print('True')

if not 1:
    print('true')
else:
    print('false')

x = 'killer rabbit'

if x == 'roger':
    print('shave and haircut')
elif x == 'bugs':
    print('whatsap doc')
else:
    print('Run away! Run away!')

choice = 'ham'
print({'spam': 1.25,  # A dictionary based switch
       'ham': 1.99,  # Use has_key or get for default
       'eggs': 0.99,
       'bacon': 1.10}[choice])

if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print(branch.get('spam', 'Bad choice'))
print(branch.get('bacon', 'Bad choice'))

choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

x = 1
if x:
    y = 2
    if y:
        print('block 2')
    print('block 1')
print('block 0')

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)  # Prints 8 'SPAM'
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)  # Prints 'SPAMNISPAMNISPAMNI'

L = ['Good',
     'Bad',
     'Ugly']  # Open pairs may span lines

a, b, c, d, e, f = (1, 1, 1, 1, 1, 1)
if (a == b and c == d and
    d == e and e == f):
    print('new')  # Parentheses allows continuation and is obvious

x = 1 + 2 + 3 \
    + 4  # Omitting the \ makes this very different!

x = 1; y = 2; print(x)  # More than one simple statement

S = """
aaaa
bbbb
cccc
"""

S = ('aaaa'
     'bbbb'
     'cccc')  # Comments here are ignored

if 1: print('hello')  # Simple statement on header line

