# Anonymous Functions lambda
# Lambda Basics


def func(x, y, z): return x + y + z


print(func(2, 3, 4))

f = lambda x, y, z: x + y + z

print(f(2, 3, 4))

x = (lambda a = 'fee', b = 'fie', c = 'foe': a + b + c)
print(x('wee'))


def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)  # title in enclosing def scope
    return action  # Return a function object


act = knights()
msg = act('Robin')  # Robin passed to x
print(msg)
print(act)  # act a function not its result

# Why use lambda?

L = [lambda x: x ** 2,  # Inline function definition
     lambda x: x ** 3,
     lambda x: x ** 4]  # A list of three callable functions

for f in L:
    print(f(2))  # Prints 4, 8, 16

print(L[0](3))  # Prints 9


def f1(x): return x ** 2
def f2(x): return x ** 3  # Define named functions
def f3(x): return x ** 4


L = [f1, f2, f3]  # Reference by a name

for f in L:
    print(f(2))  # Prints 4, 8, 16

print(L[0](3))  # Prints 9

# Multi branch switches the finale

key = 'got'
D = {'already': (lambda: 2 + 2),
     'got': (lambda: 2 * 4),
     'one': (lambda: 2 ** 6)}[key]()

print(D)


def f1(): return 2 + 2
def f2(): return 2 * 4
def f3(): return 2 ** 6


key = 'one'
D2 = {'already': f1, 'got': f2, 'one': f3}[key]()
print(D2)

# How (Not) to Obfuscate Your Python Code


a = ''
b = 'something'
c = ''
if a:
    b
else:
    c

b if a else c
((a and b) or c)

lower = (lambda x, y: x if x < y else y)
print(lower('bb', 'aa'))
print(lower('aa', 'bb'))

import sys
showall = lambda x: list(map(sys.stdout.write, x))  # 3.X must use list
t = showall(['spam\n', 'toast\n', 'eggs\n'])  # 3.X can use print

#showall = lambda x: [sys.stdout.wirte(line) for line in x]
#t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))

showall = lambda x: [print(line, end='') for line in x]
showall = lambda x: print(*x, sep='', end='')

# Scopes: lambdas Can Be Nested Too


def action(x):
    return (lambda y: x + y) # Make and return function, remember x


act = action(99)
print(act)
print(act(2))  # Call what action returned

action = (lambda x: (lambda y: x + y))
act = action(99)
print(act(3))
print(((lambda x: (lambda y: x + y))(99))(4))

import sys
from tkinter import Button, mainloop
x = Button(
    text='Press me',
    command=(lambda:sys.stdout.write('Spam\n')))
x.pack()
mainloop()  # This maybe optional in console mode


# Functional programing
