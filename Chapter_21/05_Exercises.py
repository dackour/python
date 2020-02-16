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

