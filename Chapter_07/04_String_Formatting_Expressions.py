print('That is %d %s bird!' % (1, 'dead'))  # Format expression

exclamation = 'Ni'
print('The knights who say %s!' % exclamation)  # String substitution

print('%d %s %g you' % (1, 'spam', 4.0))  # Type specific substitutions

print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))  # All types match %s target

# %[(keyname)][flags][width][.precision]typecode

x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x, x, x)
print(res)

x = 1.23456789
print(x)  # Shows more digits before 2.7 and 3.1
print('%e | %f | %g' % (x, x, x))
print('%E' % x)

print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print('%s' % x, str(x))

print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

# Template with substitution targets
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40}  # Build up values to substitute
print(reply % values)  # Perform substitutions

food = 'spam'
qty = 10
print(vars())
print('%(qty)d more %(food)s' % vars())  # Variables are keys in vars()

print('%o, %x, %x, %X' % (64, 64, 255, 255))
