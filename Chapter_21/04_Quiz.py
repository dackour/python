# 1. What conclusions can you draw from this chapter about the relative speed of
# Python iteration tools?
#
# In general, list comprehensions are usually the quickest of the bunch; map beats list
# comprehensions in Python only when all tools must call functions; for loops tend
# to be slower than comprehensions; and generator functions and expressions are
# slower than comprehensions by a constant factor. Under PyPy, some of these findings
# differ; map often turns in a different relative performance, for example, and list
# comprehensions seem always quickest, perhaps due to function-level optimizations.
# At least that’s the case today on the Python versions tested, on the test machine
# used, and for the type of code timed—these results may vary if any of these three
# variables differ. Use the homegrown timer or standard library timeit to test your
# use cases for more relevant results. Also keep in mind that iteration is just one
# component of a program’s time: more code gives a more complete picture.
#
# 2. What conclusions can you draw from this chapter about the relative speed of the
# Pythons timed?
#
# In general, PyPy 1.9 (implementing Python 2.7) is typically faster than CPython
# 2.7, and CPython 2.7 is often faster than CPython 3.3. In most cases timed, PyPy
# is some 10X faster than CPython, and CPython 2.7 is often a small constant faster
# than CPython 3.3. In cases that use integer math, CPython 2.7 can be 10X faster
# than CPython 3.3, and PyPy can be 100X faster than 3.3. In other cases (e.g., string
# operations and file iterators), PyPy can be slower than CPython by 10X, though
# timeit and memory management differences may influence some results. The
# pystone benchmark confirms these relative rankings, though the sizes of the differences
# it reports differ due to the code timed.
# At least that’s the case today on the Python versions tested, on the test machine
# used, and for the type of code timed—these results may vary if any of these three
# variables differ. Use the homegrown timer or standard library timeit to test your
# use cases for more relevant results. This is especially true when timing Python
# implementations, which may be arbitrarily optimized in each new release.