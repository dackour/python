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