myfile = open('myfile.txt', 'w')  # Open for text output: create/empty
myfile.write('hello text file\n')  # Write a line of text: string
myfile.write('goodbye text file\n')
myfile.close()

myfile = open('myfile.txt')  # Open for text input: 'r' is default
print(myfile.readline())  # Read the lines back
print(myfile.readline())
print(myfile.readline())  # Empty string end-of-file

open('myfile.txt').read()  # Read all at once into string
print(open('myfile.txt').read())  # User friendly display

for line in open('myfile.txt'):  # Use file iterators, not reads
    print(line, end='')



#mybinfile = open('data.bin', 'wb')
#bytearray(newFileBytes)
#newFileBytes = bytearray(b'\x00\x00\x00\x07spam\x00\x08')
#bytes(newFileBytes)
#mybinfile.write(bytes(newFileBytes))
#data = open('data.bin', 'rb').read()  # open binary file rb = read binary
#print(data)  # bytes sting holds binary data
#print(data[4:8])  # Act like strings
#print(data[4:8][0])  # But really are small 8-bit integers

X, Y, Z = 43, 44, 45  # Native Python objects
S = 'Spam'  # Must be string to store in file
D = {'a': 1, 'b': 2}
L =[1, 2, 3]

F = open('datafile.txt', 'w')  # Create output text file
F.write(S + '\n')  # Terminate lines with \n
F.write('%s, %s, %s\n' % (X, Y, Z))  # Convert numbers to strings
F.write(str(L) + '$' + str(D) + '\n')  # Convert and separate with $
F.close()

chars = open('datafile.txt').read()  # Raw string display
chars
print(chars)  # User friendly display

F = open('datafile.txt')  # Open again
line = F.readline()  # Read one line
print(line)
print(line.rstrip())  # Remove end of line

line = F.readline()  # Next line from file
print(line)
parts = line.split(',')  # Split (parse) on commas
print(parts)

print(int(parts[1]))  # Convert from string to int
numbers = [int(P) for P in parts]  # Convert all in a list at once
print(numbers)

line = F.readline()
print(line)
parts = line.split('$')
print(parts)
print(eval(parts[0]))  # Convert to any object type
objects = [eval(P) for P in parts]  # Do same for all in list
print(objects)

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)  # Pickle any object to file
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)  # Load any object from file
print(E)

print(open('datafile.pkl', 'rb').read())  # Format is prone to change!
#help(pickle)