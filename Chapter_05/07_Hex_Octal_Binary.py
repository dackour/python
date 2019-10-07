print(0o1, 0o20, 0o377)  # Octal literals base 8 digits 0-7
print(0x01, 0x10, 0xFF)  # Hex literals base 16 digits 0-9/A-F
print(0b1, 0b10000, 0b11111111)  # Binary literals base 2 digits 0-1
print(0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0)))  # How hex/binary map to decimal
print(0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0)))
print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0)))

print(oct(64), hex(64), bin(64))  # Numbers to digits strings