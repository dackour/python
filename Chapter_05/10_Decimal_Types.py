print(0.1 + 0.1 + 0.1 - 0.3) # Should be zero but it is close

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))

import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))  # Default 28 digit

decimal.getcontext().prec = 4  # Fixed precision
print(decimal.Decimal(1) / decimal.Decimal(7))

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))  # Closer to 0

print(1999 + 1.33)  # This has more disgits in memory than displayed in 3.3

decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print(pay)

decimal.getcontext().prec = 28  # Return to default value of 28 digits
print(Decimal('1.00') / Decimal('3.0'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal('1.00') / Decimal('3.0'))

print(Decimal('1.00') / Decimal('3.0'))
