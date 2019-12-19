# A First Example: Definitions and Calls
# Definition


def times(x, y):  # Create and assign function
    return x * y  # Body executed when called


# Calls
times(2, 4)  # Arguments in parentheses

x = times(3.14, 4)  # Save the result object
print(x)

x = times('Ni', 4)  # Functions are "typeless"
print(x)

# Polymorphism in Python
# A Second Example Intersecting Sequences

def intersect(seq1, seq2):
    res = []  # Start empty
    for x in seq1:  # Scan seq1
        if x in seq2:  # Common item?
            res.append(x)  # Add to end
    return res


s1 = 'SPAM'
s2 = 'SCAM'
print(intersect(s1, s2))  # Strings

print([x for x in s1 if x in s2])

# Polymorphism revisited
x = intersect([1, 2, 3], (1, 4))  # Mixed types
print(x)  # Saved result object


