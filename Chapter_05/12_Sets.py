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

z = x.intersection(y)  # Same as x & y
print(z)
z.add('SPAM')  # Insert one item
print(z)
z.update(set(['X', 'Y']))  # Merge in place union
print(z)
z.remove('b')  # Delete one item
print(z)

for item in set('abc'): print(item * 3)

S = set([1, 2, 3])
print(S | set([3, 4]))  # Expressions require both to be sets
#print(S | [3, 4])
print(S.union([3, 4]))  # But their methods allow any iterable
print(S.intersection((1, 3, 5)))
print(S.issubset(range(-5, 5)))

set([1, 2, 3, 4])  # Built-in call (all)
{1, 2, 3, 4}  # Newer set literals (2.7, 3.x)

print(set([1, 2, 3, 4]))  # Built-in same as in 2.6
print(set('spam'))  # Add all items in an iterable

print({1, 2, 3, 4})  # Set literals: new in 3.x (and 2.7)
S = {'s', 'p', 'a', 'm'}
print(S)

S.add('alot')  # Methods work as before
print(S)

S1 = {1, 2, 3, 4}
print(S1 & {1, 3})  # Intersection
print({1, 5, 3, 6} | S1)  # Union
print(S1 - {1, 3, 4})  # Difference
print(S1 > {1, 3}) # Superset

print(S1 - {1, 2, 3, 4})  # Empty sets print differently
print(type({}))  # Because {} is an empty dictonary

S = set()  # Initialize an empty set
S.add(1.23)
print(S)

print({1, 2, 3} | {3, 4})
#print({1, 2, 3} | [3, 4])
print({1, 2, 3}.union([3, 4]))
print({1, 2, 3}.union({3, 4}))
print({1, 2, 3}.union(set([3, 4])))
print({1, 2, 3}.intersection((1, 3, 5)))
print({1, 2, 3}.issubset(range(-5, 5)))

print(S)
#S.add([1, 2, 3])  # Only immutable objects work in a set
#S.add({'a':1})
S.add((1, 2, 3))
print(S)  # No list or dict, but tuple OK
print(S | {(4, 5, 6), (1, 2, 3)})  # Union: same as S.union(...)
print((1, 2, 3) in S)  # Membership: by complete values
print((1, 4, 3) in S)

print({x ** 2 for x in [1, 2, 3, 4]})  # 3.x/2.7 set comprehension
print({x for x in 'spam'})  # Same as set('spam')
print({c * 4 for c in 'spam'})  # Set of collected expression results
print({c * 4 for c in 'spamham'})

S = {c * 4 for c in 'spam'}
print(S | {'mmmm', 'xxxx'})
print(S & {'mmmm', 'xxxx'})

L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))
L = list(set(L))  # Remove duplicates
print(L)

print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))  # But order may change