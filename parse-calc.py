# Let's make a calculator!

# You're given a string with two numbers in prefix or 'Polish' notation. Operations can be one of multiplication, division, addition, and subtraction. They are written as +, *, /, and - respectively.

# Many calculators from the 1980's operated this way.

# Write a function called parse_calculation that reads the string and returns a value.

# You may find str.strip() and eval() useful.

# s	Output
# "+ 1 1"	2
# "* 4 12"	48
# "/ 10 5"	2
# "- 10 15"	-5

def parse_calculation(s):
    s = s.split(' ')
    # expression = s[1] + ' ' + s[0] + ' ' + s[2]
    expression = (f'{s[1]} {s[0]} {s[2]}')
    return eval(expression)

s = "* 4 12"
print(parse_calculation(s))
