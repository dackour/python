print(len([1, 2, 3]))  # Length

print([1, 2, 3] + [4, 5, 6])  # Concatenation

print(['Ni!'] * 4)  # Repetition

print(str([1, 2]) + '34')  # Same as "[1, 2]" + "34"

print([1, 2] + list('34'))  # Same as [1, 2] + ['3', '4']

print(3 in [1, 2, 3])  # Membership

for x in [1, 2, 3]:
    print(x, end=' ')  # Iteration (2.X uses: print x,)

print('\n')

res = [c * 4 for c in 'SPAM']  # List comprehensions
print(res)

res = []
for c in 'SPAM':  # List comprehension equivalent
    res.append(c * 4)
print(res)

print(list(map(abs, [-1, -2, 0, 1, 2])))

L = ['spam', 'Spam', 'SPAM!']
print(L[2])  # Offset start at zero
print(L[-2])  # Negative count from the right
