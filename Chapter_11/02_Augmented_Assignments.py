# Augmented Assignments
X = 2
Y = 3
X = X + Y  # Traditional form
X += Y  # Newer augmented form

'''
X += Y
X &= Y
X -= Y
X |= Y
X *= Y
X ^= Y
X /= Y
X >>= Y
X %= Y
X <<= Y
X **= Y
X //= Y
'''

x = 1
x = x + 1
print(x)
x += 1
print(x)

S = 'spam'
S += 'SPAM'  # Implied concatenation
print(S)

L = [1, 2]
L = L + [3]  # Concatenate slower
print(L)
L.append(4)  # Faster but in place
print(L)

L = L + [5, 6]  # Concatenate slower
print(L)
L.extend([7, 8])  # Faster but in place
print(L)

L += [9, 10]  # Mapped to L.extend([9,10)
print(L)

L = []
L += 'spam'  # += and extend allow any sequence, but + does not !
print(L)
#L = L + 'spam'  # Error

L = [1, 2]
M = L  # L and M reference the same object
L = L + [3, 4]  # Concatenation makes a new object
print(L, M)  # Changes L but not M

L = [1, 2]
M = L
L += [3, 4]  # But += really means extend
print(L, M)  # M sees the in-place change too!