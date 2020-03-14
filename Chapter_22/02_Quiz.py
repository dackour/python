# 1. How does a module source code file become a module object?
# A module’s source code file automatically becomes a module object when that
# module is imported. Technically, the module’s source code is run during the import,
# one statement at a time, and all the names assigned in the process become
# attributes of the module object.

# 2. Why might you have to set your PYTHONPATH environment variable?
# You only need to set PYTHONPATH to import from directories other than the one in
# which you are working (i.e., the current directory when working interactively, or
# the directory containing your top-level file). In practice, this will be a common case
# for nontrivial programs.

# 3. Name the five major components of the module import search path.
# The five major components of the module import search path are the top-level
# script’s home directory (the directory containing it), all directories listed in the
# PYTHONPATH environment variable, the standard library directories, all directories
# listed in .pth path files located in standard places, and the site-packages root directory
# for third-party extension installs. Of these, programmers can customize
# PYTHONPATH and .pth files.

# 4. Name four file types that Python might load in response to an import operation.
# Python might load a source code (.py) file, a byte code (.pyc or .pyo) file, a C extension
# module (e.g., a .so file on Linux or a .dll or .pyd file on Windows), or a
# directory of the same name for package imports. Imports may also load more exotic
# things such as ZIP file components, Java classes under the Jython version of
# Python, .NET components under IronPython, and statically linked C extensions
# that have no files present at all. In fact, with import hooks, imports can load arbitrary
# items.

# 5. What is a namespace, and what does a module’s namespace contain?
# A namespace is a self-contained package of variables, which are known as the
# attributes of the namespace object. A module’s namespace contains all the names
# assigned by code at the top level of the module file (i.e., not nested in def or
# class statements). Technically, a module’s global scope morphs into the module
# object’s attributes namespace. A module’s namespace may also be altered by assignments
# from other files that import it, though this is generally frowned upon
# (see Chapter 17 for more on the downsides of cross-file changes).