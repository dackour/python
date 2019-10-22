x = set('abcde')
y = set('bdyxz')

print(x)
print(y)

print(x - y)  # Difference
print(x | y)  # Union
print(x & y)  # Intersection
print(x ^ y)  # Symmetric difference XOR
print(x > y, x < y)  # Superset, subset

print('e' in x)  # Membership sets
