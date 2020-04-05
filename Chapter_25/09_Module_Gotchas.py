# Module Gotchas
# Module Name Clashes: Package and Package-Relative Imports
# Statement Order Matters in Top-Level Code

# func1()  # Error: "func1" not yet assigned


def func1():
    print(func2())  # OK "func2" looked up later


# func1()  # Error: "func2" not yet assigned


def func2():
    return 'Hello'


func1()  # OK: func1() and func2() assigned

# from Copies Names but Doesn't Link
# from * Can Obscure the Meaning of Variables

from nested1 import *  # Bad may overwrite my names silently
from nested2 import *  # Worse no way to tell what we get!
from nested3 import *

printer()  # Huh??

# Reload May Not Impact from Imports

# from module import X  # X may not reflect nay module reloads!
# from importlib import reload
# reload(module)  # Changes module, but not my names
# X  # Still references old object

# import module  # Get module not names
# from importlib import reload
# reload(module)  # Changes module in place
# module.X  # Get current X: reflects module reloads

# reload, from, and Interactive Testing

# from module import function
# function(1, 2, 3)

# from importlib import reload
# reload(module)

# from importlib import reload
# import module
# reload(module)
# function(1, 2, 3)

# from  importlib import reload
# import module
# reload(module)
# from module import function  # Or give up and use module.function()
# function(1, 2, 3)

# Recursive from Imports May Not Work