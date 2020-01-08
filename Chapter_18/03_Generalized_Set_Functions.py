# Generalized Set Functions


def intersect(*args):
    res = []
    for x in args[0]:  # Scan first sequence
        if x in res: continue  # Skip duplicates
        for other in args[1:]:  # For all other args
            if x not in other:  # item in each one?
                break  # No break out of loop
            else:
                res.append(x)  # Yes: add items to end
    return res


print(intersect((1, 2, 2, 3), (3, 4, 5)))


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


print(union((1, 2, 3, 4, 5), (5, 6, 7, 8, 9)))

s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'

print(intersect(s1, s2), union(s1, s2))  # Two operands
print(intersect([1, 2, 3], (1, 4)))  # Mixed types
print(intersect(s1, s2, s3))  # Three operands
print(union(s1, s2, s3))


def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))


tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)