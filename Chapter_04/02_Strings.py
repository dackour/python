# Make a 4 character string, and assign it to a name
S = 'Spam'
# Lenght
print(len(S))
# The first item in S, indexing by zero-based position
print(S[0])
# The second item from the left
print(S[1])
# The last item from the end in S
print(S[-1])
# The second-to-last item from the end
print(S[-2])
# The last item in S
print(S[-1])
# Negative indexing, the hard way
print(S[len(S)-1])
# A 4-character string
print(S)
# Slice of S from offsets 1 through 2 (not 3)
print(S[1:3])
print(S[0:3])
# Everything past the first (1:len(S))
print(S[1:])
# Everything but the last
print(S[0:3])
# Same as S[0:3]
print(S[:3])
# Everything but the last again, but simpler (0:-1)
print(S[:-1])
# All of S as top-level copy  (0:len(S))
print(S[:])
# Concatenation
print(S + 'xyz')
# S is unchanged
print(S)
# Repetition
print(S * 8)
