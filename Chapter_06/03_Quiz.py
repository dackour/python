A = 'spam'
print(A)
B = A
print(A, B)
B = 'shrubbery'
print(A, B)

A = ['spam']
print(A)
B = A
print(A, B)
B[0] = 'shrubbery'
print(A, B)

A = ['spam']
print(A)
B = A[:]
print(A, B)
B[0] = 'shrubbery'
print(A, B)
