# Comprehension Syntax Summary

print([x * x for x in range(10)])  # List comprehension: build list
# Like list(generator expr)
print((x * X for x in range(10)))  # Generator expression: produces items
# Parens are often optional
print({x * x for x in range(10)})  # Set comprehension, 3.X and 2.7
# {x, y} is a set in these versions too
print({x: x * x for x in range(10)})  # Dictionary comprehension, 3.x and 2.7

# Scopes and Comprehensions Variables
print((X for X in range(5)))

X = 99
print([X for X in range(5)])  # 3.x: Generator, set, dict and list localize
print(X)

Y = 99
for Y in range(5): pass  # But loop statements do not localize names
print(Y)

X = 'aaa'
def func():
    Y = 'bbb'
    print(''.join(Z for Z in X + Y))  # Z comprehension, Y local, X global

func()

X = 99
print([X for X in range(5)])  # 2.X List does not localize its names, like for
print(X)

Y = 99
for Y in range(5): pass  # for loops do not localize names in 2.x or 3.x
print(Y)

# Comprehending Set and Dictionary Comprehensions

print({x * x for x in range(10)})  # Comprehension

print(set(x * x for x in range(10)))  # Generator and type name

print({x : x * x for x in range(10)})

print(dict((x, x * x) for x in range(10)))

# print(x)  # Loop variable localized in 2.X + 3.X

res = set()
for x in range(10):  # Set comprehension equivalent
    res.add(x * x)

print(res)

res = {}
for x in range(10):  # Dict comprehension equivalent
    res[x] = x * x

print(res)

print(x)  # Localized in comprehension expressions, but not in loop statements

G = ((x, x * x) for x in range(10))
print(next(G))
print(next(G))
print(next(G))

# Extended Comprehension Syntax for Sets and Dictionaries

print([x * x for x in range(10) if x % 2 == 0])  # Lists are ordered

print({x * x for x in range(10) if x % 2 == 0})  # But sets are not

print({x: x * x for x in range(10) if x % 2 == 0})  # Neither are dict keys

print([x + y for x in [1, 2, 3] for y in [4, 5, 6]])  # Lists keep duplicates

print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})  # But sets do not

print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})  # Neither do dict keys

print({x + y for x in 'ab' for y in 'cd'})

print({x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'})

print({k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})

print({k.upper(): k *2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})


