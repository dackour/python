# 1. How do you make a module?
#
# To create a module, you simply write a text file containing Python statements; every
# source code file is automatically a module, and there is no syntax for declaring one.
# Import operations load module files into module objects in memory. You can also
# make a module by writing code in an external language like C or Java, but such
# extension modules are beyond the scope of this book.
#
# 2. How is the from statement related to the import statement?
#
# The from statement imports an entire module, like the import statement, but as an
# extra step it also copies one or more variables from the imported module into the
# scope where the from appears. This enables you to use the imported names directly
# (name) instead of having to go through the module (module.name).
#
# 3. How is the reload function related to imports?
#
# By default, a module is imported only once per process. The reload function forces
# a module to be imported again. It is mostly used to pick up new versions of a
# module’s source code during development, and in dynamic customization scenarios.
#
# 4. When must you use import instead of from?
#
# You must use import instead of from only when you need to access the same name
# in two different modules; because you’ll have to specify the names of the enclosing
# modules, the two names will be unique. The as extension can render from usable
# in this context as well.
#
# 5. Name three potential pitfalls of the from statement.
#
# The from statement can obscure the meaning of a variable (which module it is
# defined in), can have problems with the reload call (names may reference prior
# versions of objects), and can corrupt namespaces (it might silently overwrite names
# you are using in your scope). The from * form is worse in most regards—it can
# seriously corrupt namespaces and obscure the meaning of variables, so it is probably
# best used sparingly.
#
# 6. What...is the airspeed velocity of an unladen swallow?
#
# What do you mean? An African or European swallow?


