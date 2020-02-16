# In these exercises, you’re going to start coding more sophisticated programs. Be sure
# to check the solutions in Part IV in Appendix D, and be sure to start writing your code
# in module files. You won’t want to retype these exercises if you make a mistake.

# 1. The basics. At the Python interactive prompt, write a function that prints its single
# argument to the screen and call it interactively, passing a variety of object types:
# string, integer, list, dictionary. Then, try calling it without passing any argument.
# What happens? What happens when you pass two arguments?

# The basics. There’s not much to this one, but notice that using print (and hence
# your function) is technically a polymorphic operation, which does the right thing
# for each type of object:


def func(x):
    print(x)

func('spam')
func(42)
func([1, 2, 3])
func({'food': 'spam'})
#func() # TypeError: single() missing 1 required positional argument: 'x'
#func('a', 'b') # TypeError: single() takes 1 positional argument but 2 were given

# 2. Arguments. Write a function called adder in a Python module file. The function
# should accept two arguments and return the sum (or concatenation) of the two.
# Then, add code at the bottom of the file to call the adder function with a variety of
# object types (two strings, two lists, two floating points), and run this file as a script
# from the system command line. Do you have to print the call statement results to
# see results on your screen?

# Arguments. Here’s a sample solution. Remember that you have to use print to see
# results in the test calls because a file isn’t the same as code typed interactively;
# Python doesn’t normally echo the results of expression statements in files:


def adder(x, y):
    return x + y


print(adder(2, 3))
print(adder('spam', 'eggs'))
print(adder(['a', 'b'], ['c', 'd']))

# 3. varargs. Generalize the adder function you wrote in the last exercise to compute
# the sum of an arbitrary number of arguments, and change the calls to pass more
# or fewer than two arguments. What type is the return value sum? (Hints: a slice
# such as S[:0] returns an empty sequence of the same type as S, and the type builtin
# function can test types; but see the manually coded min examples in Chapter
# 18 for a simpler approach.) What happens if you pass in arguments of different
# types? What about passing in dictionaries?

# varargs. Two alternative adder functions are shown in the following file, adders.py.
# The hard part here is figuring out how to initialize an accumulator to an
# empty value of whatever type is passed in. The first solution uses manual type
# testing to look for an integer, and an empty slice of the first argument (assumed to
# be a sequence) if the argument is determined not to be an integer. The second
# solution uses the first argument to initialize and scan items 2 and beyond, much
# like one of the min function variants shown in Chapter 18.

# The second solution is better. Both of these assume all arguments are of the same
# type, and neither works on dictionaries (as we saw in Part II, + doesn’t work on
# mixed types or dictionaries). You could add a type test and special code to allow
# dictionaries, too, but that’s extra credit.


def adder1(*args):
    print('adder1', end=' ')
    if type(args[0]) == type(0):  # Integer?
        sum = 0  # Init to zero
    else:  # else sequence:
        sum = args[0][:0]  # Use empty slice of arg1
    for arg in args:
        sum = sum + arg
    return sum


def adder2(*args):
    print('adder2', end=' ')
    sum = args[0]  # Init to arg1
    for next in args[1:]:
        sum += next  # Add items 2..N
    return sum


for func in (adder1, adder2):
    print(func(2, 3, 4))
    print(func('spam', 'eggs', 'toast'))
    print(func(['a', 'b'], ['c', 'd'], ['e', 'f']))

# 4. Keywords. Change the adder function from exercise 2 to accept and sum/concatenate
# three arguments: def adder(good, bad, ugly). Now, provide default values
# for each argument, and experiment with calling the function interactively. Try
# passing one, two, three, and four arguments. Then, try passing keyword arguments.
# Does the call adder(ugly=1, good=2) work? Why? Finally, generalize the
# new adder to accept and sum/concatenate an arbitrary number of keyword arguments.
# This is similar to what you did in exercise 3, but you’ll need to iterate over
# a dictionary, not a tuple. (Hint: the dict.keys method returns a list you can step
# through with a for or while, but be sure to wrap it in a list call to index it in 3.X;
# dict.values may help here too.)

# Keywords. Here is my solution to the first and second parts of this exercise (coded
# in the file mod.py). To iterate over keyword arguments, use the **args form in the
# function header and use a loop (e.g., for x in args.keys(): use args[x]), or use
# args.values() to make this the same as summing *args positionals:


