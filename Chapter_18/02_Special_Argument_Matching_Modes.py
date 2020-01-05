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
