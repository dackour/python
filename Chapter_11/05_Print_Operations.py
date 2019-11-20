# Print operations
print()  # Display a blank line
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z)  # print 3 objects per defaults

print(x, y, z, sep='')  # Suppress separator
print(x, y, z, sep=', ')  # Custom separator

print(x, y, z, end='')  # Suppress line break
print(x, y, z, end=''); print(x, y, z)  # 2 prints same output line
print(x, y, z, end='...\n')  # Custom line end

print(x, y, z, sep='...', end='!\n')  # Multiple keywords
print(x, y, z, end='!\n', sep='...')  # Order doesnt matter

print(x, y, z, sep='...', file=open('data.txt', 'w'))  # Print to a file
print(x, y, z)  # Back to stdout
print(open('data.txt').read())  # Display file text

text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)
print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))



