import os
F = os.popen('dir') # Read line by line
print(F.readline())
F = os.popen('dir')  # Read by sized blocks
print(F.read(50))

print(os.popen('dir').readlines()[0])  # Read all lines: index
print(os.popen('dir').read()[:50])  # Read all at once: slice

for line in os.popen('dir'):  # File line iterator loop
    print(line.rstrip())

print(os.system('systeminfo'))

for line in os.popen('systeminfo'): print(line.rstrip())

# Formatted, limited display
for (i, line) in enumerate(os.popen('dir')):
    if i == 4: break
    print('%05d) %s' % (i, line.rstrip()))

# Parse for specific lines, case neutral
for line in os.popen('systeminfo'):
    parts = line.split(':')
    if parts and parts[0].lower() == 'system type':
        print(parts[1].strip())

# awk emulation extract column 7 from whitespace-delimited file
'''
for val in [line.split()[6] for line in open('input.txt')]:
    print(val)
'''
# Same but more explicit code that retains result
'''
col7 = []
for line in open('input.txt'):
    cols = line.split()
    col7.append(cols[6])
for item in col7: print(item)
'''
# Same but a reausable  function (see the next part of the book)
'''
def awker(file, col):
    return [line.rstrip().split()[col-1] for line in open(file)]

print(awker('input.txt', 7))  # List of strings
print(','.join(awker('input.txt', 7)))  # Put commas between
'''

from urllib.request import urlopen
for line in urlopen('http://home.rmi.net/~lutz'):
    print(line)