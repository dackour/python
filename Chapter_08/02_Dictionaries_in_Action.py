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
