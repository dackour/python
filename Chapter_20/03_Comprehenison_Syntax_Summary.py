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