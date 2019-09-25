S = 'A\nB\tC'       # \n is the end of line, \t is a tab
print(S)
print(len(S))       # each stands for just one character

print(ord('\n'))    # \n is a byte with the binary value of 10 in ASCII

S = 'A\0B\0C'       # \0 a binary zero byte, does not terminate string
print(S)
print(len(S))


S = 'A\x00B\x00C'   #Non-printables are displayed as \xNN hex escapes
print(S)

