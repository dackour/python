# Assignments Statements
nudge = 1  # Basic assignment
wink = 2
A, B = nudge, wink  # Tuple assignment
print(A, B)
[C, D] = [nudge, wink]  # List assignment
print(C, D)

nudge = 1
wink = 2
nudge, wink = wink, nudge  # Tuples: swap values
print(nudge,wink)  # Like T = nudge; nudge = wink; wink = T

[a, b, c] = (1, 2, 3)  # assign tuple of values to list of names
print(a, c)
(a, b, c) = 'ABC'  # assign string of characters to tuple
print(a, c)

string = 'SPAM'
a, b, c, d = string  # Same number on both sides
print(a, d)
#a,b,c = string  # Error if not

a, b, c = string[0], string[1], string[2:]  # Index and slice
print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]]  # Slice and concatenate
print(a, b, c)

a, b = string[:2]  # Same, but simpler
c = string[2:]
print(a, b, c)

(a, b), c = string[:2], string[2:]  # Nested sequences
print(a, b, c)

((a, b), c) = ('SP', 'AM')  # Paired by shape and position
print(a, b, c)

red, green, blue = range(3)
print(red, blue)

print(list(range(3)))  # list() required in Python 3.x only

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]  # See the next section for 3.x alternative
    print(front, L)
