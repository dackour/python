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
