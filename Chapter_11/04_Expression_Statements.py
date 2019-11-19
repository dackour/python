# Expression Statements
x = print('spam')  # Print is a function call expression in 3.X
print(x)  # But it is coded as an expression statement

L = [1, 2]
L.append(3)  # Append is an in-place change
print(L)

# Don't do this:
L = L.append(4)  # But append returns None, not L
print(L)  # So we lose our list