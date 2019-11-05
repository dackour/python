template = '{0}, {1} and {2}'  # By position
print(template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}'  # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'  # By both
print(template.format('ham', motto='spam', food='eggs'))

template = '{}, {} and {}'  # By relative position
print(template.format('spam', 'ham', 'eggs'))  # New in 3.1 and 2.7
