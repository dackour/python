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
