print(10 / 4)  # Diff ers in 3.x keeps remainder
print(10 / 4.0)  # Same in 3.x  keeps remainder
print(10 // 4)  # Same in 3.x truncates remainder
print(10 // 4.0)  # Same in 3.x truncates to floor

Y = 10
Z = 4
X = Y // Z  # Always truncates, always an int result for ints in 2.x and 3.x
print(X)

X = Y / float(Z)  # guarantees float division with remainder in either 2.x or 3.x
print(X)

# Floor versus truncation
print('Floor versus truncation')
import math
print(math.floor(2.5))  # Closest number below value
print(math.floor(-2.5))
print(math.trunc(2.5))  # Truncate fraction part (toward zero)
print(math.trunc(-2.5))

print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)  # Truncates to floor rounds to first lower integer 2.5 becomes 2, -2.5 becomes -3