# Imports and Attributes

import b

b.spam('gumby')

# Standard Library Modules
# How Imports Work
# 1. Find It
# 2. Compile It (Maybe)
# 3. Run It

import sys

print(sys.modules.keys())

# Byte Code Files: __pycache__ in Python 3.2+
# Byte Code File Models in Action
# The Module Search Path
# Configure the Search Path
# Search Path Variations
# The sys.path List

import sys
print(sys.path)

# sys.path.append
# sys.path.insert

# Module File Selection
# Module sources
# Selection priorities
# Import hooks and ZIP files
# Optimized byte code files
# Third-Party Software: distutils

