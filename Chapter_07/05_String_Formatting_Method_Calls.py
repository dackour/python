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

print(oct(255), int('377', 8), 0o377)  # Other to/from octal, in 3.X
                                       # 2.X prints and accepts 0377

print('{0:.2f}'.format(1 / 3.0))  # Parameters hardcoded
print('%.2f' % (1 / 3.0))  # Ditto for expression

print('{0:.{1}f}'.format(1 / 3.0, 4))  # Take value from arguments
print('%.*f' % (4, 1 / 3.0))  # Ditto for expression

print('{0:.2f}'.format(1.2345))  # String method
print(format(1.2345, '.2f'))  # Built-in function
print('%.2f' % 1.2345)  # Expression
