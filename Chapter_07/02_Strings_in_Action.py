print(len('abc'))  # Length number of items
print('abc' + 'def')  # Concatenation a new string
print('Ni!' * 7)  # Repetition like 'Ni!' + 'Ni!' + ...

print('------...more...---')  # 80 dashes the hard way
print('-' * 80)  # 80 dashes the easy way

myjob = 'hacker'
for c in myjob: print(c, end=' ')  # Step through items. print each (3.x form)
print('\n')
print('k' in myjob)  # Found
print('z' in myjob)  # Not found
print('spam' in 'abcspamdef')  # Substring search, no position returned

S = 'spam'
print(S[0], S[-2])  # Indexing from front or end -2 (4+(-2))
print(S[1:3], S[1:], S[:-1])  # Slicing extract section

S = 'abcdefghijklmnop'
print(S[1:10:2])  # Skipping items
print(S[::2])
print('hello'[::-1])  # Reversing items

S = 'abcedfg'
print(S[5:1:-1])  # bounds roles differ

print('spam'[1:3])  # Slicing syntax
print('spam'[slice(1, 3)])  # Slice objects with index syntax + object
print('spam'[::-1])
print('spam'[slice(None, None, -1)])

print(int('42'), str(42))  # Convert from/to string
print(repr(42))  # Convert to as-code string

S = '42'
I = 1
print(int(S) + I)  # Force addition
print(S + str(I))  # Force concatenation

print(str(3.1415), float('1.5'))
text = '1.234E-10'
print(float(text))  # Shows more digits before 2.7 and 3.1

print(ord('s'))
print(chr(115))
