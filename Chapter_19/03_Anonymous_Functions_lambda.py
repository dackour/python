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


