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

mantra = '''Always look
on the bright
side of life.
'''
print(mantra)

menu = """spam  # comments here added to string!
eggs  # ditto
"""
print(menu)

menu = (
"spam\n"  # comments here ignored
"eggs\n"  # but new lines not automatic
)
print(menu)

X = 1
'''
import os
print(os.getcwd())
'''
Y = 2