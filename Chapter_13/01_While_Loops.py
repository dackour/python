# While Loops
#while True:
#    print('Type Ctrl-C to stop me!')

x = 'spam'
while x:  # While x is not empty
    print(x, end=' ')
    x = x[1:]  # Strip first character off x

print('\n')

a = 0; b = 10
while a < b:  # One way to code counter loops
    print(a, end=' ')
    a += 1  # Or a = a + 1

print('\n')

x = 10
while x:
    x = x - 1  # Or x -= 1
    if x % 2 != 0: continue  # odd skip print
    print(x, end=' ')

print('\n')

x = 10
while x:
    x = x -1
    if x % 2 == 0:  # Even? -- print
        print(x, end=' ')

print('\n')


while True:
    name = input('Enter name: ')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)

y = input('Enter number: ')
x = int(y) // 2
print(x)
while x > 1:
    if int(y) % int(x) == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')


