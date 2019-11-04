S = 'spam'
result = S.find('pa')  # Call the find method to look for 'pa' in string S

S = 'spammy'
S = S[:3] + 'xx' + S[5:]  # Slice sections from S
print(S)

S = 'spammy'
S = S.replace('mm', 'xx')  # Replace all mm with xx in S
print(S)

X = 'aa$bb$cc$dd'.replace('$', 'SPAM')
print(X)

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print(where)
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))  # Replace all
print(S.replace('SPAM', 'EGGS', 1))  # Replace one

S = 'spammy'
L = list(S)
print(L)
L[3] = 'x'  # Works for lists, not strings
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)

print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)

line = 'aaa bbb  ccc'
cols = line.split()
print(cols)

line = 'bob,hacker,40'
print(line.split(','))

line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM'))

line = 'The knights who say Ni!\n'
print(line)
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))

print(line)
print(line.find('Ni') != -1)  # Search via method call or expression
print('Ni' in line)

sub = 'Ni!\n'
print(line.endswith(sub))  # End test via method call or slice
print(line[-len(sub):] == sub)

print(help(S.endswith))

S = 'a+b+c+'
x = S.replace('+', 'spam')
print(x)

# import string
# y = string.replace(S, '+', 'spam')
# print(y)
