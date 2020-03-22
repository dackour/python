# The import statement

import module1  # Get module as a whole (one or more)
module1.printer('Hello world!')  # Qualify to get names

# The from Statement

from module1 import printer  # Copy out a variable (one or more)
printer('Hello world!')  # No need to qualify name

# The from * Statement

from module1 import *  # Copy out _all_variables
printer('Hello world!')

# Imports Happen Only Once

import simple  # First import: loads and runs file's code
print(simple.spam)  # Assignment makes an attribute
simple.spam = 2  # Change attribute in module
import simple  # Just fetches already loaded module
printer(simple.spam)  # Code wasn't rerun: attribute unchanged

# import and from Are Assignments

from small import x, y  # Copy two names out
x = 42  # Changes local x only
y[0] = 42  # Changes shared mutable in place

import small  # Get module name (from doesn't)
print(small.x)  # Smalls x is not my x
print(small.y)  # But we share a changed mutable

# Cross-file changes

from small import x, y  # Copy two names out (only)
x = 42  # Changes my x only

import small  # Get module name
small.x = 42  # Changes x in other module
print(small.x)

# Import and from Equivalence
# Potential pitfalls of the from Statement
# When import is required

# import and from Equivalence
