S = 'Spam'
print(S.find('pa'))             # Find the offset of a substring in S
print(S)
print(S.replace('pa', 'XYZ'))   # Replace occurrences of a string in S with another
print(S)

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))              # Split on a delimiter into a list of substrings
print(S.upper())                    # Upper- and lowercase conversions
print(S.isalpha())                  # Content test: isalpha, isdigit, etc

line = 'aaa,bbb,ccccc,dd\n'
print(line.rstrip())                # Remove whitespace characters on the right side
print(line.rstrip().split(','))     # Combine two operations

print('%s, eggs, and %s' % ('spam', 'SPAM!'))           # Formatting expression (all)
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))     # Formatting method (2.6+,3.0+)
print('{}, eggs and {}'.format('spam', 'SPAM!'))        # Numbers optional (2.7+,3,1+)

print('{:,.2f}'.format(296999.2567))                      # Separator, decimal digits
print('%.2f | %+05d' % (3.14159, -42))                    # Digits, padding, signs


