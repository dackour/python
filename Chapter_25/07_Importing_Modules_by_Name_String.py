# Importing Modules by Name String
# import 'string'
# x = 'string'
# import x

# Running Code Strings

modname = 'string'
exec('import ' + modname)  # Run a string of code
print(string)  # Imported in this namespace

# Direct Calls: Two Options
modname = 'string'
string = __import__(modname)
print(string)

import importlib
modname = 'string'
string = importlib.import_module(modname)
print(string)
