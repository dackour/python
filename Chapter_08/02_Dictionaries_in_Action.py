D = {'spam': 2, 'ham': 1, 'eggs': 3}  # Make a dictionary
print(D['spam'])  # Fetch a value by key
print(D)  # Order is "scrambled"

print(len(D))  # Number of entries in dictionary
print('ham' in D)  # Key membership test alternative
print(list(D.keys()))  # Create a new list of D's keys
print(D.keys())

print(D)
D['ham'] = ['grill', 'bake', 'fry']  # Change entry (value = list)
print(D)
del D['eggs']  # Delete entry
print(D)
D['brunch'] = 'bacon'  # Add new entry
print(D)

D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
print(list(D.items()))

print(D.get('spam'))
print(D.get('toast'))  # A key that is missing
print(D.get('toast', 88))

print(D)
D2 = {'toast': 4, 'muffin': 5}  # Lots of delicious scrambled order here
D.update(D2)
print(D)

# pop a dictionary by key
print(D)
print(D.pop('muffin'))
print(D.pop('toast'))  # Delete and return from a key
print(D)

# pop a list by position
L = ['aa', 'bb', 'cc', 'dd']
print(L.pop())  # Delete and return from the end
print(L)
print(L.pop(1))  # Delete from a specific position
print(L)

table = {  # Key: Value
    '1975': 'Holy Grail',
    '1979': 'Life of Brian',
    '1983': 'The Meaning of Life'
}

year = '1983'
movie = table[year]  # dictionary[Key] => Value
print(movie)

for year in table:  # Same as for year in table.keys()
    print(year + '\t' + table[year])

table = {  # Key=>Value (title=>year)
    'Holy Grail': '1975',
    'Life of Brian': '1979',
    'The Meaning of Life': '1983'
}

print(table['Holy Grail'])

print(list(table.items())) # Value=Key (year=>title)

print([title for (title, year) in table.items() if year == '1975'])

K = 'Holy Grail'
print(table[K])  # Key=>Value (normal usage)

V = '1975'
print([key for (key, value) in table.items() if value == V])  # Value=>Key
print([key for key in table.keys() if table[key] == V])  # Ditto

# L = []
# L[99] = 'spam'

D = {}
D[99] = 'spam'
print(D[99])
print(D)

table = {
    1975: 'Holy Grail',
    1979: 'Life of Brian',  # Keys are integers, not strings
    1983: 'The Meaning of Life'
}
print(table[1975])
print(list(table.items()))

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4  # ; separates statements: see Chapter 10
print(Matrix[(X, Y, Z)])
print(Matrix)

# Matrix[(2, 3, 6)]

if (2, 3, 6) in Matrix:  # check for key before fetch
    print(Matrix[(2, 3, 6)])  # See Chapter 10 and 12 for if/else
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])  # try to index
except KeyError:  # catch and recover
    print(0)  # see chapter 10 and 34 for try/except

print(Matrix.get((2, 3, 4), 0))  # Exists: fetch and return
print(Matrix.get((2, 3, 6), 0))  # Doesnt exists: use default arg

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'

print(rec['name'])

rec = {
    'name': 'Bob',
    'jobs': ['developer', 'manager'],
    'web': 'www.bobs.org/~Bob',
    'home': {'state': 'Overworked', 'zip': 12345}
}

rec2 = {
    'name': 'Jack',
    'jobs': ['Admin', 'manager'],
    'web': 'www.jacks.org/~Jack',
    'home': {'state': 'Married', 'zip': 54321}
}

print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])

db = []  # A list "Database"
db.append(rec)
db.append(rec2)
print(db[0]['jobs'])
print(db[1]['jobs'])

db = {}
db['bob'] = rec  # A dictionary "database"
db['jack'] = rec2
print(db)
print(db['bob']['jobs'])

{'name': 'Bob', 'age': 40}  # traditional literal expression

D = {}  # assigned by keys dynamically
D['name'] = 'Bob'
D['age'] = 40

dict(name='Bob', age=40)  # dict keyword argument form
dict([('name', 'Bob'), ('age', 40)]) # dict key/value tuples form

