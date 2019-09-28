import struct

packed = struct.pack('>i4sh', 7, b'spam', 8)  # Create packed binary data
print(packed)  # 10 bytes not objects or text
file = open('data.bin', 'wb')  # Open binary output file
file.write(packed)  # Write packed binary data
file.close()

data = open('data.bin', 'rb').read()
print(data)
print(data[4:8])  # Slice bytes in the middle
print(list(data))  # A sequence of 8-bit bytes
data2 = struct.unpack('>i4sh', data)  # Unpack in too object again
print(data2)