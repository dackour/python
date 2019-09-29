print(1 < 2)  # Less than
print(2.0 >= 1)  # Greater than or equal mixed type 1 converted to 1.0
print(2 == 2)  # Equal value
print(2.0 != 2.0)  # Not equal value

x = 2
y = 4
z = 6

print(x < y < z)  # Chained comparisons range tests
print(x < y and y < z)

print(x < y > z)
print(x < y and y > z)

print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)

print(1 == 2 < 3)  # Same as 1 == 2 and 2 < 3

print(1.1 + 2.2 == 3.3)  # Shouldn't be true?
print(1.1 + 2.2)  # Close to 3.3 but not exactly: limited precision
print(int(1.1 + 2.2) == int(3.3))  # Ok if convert see also round floor trunc ahead
                                   # Decimals and fractions (ahead) may hel here too
