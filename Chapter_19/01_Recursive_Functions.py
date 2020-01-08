# Recursive Functions
# Summation with Recursion


def mysum(L):
    print(L)  # Trace recursive levels
    if not L: # L shorter at each level
        return 0
    else:
        return L[0] + mysum(L[1:])  # Call myself recursively


print(mysum([1, 2, 3, 4, 5]))

# Coding Alternatives


def mysum1(L):
    return 0 if not L else L[0] + mysum1(L[1:])  # USe ternary expression


def mysum2(L):
    return L[0] if len(L) == 1 else L[0] + mysum2(L[1:])  # Any type, assume one

def mysum3(L):
    first, *rest = L
    return first if not rest else first + mysum3(rest)  # Use 3.x ext seq assign

print(mysum1([1]))
print(mysum2([1]))
print(mysum3([1]))

print(mysum1([]))  #mysum fails in last 2
#print(mysum2([])) # Err
#print(mysum3([])) # Err

print(mysum1([1, 2, 3, 4, 5]))
print(mysum2([1, 2, 3, 4, 5]))
print(mysum3([1, 2, 3, 4, 5]))

print(mysum2(('s', 'p', 'a', 'm')))  # But various types now work
print(mysum2(['spam', 'ham', 'eggs']))
print(mysum3(('s', 'p', 'a', 'm')))


def mysum(L):
    if not L: return 0
    return nonempty(L)  # call a function that calls me


def nonempty(L):
    return L[0] + mysum(L[1:])  # Indirectly recursive

print(mysum([1.1, 2.2, 3.3, 4.4]))

# Loop Statements Versus Recursion


