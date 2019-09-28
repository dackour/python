f = open('data.txt', 'w')  # Make a new file in output mode ('w' is write)
f.write('Hello\n')  # Write string of characters to it
f.write('world\n')
f.close()  # Close to flush output buffers to disk

f = open('data.txt')  # 'r' (read) is default processing mode
text = f.read()  # Read entire file into string
print(text)  # print interprets control characters

print(text.split())  # File content is always a string

for line in open('data.txt'): print(line)

dir(f)

help(f.seek)
