# Generator Functions and Expressions


def gensquares(N):
    for i in range(N):
        yield i ** 2  # Resume here later


for i in gensquares(5):  # Resume function
    print(i, end=' : ')  # Print last yielded value

print('\n')

x = gensquares(4)
print(x)

print(next(x))  # Same as x.__next__() in 3.x
print(next(x))  # Use x.next() or next() in 2.x
print(next(x))
print(next(x))
#print(next(x))  # StopIteration exeception

y = gensquares(5)  # returns a generator which is its own iterator
print(iter(y) is y)  # iter() is not required: a no-op here
print(next(y))  # Can run next() immediately

# Why generator functions?