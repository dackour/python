S = 'sp\xc4m'  # Non-ASCII Unicode text
print(S)
print(S[2])  # Sequence of characters

file = open('unidata.txt', 'w', encoding='utf-8')  # Write/encode UTF-8 text
file.write(S)  # 4 Characters written
file.close()

text = open('unidata.txt', encoding='utf8').read()  # Read/decode UTF-8 text
print(text)
print(len(text))  # 4 characters (code points)

raw = open('unidata.txt', 'rb').read()  # Read raw encoded bytes
print(raw)
print(len(raw))  # Really 5 bytes in UTF-8
print(text.encode('utf-8'))  # Manual encode to bytes
print(raw.decode('utf-8'))  # Manual decode to str

print(text.encode('latin-1'))  # Bytes differ in others
print(text.encode('utf-16'))

print(len(text.encode('latin-1')), len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))  # But same string decoded

import codecs
print(codecs.open('unidata.txt', encoding='utf-8').read())  # 2.X read/decode text
print(open('unidata.txt', 'rb').read())  # 2.X read raw bytes
open('unidata.txt').read()  # 2.X raw/undecoded too