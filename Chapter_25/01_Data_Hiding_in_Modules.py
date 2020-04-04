# Advanced Module Topics
# Module design Concepts
# Data Hiding in Modules
# Minimizing from * Damage: _X and __all__
from unders import *  # Load non _X names only
print(a, c)
# print(_b)

import unders  # But other importers get every name
print(unders._b)

from alls import *  # Load __all__names only
print(a, _c)
# print(b)

from alls import a, b, _c, _d  # But other importers get every name
print(a, b, _c, _d)

import alls
print(alls.a, alls.b, alls._c, alls._d)

# Enabling Future Language Features: __future__

