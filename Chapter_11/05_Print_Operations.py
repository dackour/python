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

print('hello world')  # Print a string object in 3.x

import sys  # Printing the hard way
sys.stdout.write('hello world\n')

X, Y = ['spam', 'eggs']

print(X, Y)
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')

#sys.stdout = open('log.txt', 'a')  # Redirects prints to a file
print(x, y, x)  # Shows up in log.txt

temp = sys.stdout  # save for restoring later
sys.stdout = open('log.txt', 'a')  # Redirects prints to a file
print('spam')  # prints go to file not here
print(1, 2, 3)
sys.stdout.close()  # Flush output to disk
sys.stdout = temp  # Restore original stream
print('back here')  # Prints show up here again
print(open('log.txt').read())  # Result of earlier prints

log = open('log.txt', 'a')  # 3.x
print(x, y, z, file=log)  # Print to file like object
print(x, y, z)  # print to original stdout

#log = open('log.txt', 'a')  # 2.x
#print >> log, x, y, z
#print x y z

log = open('log.txt', 'a')
print(1, 2, 3, file=log)
print(4, 5, 6, file=log)
log.close()
print(7, 8, 9)

sys.stderr.write(('Bad!' * 8) + '\n')
print('Bad!' * 8, file=sys.stderr)
print(sys.stderr)

X = 1
Y = 2
print(X, Y)  # Print the easy way
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')  # Print the hard way

print(X, Y, file=open('temp1.txt', 'w'))  # Redirect text to file

open('temp2.txt', 'w').write(str(X) + ' ' + str(Y) + '\n')  # Send to a file manually

print(open('temp1.txt', 'rb').read())  # Binary mode for bytes
print(open('temp2.txt', 'rb').read())

print('spam')  # 3.x print function call syntax
print('spam', 'ham', 'eggs')  # This are multiple arguments

# Python27
#print('spam')  # 2.x statement, enclosing parens
#print('spam', 'ham', 'eggs')  # This is really a tuple object in 2.7

print()  # This is just a line feed on 3.0

print('%s %s %s' % ('spam', 'ham', 'eggs'))
print('{0} {1} {2}'.format('spam', 'ham', 'eggs'))
print('answer: ' + str(42))