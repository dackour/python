import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)  # Create packed binary data
print(packed)  # 10 bytes not objects or text
file = open('data.bin', 'wb')  # Open binary output file
file.write(packed)  # Write packed binary data
file.close()