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


