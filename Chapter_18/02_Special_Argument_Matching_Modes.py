# Special Argument Matching Modes
# Key word and Default Examples


def f(a, b, c): print(a, b, c)


f(1, 2, 3)

# Keywords
f(c=3, b=2, a=1)

f(1, c=3, b=2)  # a gets 1 by  position, b and c passed by name


def fpearson(name, age, job):
    print('Your name is', name)
    print('Your age is', age)
    print('Your job is', job)


fpearson(name='Bob', age=40, job='dev')

# Defaults


def f(a, b=2, c=3): print(a, b, c)  # a required, b and c optional


f(1)
f(a=1)

f(1, 4)  # Override defaults
f(1, 4, 5)

f(1, c=6)

# Combining keywords and defaults


def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))


func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)

# Arbitrary Arguments Examples
# Headers Collecting arguments


def f(*args): print(args)

f()
f(1)
f(1, 2, 3, 4)


def f(**args): print(args)


f()
f(a=1, b=2)


def f(a, *pargs, **kargs): print(a, pargs, kargs)


f(1, 2, 3, x=1, y=1)

# Calls Unpacking arguments


def func(a, b, c, d): print(a, b, c, d)


args = (1, 2)
args += (3, 4)
func(*args)  # Same as func(1, 2, 3, 4)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)

func(*(1, 2), **{'d': 4, 'c': 3})  # Same as func(1,2,d=4,c=3)
func(1, *(2, 3), **{'d': 4})  # Same as func(1,2,3,d=4)
func(1, c=3, *(2, ), **{'d': 4})  # Same as func(1,2,c=3,d=4)
func(1, * (2, 3), d=4)  # Same as func(1,2,3,d=4)
func(1, *(2, ), c=3, **{'d': 4})  # Same as func(1,2,c=3,d=4)

# Applying functions generically


def tracer(func, *pargs, **kargs):  # Accept arbitrary arguments
    print('calling:', func.__name__)
    return func(*pargs, **kargs)  # Pass along arbitrary arguments


def func(a,b,c,d):
    return a + b + c + d


print(tracer(func, 1, 2, c=3, d=4))

# The defunct apply built-in (Python 2.X)
# Python 3.X Keyword Only Arguments


def kwonly(a, *b, c):
    print(a, b, c)


kwonly(1, 2, c=3)
kwonly(a=1, c=3)
#kwonly(1, 2, 3)  # err


def kwonly(a, *, b, c):
    print(a, b,c )


kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)
#kwonly(1, 2, 3)  # err
#kwonly(1)  # err


def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)


kwonly(1)
kwonly(1, c=3)
kwonly(a=1)
kwonly(c=3, b=2, a=1)
#kwonly(1, 2)  # err


def kwonly(a, *, b, c='spam'):
    print(a, b, c)


kwonly(1, b='eggs')
#kwonly(1, c='eggs')  # err
#kwonly(1,2)  # err


def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)


kwonly(3, c=4)
kwonly(3, c=4, b=5)
#kwonly(3)  # err
#kwonly(1, 2, 3)  # err

# Ordering rules


def f(a, *b, c=6, **d): print(a, b, c, d)  # Collect args in header


f(1, 2, 3, x=4, y=5)  # Default used
f(1, 2, 3, x=4, y=5, c=7)  # Override default
f(1, 2, 3, c=7, x=4, y=5)  # Anywhere in keywords


def f(a, c=6, *b, **d): print(a, b, c, d)  # c is not keyword-only here


f(1, 2, 3, x=4)


def f(a, *b, c=6, **d): print(a, b, c, d)  # KW-only between * and **


f(1, *(2, 3), **dict(x=4, y=5))  # Unpack args at call
f(1, *(2, 3), **dict(x=4, y=5), c=7)  # Keywords before **args
f(1, *(2, 3), c=7, **dict(x=4, y=5))  # Override default
f(1, c=7, *(2, 3), **dict(x=4, y=5))  # After or before *
f(1, *(2, 3), **dict(x=4, y=5, c=7))  # Keyword only in **

# Why keyword only arguments
# The min Wakeup call
# Full credit


def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return  first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


print(min1(3, 4, 1, 2))
print(min2('bb', 'aa'))
print(min3([2,2], [1,1], [3,3]))

# Bonus Points


def max1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg > res:
            res = arg
    return res


def max2(first, *rest):
    for arg in rest:
        if arg > first:
            first = arg
    return  first


def max3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[-1]


print(max1(3, 4, 1, 2))
print(max2('bb', 'aa'))
print(max3([2,2], [1,1], [3,3]))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y


def grtrthan(x, y): return x > y


print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

# The punch Line


