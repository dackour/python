X = 88  # My X: Global to this file only


def f():
    global X  # Change this file's X
    X = 99  # Cannot se names in other modules

