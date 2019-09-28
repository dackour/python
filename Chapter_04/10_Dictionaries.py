D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food'])  # Fetch value of key 'food'
D['quantity'] += 1  # Add 1 to 'quantity' value
print(D)

D2 = {}
D2['name'] = 'Bob'  # Create keys by assignment
D2['job'] = 'dev'
D2['age'] = 40
print(D2)
print(D2['name'])

bob1 = dict(name='Bob', job='dev', age=40)  # Keywords
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))  # Zipping
print(bob2)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}

print(rec)

print(rec['name'])  # Name is a Nested dictionary
print(rec['name']['last'])  # Index the nested dictionary
print(rec['jobs'])  # 'jobs' is a Nested list
print(rec['jobs'][-1])  # Index the nested list
rec['jobs'].append('janitor')  # Expand Bob job description in place
print(rec['jobs'])

rec = 0

D3 = {'a': 1, 'b': 2, 'c': 3}
print(D3)

D3['e'] = 99  # Assigning new keys grows dictionaries
print(D3)

# D['f'] Referencing nonexistent key is an error

print('f' in D3)

if not 'f' in D3:  # Python sole selection statement
    print('missing')

if not 'f' in D3:
    print('missing')
    print('no, really')  # Statement blocks are indented

value = D3.get('x', 0)  # Index but with a default
print(value)

value = D3['x'] if 'x' in D3 else 0  # if/else expression form
print(value)

D4 = {'a': 1, 'c': 3, 'b': 2}
Ks = list(D4.keys())  # Unordered keys list
print(Ks)

Ks.sort()
print(Ks)

for key in Ks:
    print(key, '=>', D4[key])