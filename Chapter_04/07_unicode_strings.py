print('sp\xc4m')        # 3.X normal str strings are Unicode text
print(b'a\x01c')        # bytes strings are byte-based data
print(u'sp\u00c4m')     # The 2.X Unicode literal works in 3.3+ just str
print(u'sp\xc4m')       # 2.X Unicode strings are a distinct type
print('a\x01c')         # Normal str strings contain byte-based text/data
print(b'a\x01c')        # The 3.X bytes literal works in 2.6+ just str

print('spam')                                                           # Characters may be 1,2 or 4 bytes in memory

print('spam'.encode('utf8'))                                            # Encoded to 4 bytes in UTF-8 in files

print('spam'.encode('utf16'))                                           # But encoded to 10 bytes in UTF-16

print('sp\xc4\u00c4\U000000c4m')

print('\u00A3', '\u00A3'.encode('latin1'), b'xA3'.decode('latin1'))

