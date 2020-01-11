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
