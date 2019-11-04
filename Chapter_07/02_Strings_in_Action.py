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

S = '5'
S = chr(ord(S) + 1)
print(S)
S = chr(ord(S) + 1)
print(S)

print(int('5'))
print(ord('5') - ord('0'))

B = '1101'  # Convert binary digits to integer with ord
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I)

print(int('1101', 2))  # Convert binary to integer built-int
print(bin(13))  # Convert integer to binary: built-in

S = 'spam'
# S[0] = 'x'  # Raises an error!

S = S + 'SPAM!'  # To change string make a new one
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)

