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

