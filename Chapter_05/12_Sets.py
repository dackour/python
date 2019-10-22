x = set('abcde')
y = set('bdyxz')

print(x)
print(y)

print(x - y)  # Difference
print(x | y)  # Union
print(x & y)  # Intersection
print(x ^ y)  # Symmetric difference XOR wsystko poza czescia wspolna
print(x > y, x < y)  # Superset, subset

print('e' in x)  # Membership sets

print('e' in 'Camelot', 22 in [11, 22, 33])  # But works on other types too