def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly


print(adder())
print(adder(5))
print(adder(5, 6))
print(adder(5, 6, 7))
print(adder(ugly=7, good=6, bad=5))

# Second part solutions


def adder1(*args): # Sum any number of positional args
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot


def adder2(**args): # Sum any number of keyword args
    argskeys = list(args.keys()) # list needed in 3.X!
    tot = args[argskeys[0]]
    for key in argskeys[1:]:
        tot += args[key]
    return tot


def adder3(**args): # Same, but convert to list of values
    args = list(args.values()) # list needed to index in 3.X!
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot


def adder4(**args): # Same, but reuse positional version
    return adder1(*args.values())


print(adder1(1, 2, 3), adder1('aa', 'bb', 'cc'))
print(adder2(a=1, b=2, c=3), adder2(a='aa', b='bb', c='cc'))
print(adder3(a=1, b=2, c=3), adder3(a='aa', b='bb', c='cc'))
print(adder4(a=1, b=2, c=3), adder4(a='aa', b='bb', c='cc'))

# 5. Dictionary tools. Write a function called copyDict(dict) that copies its dictionary
# argument. It should return a new dictionary containing all the items in its argument.
# Use the dictionary keys method to iterate (or, in Python 2.2 and later, step
# over a dictionary’s keys without calling keys). Copying sequences is easy (X[:]
# makes a top-level copy); does this work for dictionaries, too? As explained in this
# exercise’s solution, because dictionaries now come with similar tools, this and the
# next exercise are just coding exercises but still serve as representative function
# examples.

# 6. Dictionary tools. Write a function called addDict(dict1, dict2) that computes the
# union of two dictionaries. It should return a new dictionary containing all the items
# in both its arguments (which are assumed to be dictionaries). If the same key appears
# in both arguments, feel free to pick a value from either. Test your function
# by writing it in a file and running the file as a script. What happens if you pass lists
# instead of dictionaries? How could you generalize your function to handle this case,
# too? (Hint: see the type built-in function used earlier.) Does the order of the arguments
# passed in matter?

# Dictionary tools. Here are my solutions to exercises 5 and 6 (file dicts.py).
# These are just coding exercises, though, because Python 1.5 added the dictionary
# methods D.copy() and D1.update(D2) to handle things like copying and adding
# (merging) dictionaries. See Chapter 8 for dict.update examples, and Python’s library manual
# or O’Reilly’s Python Pocket Reference for more details. X[:] doesn’t
# work for dictionaries, as they’re not sequences (see Chapter 8 for details). Also,
# remember that if you assign (e = d) rather than copying, you generate a reference
# to a shared dictionary object; changing d changes e, too:

def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new