keylist = ['name', 'age']
valueslist = ['Bob', 40]
D2 = dict(zip(keylist, valueslist))  # Zipped key/value tuples form (ahead)
print(D2)

print(dict.fromkeys(['a', 'b'], 0))

L = ['Bob', 40.5, ['dev', 'mgr']]  # List-based "record"
print(L[0])
print(L[1])  # Position/numbers for fields
print(L[2][1])

D = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}  # Dictionary-based "record"
print(D['name'])
print(D['age'])
print(D['jobs'][1])  # Names mean more than numbers

D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
print(D['name'])
D['jobs'].remove('mgr')
print(D)

D = {}
D['state1'] = True  # A visited state dictionary
print('state1' in D)

S = set()
S.add('state1')  # Same but with sets
print('state1' in S)

print(list(zip(['a', 'b', 'c'], [1, 2, 3])))  # Zip together keys and values

D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # Make a dict from zip result
print(D)

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)

D = {x: x ** 2 for x in [1, 2, 3, 4]}  # Or range(1, 5)
print(D)

D = {c: c * 4 for c in 'SPAM'}  # Loop over any iterable
print(D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)

D = dict.fromkeys(['a', 'b', 'c'], 0)  # Initialize dict from keys
print(D)

D = {k: 0 for k in ['a', 'b', 'c']}  # Same but with a comprehension
print(D)

D = dict.fromkeys('spam')  # Other iterables, default value
print(D)

D = {k: None for k in 'spam'}
print(D)

D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()  # Makes a view object in 3.X, not a list
print(K)
print(list(K))  # Force a real list in 3.X if needed

V = D.values()
print(V)
print(list(V))

print(D.items())
print(list(D.items()))

#K[0]  # List operation fails unless converted
print(list(K)[0])

for k in D.keys(): print(k)  # Iterators used automatically in loops

for key in D: print(key)  # Still no need to call keys() to iterate

D = {'b': 2, 'c': 3, 'a': 1}
print(D)

K = D.keys()
V = D.values()
print(list(K))  # Views maintain same order as dictionary
print(list(V))

del D['b']  # Change a dictionary in place
print(D)

print(list(K))  # Reflected in any current view objects
print(list(V))  # Not true in 2.X! list detached from dict

print(K, V)
print(K | {'x': 4})  # Keys (and some items) views are setilike

#V & {'x': 4}
#V & {'x': 4}.values()

D = {'a': 1, 'b': 2, 'c': 3}
print(D.keys() & D.keys())  # Intersect keys views
print(D.keys() & {'b'})  # Intersect keys and set
print(D.keys() & {'b': 1})  # Intersect keys and dict
print(D.keys() | {'b', 'c', 'd'})  # Union keys and set

D = {'a': 1}
print(list(D.items()))  # Items set-like if hashable
print(D.items() | D.keys())  # Union view and view
print(D.items() | D)  # dict treated same as its keys
print(D.items() | {('c', 3), ('d', 4)})  # Set of key/value pairs
print(dict(D.items() | {('c', 3), ('d', 4)}))  # dict accepts iterable sets too

D = {'b': 2, 'c': 3, 'a': 1}
print(D)

Ks = D.keys()  # Sorting a view object doesnt work!
#Ks.sort()

Ks = list(Ks)  # Force it to be a list and then sort
Ks.sort()

for k in Ks: print(k, D[k])  # 2.X omit outer parens in prints

print(D)
Ks = D.keys()  # Or you can use sorted() on the keys
for k in sorted(Ks): print(k, D[k])  # Sorted() accepts any iterable and returns its result

print(D)  # Better yet, sort the dict directly
for k in sorted(D): print(k, D[k])  # dict iterators return keys

D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'a': 1, 'b': 2, 'c': 3}
# print(sorted(D1.items())) < sorted(D2.items())  # Like 2.X D1 < D2
print(D1 == D2)

D = {'b': 2, 'c': 3, 'a': 1}
#D.has_key('c')  # 2.X only: True/False

print('c' in D)  # Required in 3.X
print('x' in D)  # Preferred in 2.X today

if 'c' in D: print('present', D['c'])  # Branch on result

print(D.get('c'))  # Fetch with default
print(D.get('x'))

if D.get('c') != None: print('present', D['c'])  # Another option
