from fractions import Fraction

x = Fraction(1, 3)  # numerator  denominator
y = Fraction(4, 6)  # Simplified to 2, 3 by gcd

print(x)
print(y)

print(x + y)
print(x - y)  # Results are exact numerator, denominator
print(x * y)

print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))

a = 1 / 3.0  # Only asa accurate as floating-point hardware
b = 4 / 6.0  # Can lose precision over many calculations
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)

print(0.1 + 0.1 + 0.1 - 0.3)  # This should be 0 close but not exact

print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

print(1 / 3)  # Use a ".0" in Python 2.x for true "/"

print(Fraction(1, 3))  # Numeric accuracy two ways

import decimal

decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))

print((1 / 3) + (6 / 12))  # Use a ".0" in Python 2.x for true "/"

print(Fraction(6, 12))  # Automatically simplified

print(Fraction(1, 3) + Fraction(6, 12))

print(decimal.Decimal(str(1 / 3)) + decimal.Decimal(str(6 / 12)))

print(1000.0 / 1234567890)
print(Fraction(100, 123456789))  # Substantially simpler!

print((2.5).as_integer_ratio())  # Float object method

f = 2.5
z = Fraction(*f.as_integer_ratio())  # Convert float to fraction: two args
print(z)  # Same as Fractions(5, 2) the * is a special syntax that expands tuple into individual args

print(x)  # x from prior interaction
print(x + z)  # 5/2 + 1/3 = 15/6 + 2/6

print(float(x))  # Convert fraction to float
print(float(z))

print(float(x + z))
print(17 / 6)

print(Fraction.from_float(1.75))  # Convert float to fraction other way
print(Fraction(*(1.75).as_integer_ratio()))

print(x)
print(x + 2)  # Fraction + int = Fraction
print(x + 2.0) # Fraction + float = float
print(x + (1./3))  # Fraction + float = float
print(x + (4./3))
print(x + Fraction(4, 3))  # Fraction + Fraction = Fraction

print(4.0 / 3)
print((4.0 / 3).as_integer_ratio())  # Precision loss from float

print(x)
a = x + Fraction(*(4.0 / 3).as_integer_ratio())
print(a)

print(22517998136852479 / 13510798882111488)  # 5/3 or close to it

print(a.limit_denominator(10))  # Simplify to closest fraction
