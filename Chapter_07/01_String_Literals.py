print('shrubbery', "shrubbery")
print('knight"s', "knight's")

title = "Meaning " 'of' " Life"  # Implicit concatenation
print(title)

print('knight\'s', "knight\"s")

s = 'a\nb\tc'
print(s)

print(len(s))

s = 'a\0b\0c'
print(s)
print(len(s))

s = '\001\002\x03'
print(s)
print(len(s))

S = 's\tp\na\x00m'
print(S)
print(len(S))

x  = 'C:\py\code'  # Keeps \ literally (and displays it as \\)
print(x)
print(len(x))

#myfile = open(r'C:\new\text.dat', 'w')
#myfile = open(r'C:\\new\\text.dat', 'w')

path = r'C:\new\text.dat'
print(path)  # User friendly format
print(len(path))