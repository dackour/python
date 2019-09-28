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
print(text.encode('utf-8'))