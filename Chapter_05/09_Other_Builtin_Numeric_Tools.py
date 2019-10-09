import math

print(math.pi)  # Common constants
print(math.e)

print((2 * math.pi) / 180)
print(2 * math.pi / 180)
print(math.sin(2 * math.pi / 180))  # Sine, tangent, cosine

print(math.sqrt(144), math.sqrt(2))  # Square root

print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)  # Exponentiation (power)

print(abs(-42.0), sum((1, 2, 3, 4)))  # Absolute value, summation

print(min(3, 1, 2, 4), max(3, 1, 2, 4))  # Minimum maximum

print(math.floor(2.567), math.floor(-2.567))  # Floor next-lower integer

print(math.trunc(2.567), math.trunc(-2.567))  # Truncate (drop decimal digits)

print(int(2.567), int(-2.567))  # Truncate (integer conversion)

print(round(2.567), round(2.467), round(2.567, 2))  # Round

print('%.1f' % 2.567, '{0:.2f}'.format(2.567))  # Round for display

print((1 / 3.0), round(1 /3.0, 2), ('%.2f' % (1 / 3.0)))

print(math.sqrt(144))  # Module
print(144 ** .5)  # Expression
print(pow(144, .5))  # Built-in

print(math.sqrt(1234567890))  # Larger numbers
print(1234567890 ** .5)
print(pow(1234567890, .5))

import random

print(random.random())
print(random.random())  # Random floats, integers, choices, shuffles
print(random.randint(1, 10))
print(random.randint(1, 10))

print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)
random.shuffle(suits)
print(suits)