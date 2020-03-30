# Package Relative Imports
# Changes in Python 3.X
# Relative Import Basics
# Why Relative Imports?
# The relative imports solution in 3.X
# The Scope of relative Imports
# Module Lookup Rules Summary
# Relative imports in Action
import sys
import string
print(sys.path)
print(string)

# Imports within packages
import pkg.spam

# Imports are still relative to the CWD
# Selecting modules with relative and absolute imports
# Relative imports search packages only
# Imports are still relative to the CWD, again
# Pitfalls of Package-Relative Imports: Mixed Use
# The issue
# Fix 1: Package subdirectories
# Fix 2: Full path absolute import
# Example: Application to module self-test code (preview)

