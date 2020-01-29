# List Comprehensions and Functional Tools
# List Comprehensions Versus map

print(ord('s'))

res = []
for x in 'spam':
    res.append(ord(x))  # Manual result collection

print(res)

res = list(map(ord, 'spam'))  # apply function to sequence (or other)
print(res)

res = [ord(x) for x in 'spam']  # Apply expression to sequence (or other)
print(res)

# Adding Tests and Nested Loops: filter

print([x for x in range(5) if x % 2 == 0])

print(list(filter((lambda x: x % 2 == 0), range(5))))

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

print(res)

print([x ** 2 for x in range(10) if x % 2 == 0])

print(list(map((lambda x: x ** 2), filter((lambda x: x % 2 == 0), range(10)))))

# Formal comprehension syntax
