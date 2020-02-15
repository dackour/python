# Timing Iterations and Pythons with timeit
# Basic timeit Usage
# Interactive Usage and API calls
import timeit

T = min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5))
print(T)

# Command-line usage
# timeit.py -n 1000 "[x ** 2 for x in range(1000)]"
# pythom -m timeit -n 1000 "[x ** 2 for x in range(1000)]"
# py -3 -m timeit -n 1000 -r 5 "[x ** 2 for x in range(1000)]"

# Timing multiline statements

T = min(timeit.repeat(stmt="L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1", number=10000, repeat=3))
print(T)

T = min(timeit.repeat(stmt="L = [1, 2, 3, 4, 5]\ni = 0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1", number=10000, repeat=3))
print(T)

T = min(timeit.repeat(stmt="L = [1, 2, 3, 4, 5]\nM = [x + 1 for x in L]", number=10000, repeat=3))
print(T)

# py -3 -m timeit -n 1000 -r 3 "L = [1, 2, 3, 4, 5]" "i=0" "while i < len(L):" "    L[i] += 1" "    i += 1"

# py -3 -m timeit -n 1000 -r 3 "L = [1, 2, 3, 4, 5]" "M = [x + 1 for x in L]"

# Other usage modes: Setup, totals, and objects

# python -m timeit -n 1000 -r 3 -s "L = [1, 2, 3, 4, 5]" "M = [x + 1 for x in L]"

from timeit import repeat

#min(repeat(number=1000, repeat=3, setup='from mins import min1, min2, min3\n' 'vals=list(range(1000))', stmt='min3(*vals)'))

print(timeit.timeit(stmt='[x ** 2 for x in range(1000)]', number=1000))  # Total time

print(timeit.Timer(stmt='[x ** 2 for x in range(1000)]').timeit(1000))  # Class API

print(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=3))


def testcase():
    y = [x ** 2 for x in range(1000)]  # callable objects or code strings


print(min(timeit.repeat(stmt=testcase, number=1000, repeat=3)))

# Benchmark Module and Script: timeit
