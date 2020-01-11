# Function Objects Attributes and Annotations
# Indirect Function Calls: First Class Objects


def echo(message):  # Name echo assigned to function object
    print(message)


echo('Direct call')  # Call object through original name

x = echo  # Now x references the function too
x('Indirect call!')  # Call object through name by adding ()


def indirect(func, arg):
    func(arg)  # Call passed in object by adding ()


indirect(echo, 'Argument call!')  # Pass the function to another function

schedule = [(echo, 'Spam!'), (echo, 'Ham!')]
for (func, arg) in schedule:
    func(arg)  # Call functions embedded in containers


def make(label):  # Make a function but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo


F = make('Spam')  # Label in enclosing scope is retained
F('Eggs')  # Call the function that make returned
F('Toast')

# Function Introspection


def func(a):
    b = 'spam'
    return print(b * a)


func(8)

print(func.__name__)
print(dir(func))
print(func.__code__)
print(dir(func.__code__))
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)

# Function Attributes

print(func)
func.count = 0
func.count += 1
print(func.count)

func.handles = 'Button-Press'
print(func.handles)
print(dir(func))


def f(): pass


f.handler = 'Some handler piece'
dir(f)
print(len(dir(f)))
print([x for x in dir(f) if not x.startswith('__')])

# Function Annotations in 3.X


def func(a, b, c):
    return a + b + c


print(func(1, 2, 3))


def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func.__annotations__)


def func(a: 'spam', b, c: 99):
    return a + b + c


print(func(1, 2, 3))
print(func.__annotations__)

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])


def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


print(func(1, 2, 3))
print(func())  # 4 + 5 + 6 (all defaults)

print(func(1, c=10))  # 1 + 5 + 10 (keywords work normally)
print(func.__annotations__)