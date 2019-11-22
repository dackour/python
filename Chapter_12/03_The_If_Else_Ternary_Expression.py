# The_If_Else_Ternary_Expression

X = 1
A = 0
Y = 1
Z = 2

if X:
    A = Y
else:
    A = Z

A = Y if X else Z
print(A)

A = 't' if 'spam' else 'f'  # For strings nonempty means true
print(A)

A = 't' if '' else 'f'
print(A)

A = ((X and Y) or Z)
A = Y if X else Z

A = [Z, Y][bool(X)]
print(['f', 't'][bool('')])
print(['f', 't'][bool('spam')])

A = ''
B = 'spam'
C = ''
X = A or B or C or None  # Select first non empty
print(X)

default = None
X = A or default

if B:
    print(B)  # Test object directly

if B != '':
    print(B)  # Than compare it to empty value

L = [1, 0, 2, 0, 'spam', '', 'ham', []]
print(list(filter(bool, L)))  # Get true values
print([x for x in L if x])  # Comprehensions
print(any(L), all(L))  # Aggregate truth

