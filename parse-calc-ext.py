# Let's extend your calculator!

# We are going to extend the last problem by also handling additional calls. See the examples.

# s	Output
# "3"	3
# "(+ 1 1 )"	2
# "(* 4 (- 1 2 ) )"	-4
# "(/ (- 10 2 ) 4 )"	2
# "(- (+ (+ 2 4 ) (* 1 8 ) ) 15 )"	-1
# Assume any operation contains exactly two operands.

# You will want to write a recursive function and a helper function that will compute the bounds of the outer-most parenthesis. This can be tricky, due to the recursive nature, but if you create a counter to track how deep you are nested, it will inform you when an expression ends.

# Also, str.strip() will continue to be very useful. All terms are spaced except the operator and left parenthesis.

import re

def calc_match(s):
    s = match.group()
    parts = s.split(' ')
    return str(eval(f'{parts[1]} {parts[0][1]} {parts[2]}'))

def parse_calculation_ext(s):
    while '(' in s:
        s = re.sub('\([+-/*] \d+ \d+ \)', calc_match, s)


s = "(- (+ (+ 2 4 ) (* 1 8 ) ) 15 )"
print(parse_calculation_ext(s))
