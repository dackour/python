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
