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
print('first={0}, last={1}, middle={2}'.format(*parts))
print('first={}, last={}, middle={}'.format(*parts))  # Or '{}' in 2.7/3.1
