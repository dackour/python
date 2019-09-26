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

bob1 = dict(name= 'Bob', job= 'dev', age=40)  # Keywords
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