def addDict(d1, d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
        for key in d2.keys():
            new[key] = d2[key]
    return new


# 7. More argument-matching examples. First, define the following six functions (either
# interactively or in a module file that can be imported):
# def f1(a, b): print(a, b) # Normal args
# def f2(a, *b): print(a, b) # Positional varargs
# def f3(a, **b): print(a, b) # Keyword varargs
# def f4(a, *b, **c): print(a, b, c) # Mixed modes
# def f5(a, b=2, c=3): print(a, b, c) # Defaults
# def f6(a, b=2, *c): print(a, b, c) # Defaults and positional varargs
# Now, test the following calls interactively, and try to explain each result; in some
# cases, you’ll probably need to fall back on the matching algorithm shown in Chapter
# 18. Do you think mixing matching modes is a good idea in general? Can you
# think of cases where it would be useful?

# More argument-matching examples. Here is the sort of interaction you should get,
# along with comments that explain the matching that goes on:


def f1(a, b): print(a, b) # Normal args


def f2(a, *b): print(a, b) # Positional varargs


def f3(a, **b): print(a, b) # Keyword varargs


def f4(a, *b, **c): print(a, b, c) # Mixed modes


def f5(a, b=2, c=3): print(a, b, c) # Defaults


def f6(a, b=2, *c): print(a, b, c) # Defaults and positional varargs


# 8. Primes revisited. Recall the following code snippet from Chapter 13, which simplistically
# determines whether a positive integer is prime:
# x = y // 2 # For some y > 1
# while x > 1:
#     if y % x == 0: # Remainder
#         print(y, 'has factor', x)
#         break # Skip else
#     x -= 1
# else: # Normal exit
#     print(y, 'is prime')
# Package this code as a reusable function in a module file (y should be a passed-in
# argument), and add some calls to the function at the bottom of your file. While
# you’re at it, experiment with replacing the first line’s // operator with / to see how
# true division changes the / operator in Python 3.X and breaks this code (refer back
# to Chapter 5 if you need a reminder). What can you do about negatives, and the
# values 0 and 1? How about speeding this up? Your outputs should look something
# like this:
# 13 is prime
# 13.0 is prime
# 15 has factor 5
# 15.0 has factor 5.0

# Primes revisited. Here is the primes example, wrapped up in a function and a module
# (file primes.py) so it can be run multiple times. I added an if test to trap
# negatives, 0, and 1. I also changed / to // in this edition to make this solution immune
# to the Python 3.X / true division changes we studied in Chapter 5, and to enable
# it to support floating-point numbers (uncomment the from statement and
# change // to / to see the differences in 2.X):

#from __future__ import division


def prime(y):
    if y <= 1: # For some y > 1
        print(y, 'not prime')
    else:
        x = y // 2 # 3.X / fails
        while x > 1:
            if y % x == 0: # No remainder?
                print(y, 'has factor', x)
                break # Skip else
            x -= 1
        else:
            print(y, 'is prime')


prime(13); prime(13.0)
prime(15); prime(15.0)
prime(3); prime(2)
prime(1); prime(-3)

# Here is the module in action; the // operator allows it to work for floating-point
# numbers too, even though it perhaps should not:

# This function still isn’t very reusable—it could return values, instead of printing
# —but it’s enough to run experiments. It’s also not a strict mathematical prime
# (floating points work), and it’s still inefficient. Improvements are left as exercises
# for more mathematically minded readers. (Hint: a for loop over range(y, 1, −1)
# may be a bit quicker than the while, but the algorithm is the real bottleneck here.)
# To time alternatives, use the homegrown timer or standard library timeit modules
# and coding patterns like those used in Chapter 21’s timing sections (and see Solution 10).

# 9. Iterations and comprehensions. Write code to build a new list containing the square
# roots of all the numbers in this list: [2, 4, 9, 16, 25]. Code this as a for loop first,
# then as a map call, then as a list comprehension, and finally as a generator expression.
# Use the sqrt function in the built-in math module to do the calculation (i.e.,
# import math and say math.sqrt(x)). Of the four, which approach do you like best?

# Iterations and comprehensions. Here is the sort of code you should write; I may
# have a preference, but yours may vary:

values = [2, 4, 9, 16, 25]
import math
res = []
for x in values: res.append(math.sqrt(x))

print(res)
print(list(map(math.sqrt, values)))
print([math.sqrt(x) for x in values])
print(list(math.sqrt(x) for x in values))

# 10. Timing tools. In Chapter 5, we saw three ways to compute square roots:
# math.sqrt(X), X ** .5, and pow(X, .5). If your programs run a lot of these, their
# relative performance might become important. To see which is quickest, repurpose
# the timerseqs.py script we wrote in this chapter to time each of these three tools.
# Use the bestof or bestoftotal functions in one of this chapter’s timer modules to
# test (you can use either the original, the 3.X-only keyword-only variant, or the 2.X/
# 3.X version, and may use Python’s timeit module as well). You might also want
# to repackage the testing code in this script for better reusability—by passing a test
# functions tuple to a general tester function, for example (for this exercise a copyand-
# modify approach is fine). Which of the three square root tools seems to run
# fastest on your machine and Python in general? Finally, how might you go about
# interactively timing the speed of dictionary comprehensions versus for loops?

# Timing tools. Here is some code I wrote to time the three square root options, along
# with the results in CPythons 3.3 and 2.7 and PyPy 1.9 (which implements Python
# 2.7). Each test takes the best of three runs; each run takes the total time required
# to call the test function 1,000 times; and each test function iterates 1,000 times.
# The last result of each function is printed to verify that all three do the same work:

# File timesqrt.py
import sys, timer2
reps = 10000
repslist = range(reps) # Pull out range list time for 2.X
from math import sqrt # Not math.sqrt: adds attr fetch time


def mathMod():
    for i in repslist:
        res = sqrt(i)
    return res


def powCall():
    for i in repslist:
        res = pow(i, .5)
    return res


def powExpr():
    for i in repslist:
        res = i ** .5
    return res


print(sys.version)
for test in (mathMod, powCall, powExpr):
    elapsed, result = timer2.bestoftotal(test, _reps1=3, _reps=1000)
    print ('%s: %.5f => %s' % (test.__name__, elapsed, result))

# Following are the test results for the three Pythons. The 3.3 and 2.7 results are
# roughly twice as fast as 3.0 and 2.6 in the prior edition, due largely to a faster test
# machine. For each Python tested, it looks like the math module is quicker than the
# ** expression, which is quicker than the pow call; however, you should try this with
# your code and on your own machine and version of Python. Also, note that Python
# 3.3 is essentially twice as slow as 2.7 on this test, and PyPy is a rough order of
# magnitude (10X) faster than both CPythons, despite the fact that this is running
# floating-point math and iterations. Later versions of any of these Pythons might
# differ, so time this in the future to see for yourself:

# c:\code> py −3 timesqrt.py
# 3.3.0 (v3.3.0:bd8afb90ebf2, Sep 29 2012, 10:57:17) [MSC v.1600 64 bit (AMD64)]
# mathMod: 2.04481 => 99.99499987499375
# powCall: 3.40973 => 99.99499987499375
# powExpr: 2.56458 => 99.99499987499375
# c:\code> py −2 timesqrt.py
# 2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)]
# mathMod: 1.04337 => 99.994999875
# powCall: 2.57516 => 99.994999875
# powExpr: 1.89560 => 99.994999875
# c:\code> c:\pypy\pypy-1.9\pypy timesqrt.py
# 2.7.2 (341e1e3821ff, Jun 07 2012, 15:43:00)
# [PyPy 1.9.0 with MSC v.1500 32 bit]
# mathMod: 0.07491 => 99.994999875
# powCall: 0.85678 => 99.994999875
# powExpr: 0.85453 => 99.994999875


# To time the relative speeds of Python 3.X and 2.7 dictionary comprehensions and
# equivalent for loops interactively, you can run a session like the following.
# It appears that the two are roughly the same in this regard under Python 3.3; unlike list
# comprehensions, though, manual loops are slightly faster than dictionary comprehensions today
# (though the difference isn’t exactly earth-shattering—at the end
# we save half a second when making 50 dictionaries of 1,000,000 items each). Again,
# rather than taking these results as gospel you should investigate further on your
# own, on your computer and with your Python:

# C:\code> c:\python33\python
# >>>
# >>> def dictcomp(I):
#         return {i: i for i in range(I)}
# >>> def dictloop(I):
#         new = {}
#         for i in range(I): new[i] = i
#         return new
# >>> dictcomp(10)
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
# >>> dictloop(10)
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
# >>>
# >>> from timer2 import total, bestof
# >>> bestof(dictcomp, 10000)[0] # 10,000-item dict
# 0.0017095345403959072
# >>> bestof(dictloop, 10000)[0]
# 0.002097576400046819
# >>>
# >>> bestof(dictcomp, 100000)[0] # 100,000-items: 10X slower
# 0.012716923463358398
# >>> bestof(dictloop, 100000)[0]
# 0.014129806355413166
# >>>
# >>> bestof(dictcomp, 1000000)[0] # 1 of 1M-items: 10X time
# 0.11614425187337929
# >>> bestof(dictloop, 1000000)[0]
# 0.1331144855439561
# >>>
# >>> total(dictcomp, 1000000, _reps=50)[0] # Total to make 50 1M-item dicts
# 5.8162020671780965
# >>> total(dictloop, 1000000, _reps=50)[0]
# 6.626680761285343

# 11. Recursive functions. Write a simple recursion function named countdown that prints
# numbers as it counts down to zero. For example, a call countdown(5) will print: 5
# 4 3 2 1 stop. There’s no obvious reason to code this with an explicit stack or
# queue, but what about a nonfunction approach? Would a generator make sense
# here?

# Recursive functions. I coded this function as follows; a simple range, comprehension,
# or map will do the job here as well, but recursion is useful enough to experiment
# with here (print is a function in 3.X only, unless you import it from __future__ or
# code your own equivalent):


def countdown(N):
    if N == 0:
        print('stop') # 2.X: print 'stop'
    else:
        print(N, end=' ') # 2.X: print N,
        countdown(N-1)


# >>> countdown(5)
# 5 4 3 2 1 stop
# >>> countdown(20)
# 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 stop
# # Nonrecursive options:
# >>> list(range(5, 0, −1))
# [5, 4, 3, 2, 1]
# # On 3.X only:
# >>> t = [print(i, end=' ') for i in range(5, 0, −1)]
# 5 4 3 2 1
# >>> t = list(map(lambda x: print(x, end=' '), range(5, 0, −1)))
# 5 4 3 2 1

# I didn’t include a generator-based solution in this exercise on the grounds of merit
# (and humanity!), but one is listed below; all the other techniques seem much simpler
# in this case—a good example of cases where generators should probably be
# avoided. Remember that generators produce no results until iterated, so we need
# a for or yield from here (yield from works in 3.3 and later only):


def countdown2(N): # Generator function, recursive
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdown2(N-1): yield x # 3.3+: yield from countdown2(N-1)


# >>> list(countdown2(5))
# [5, 4, 3, 2, 1, 'stop']
# # Nonrecursive options:
# >>> def countdown3(): # Generator function, simpler
#  yield from range(5, 0, −1) # Pre 3.3: for x in range(): yield x
# >>> list(countdown3())
# [5, 4, 3, 2, 1]
# >>> list(x for x in range(5, 0, −1)) # Equivalent generator expression
# [5, 4, 3, 2, 1]
# >>> list(range(5, 0, −1)) # Equivalent nongenerator form
# [5, 4, 3, 2, 1]

# 12. Computing factorials. Finally, a computer science classic (but demonstrative nonetheless).
# We employed the notion of factorials in Chapter 20’s coverage of permutations:
# N!, computed as N*(N-1)*(N-2)*...1. For instance, 6! is 6*5*4*3*2*1, or
# 720. Code and time four functions that, for a call fact(N), each return N!. Code
# these four functions (1) as a recursive countdown per Chapter 19; (2) using the
# functional reduce call per Chapter 19; (3) with a simple iterative counter loop per
# Chapter 13; and (4) using the math.factorial library tool per Chapter 20. Use
# Chapter 21’s timeit to time each of your functions. What conclusions can you
# draw from your results?

# Computing factorials. The following file shows how I coded this exercise; it runs
# on Python 3.X and 2.X, and its output on 3.3 is given in a string literal at the end
# of the file. Naturally, there are many possible variations on its code; its ranges, for
# instance, could run from 2..N + 1 to skip an iteration, and fact2 could use
# reduce(operator.mul, range(N, 1, −1)) to avoid a lambda

#!python
from __future__ import print_function # File factorials.py
from functools import reduce
from timeit import repeat
import math


def fact0(N): # Recursive
    if N == 1: # Fails at 999 by default
        return N
    else:
        return N * fact0(N-1)


def fact1(N):
    return N if N == 1 else N * fact1(N-1) # Recursive, one-liner


def fact2(N): # Functional
    return reduce(lambda x, y: x * y, range(1, N+1))


def fact3(N):
    res = 1
    for i in range(1, N+1): res *= i # Iterative
        return res

def fact4(N):
    return math.factorial(N) # Stdlib "batteries"

# Tests
print(fact0(6), fact1(6), fact2(6), fact3(6), fact4(6)) # 6*5*4*3*2*1: all 720
print(fact0(500) == fact1(500) == fact2(500) == fact3(500) == fact4(500)) # True
for test in (fact0, fact1, fact2, fact3, fact4):
 print(test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3)))
r"""
C:\code> py −3 factorials.py
720 720 720 720 720
True
fact0 0.003990868798355564
fact1 0.003901433457907475
fact2 0.002732909419593966
fact3 0.002052614370939676
fact4 0.0003401475243271501
"""

# Conclusions: recursion is slowest on my Python and machine, and fails once N
# reaches 999 due to the default stack size setting in sys; per Chapter 19, this limit
# can be increased, but simple loops or the standard library tool seem the best route
# here in any event.

# This general finding holds true often. For instance, ''.join(reversed(S)) may be
# the preferred way to reverse a string, even though recursive solutions are possible.
# Time the following to see how: as for factorials in 3.X, recursion is today an order
# of magnitude slower in CPython, though these results vary in PyPy:


def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1]) # Recursive: 10x slower in CPython today


def rev2(S):
    return ''.join(reversed(S)) # Nonrecursive iterable: simpler, faster


def rev3(S):
    return S[::-1] # Even better?: sequence reversal by slice
