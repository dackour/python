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

L = [1, 2, 3, 4, 5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]

print(sum)

L = [1, 2, 3, 4, 5]
sum = 0
for x in L: sum += x

print(sum)

# Handling Arbitrary Structures


def sumtree(L):
    tot = 0
    for x in L:  # for each item at this level
        if not isinstance(x, list):
            tot += x  # Add numbers directly
        else:
            tot += sumtree(x)  # Recur for sublists
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))
print(sumtree([1, [2, [3, [4, [5]]]]]))  # Prints 15 (right heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))  # Prints 15 (left heavy)

# Recursion versus queues and stacks


def sumtree(L):  # Breadth-first, explicit queue
    tot = 0
    items = list(L)  # Start with copy of top level
    while items:
        front = items.pop()  # Fetch/delete front item
        if not isinstance(front, list):
            tot += front  # add numbers directly
        else:
            items.extend(front)  # <== Append all in nested list
    return tot


print(sumtree(L))


def sumtree(L):  # Depth-first, explicit stack
    tot = 0
    items = list(L)  # Start with copy of to level
    while items:
        front = items.pop(0)  # Fetch/delete front item
        if not isinstance(front, list):
            tot += front  # Add numbers directly
        else:
            items[:0]  = front  # <== Prepend all in nested list
    return tot


print(sumtree([1, [2, [3, [4, [5]]]]]))

# Cycle, paths, and stack limits

import sys

print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)  # Allow deeper nesting
print(help(sys.setrecursionlimit))  # Read mor about it

# More recursion examples


