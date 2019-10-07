x = 1  # 1 decimal is 0001
b1 = x << 2  # Shift left 2 bits 0100
print('{:b}'.format(b1))
b2 = x | 2  # Bitwise OR (either bit = 1): 0011
print('{:b}'.format(b2))
b3 = x & 1  # Bitwise AND (both bits = 1): 0001
print('{:b}'.format(b3))

X = 0b0001  # binary literals
X << 2  # Shift left
print(X)
print(bin(X << 2))  # Binary digits string
print(bin(X | 0b010))  # Bitwise OR either
print(bin(X & 0b1))  # Bitwise AND both

X = 0xFF
print(bin(X))
print(X ^ 0b10101010)  # Bitwise XOR either but not both
print(bin(X ^ 0b10101010))
print(int('01010101', 2))  # Digits to number string to int per base
print(hex(85))  # Number to digits Hex digit string

X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)
print(bin(256), (256).bit_length(), len(bin(256)) - 2)
