template = '{0}, {1} and {2}'  # By position
print(template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}'  # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'  # By both
print(template.format('ham', motto='spam', food='eggs'))

template = '{}, {} and {}'  # By relative position
print(template.format('spam', 'ham', 'eggs'))  # New in 3.1 and 2.7

template = '%s, %s and %s'  # Same via expression
print(template % ('spam', 'ham', 'eggs'))

template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))

print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))

X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(X)

print(X.split(' and '))

Y = X.replace('and', 'but under no circumstances')
print(Y)

import sys
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))

print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))

somelist = list('SPAM')
print(somelist)

print('first={0[0]}, third={0[2]}'.format(somelist))

print('first={0}, last={1}'.format(somelist[0], somelist[-1]))  # [-1] fails in fmt

parts = somelist[0], somelist[-1], somelist[1:3]  # [1:3] fails in fmt
print('first={0}, last={1}, middle={2}'.format(*parts))  # *parts unpacks tuple into individual function arguments
print('first={}, last={}, middle={}'.format(*parts))  # Or '{}' in 2.7/3.1

# {filename component !conversionflag :formatspec}
# formatspec:
# [[fill]align][sign][#][0][width][,][.precision][typecode]

print('{0:10} = {1:10}'.format('spam', 123.4567))  # In Python 3.3
print('{:10} = {:10}'.format('spam', 123.4567))

print('{0:>10} = {1:<10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))

print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
print('{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop')))

print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))

print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))  # Hex, octal, binary

print(bin(255), int('11111111', 2), 0b11111111)  # Other to/from binary

print(hex(255), int('FF', 16), 0xFF)  # Other to/from hex

print(oct(255), int('377', 8), 0o377)
'''
# Other to/from octal, in 3.X
2.X prints and accepts 0377
'''
print('{0:.2f}'.format(1 / 3.0))  # Parameters hardcoded
print('%.2f' % (1 / 3.0))  # Ditto for expression

print('{0:.{1}f}'.format(1 / 3.0, 4))  # Take value from arguments
print('%.*f' % (4, 1 / 3.0))  # Ditto for expression

print('{0:.2f}'.format(1.2345))  # String method
print(format(1.2345, '.2f'))  # Built-in function
print('%.2f' % 1.2345)  # Expression

print('%s=%s' % ('spam', 42))  # Format expression: in all 2.X/3.X
print('{0}={1}'.format('spam', 42))  # Format method: in 3.0+ and 2.6+
print('{}={}'.format('spam', 42))  # With autonumbering: in 3.1 and 2.7

print('%s, %s and %s' % (3.14, 42, [1, 2]))  # Arbitrary types

print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform})

print('My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform))

somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
print('first=%s, last=%s, middle=%s' % parts)

# Adding specific formatting

print('%-10s = %10s' % ('spam', 123.4567))

print('%10s = %-10s' % ('spam', 123.4567))

print('%(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop'))

# Floating point numbers

print('%e, %.3e, %g' % (3.14159, 3.14159, 3.14159))

print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))

# Hex and octal, but not binary (see ahead)

print('%x, %o' % (255, 255))

# Hardcoded references in both

print('My {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'}))
print('My %(kind)-8s runs %(plat)8s' % dict(kind='laptop', plat=sys.platform))

# Building data ahead of time in both

data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
'''
**data unpacks a dictionary of keys and values into
individual "name=value" keyword arguments so they can be
referenced by name in format string
'''
print('My %(kind)-8s runs %(platform)8s' % data)

print('{0:d}'.format(999999999999))
print('{0:,d}'.format(999999999999))

print('{:,d}'.format(999999999999))
print('{:,d} {:,d}'.format(9999999, 8888888))
print('{:,.2f}'.format(296999.2567))

'''
# Not working because of module formats
from formats import commas, money
print('%s' % commas(999999999999))
print('%s %s' % (commas(9999999), commas(8888888)))
print('%s' % money(296999.2567))

[commas(x) for x in (9999999, 8888888)]
print('%s %s' % tuple(commas(x) for x in (9999999, 8888888)))
print(''.join(commas(x) for x in (9999999, 8888888)))
'''

print('{0:b}'.format((2 ** 16) - 1))  # Expression (only) binary format code
#print('%b' % ((2 ** 16) - 1))
print(bin((2 ** 16) - 1))  # But other more general options work too
print('%s' % bin((2 ** 16) - 1))  # Usable with both method and % expression
print('{}'.format(bin((2 ** 16) - 1)))  # With 2.7/3.1+ relative numbering
print('%s' % bin((2 ** 16) - 1)[2:])  # Slice off 0b to get exact equivalent

print('{:,d}'.format(999999999999))  # New str.format method feature in 3.1/2.7
'''
# Not working because of module formats
print('%s' % commas(999999999999)  # But % is same with simple 8-line function
'''

print('{name} {job} {name}'.format(name='Bob', job='dev'))
print('%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev'))

D = dict(name='Bob', job='dev')
print('{0[name]} {0[job]} {0[name]}'.format(D))  # Method, key references
print('{name} {job} {name}'.format(**D))  # Method, dict-to-args
print('%(name)s %(job)s %(name)s' % D)  # Expressions, key references



