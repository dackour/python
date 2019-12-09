# List Comprehensions: A First Detailed Look
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)

L = [x + 10 for x in L]
print(L)

# List Comprehension Basics

res = []
for x in L:
    res.append(x + 10)
print(res)

# Using ListComprehensions on Files

f = open('script2.py')
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]
print(lines)

lines = [line.rstrip() for line in open('script2.py')]
print(lines)

lines = [line.upper() for line in open('script2.py')]
print(lines)

lines = [line.rstrip().upper() for line in open('script2.py')]
print(lines)

lines = [line.split() for line in open('script2.py')]
print(lines)

lines = [line.replace(' ', '!') for line in open('script2.py')]
print(lines)

lines = [('sys' in line, line[:5]) for line in open('script2.py')]
print(lines)

# Extended List Comprehensions Syntax

