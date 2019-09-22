S = 'Spam'
# Immutable objects cannot be changed
# S[0] = 'z'
#
# But we can run expressions to make new objects
S = 'z' + S[1:]
print(S)

S = 'shrubbery'
print(S)
L = list(S)                 # Expand to a list [...]
print(L)
L[1] = 'c'                  # change it in place
print(L)
print(''.join(L))           # join with empty delimiter

B = bytearray(b'spam')      # A byte/list hybrid (ahead)
B.extend(b'eggs')           # 'b' needed in 3.X not 2.X
print(B)                    # B[i] = ord(c) works here too
print(B.decode())           # Translate to normal string
