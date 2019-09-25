import re
match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
print(match.group(1))

match = re.match('[:/](.*)[/:](.*)[/:](.*)', '/user/home:lumberjack')
print(match.group())

print(re.split('[/:]', '/user/home/lumberjack'))