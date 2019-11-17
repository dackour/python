# Interactive Loops
'''
while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(reply.upper())

while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    print(int(reply) ** 2)
print('Bye')

S = '123'
T = 'xxx'
S.isdigit(), T.isdigit()

while True:
    reply = input('Enter text: ')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')


while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye')


while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    try:
        print(int(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')
'''

while True:
    reply = input('Enter text: ')
    if reply == 'stop': break
    try:
        print(float(reply) ** 2)
    except:
        print('Bad!' * 8)
print('Bye')