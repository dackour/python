#!python
"""
reloadall.py: transitively reload modules (2.X + 3.X).
Call reload_all with one ore more imported module objects.
"""

import types
from importlib import reload


def status(module):
    print('reloading ' + module.__name__)


def tryreload(module):
    try:
        reload(module)
    except:
        print('FAILED: %s' % module)


def transitive_reload(module, visited):
    if not module in visited:  # Trap cycleds, duplicates
        status(module)  # Reload this module
        tryreload(module)  # And visit children
        visited[module] = True
        for attrobj in module.__dict__.values():  # For all attrs
            if type(attrobj) == types.ModuleType:  # Recure if module
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}  # Main entry point
    for arg in args:  # For all passed in
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


def tester(reloader, modname):  # Self test code
    import importlib, sys  # Import on tests only
    if len(sys.argv) > 1: modname = sys.argv[1]  # Command line (or passed)
    module = importlib.import_module(modname)  # Import by name string
    reloader(module)  # Test passed-in reloader


if __name__ == '__main__':
    tester(reload_all, 'reloadall')  # Test: reload myself