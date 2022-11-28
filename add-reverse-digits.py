# You are given a function that has two lists of digits in reversed order. The function should convert each list to an integer in reverse order, add them together, then return the sum.

# reversed_digits1	reversed_digits2	Output
# [3, 2, 1]	[3, 2, 1]	246
# [3]	[3, 2, 1]	126
# [9, 9, 9]	[0, 0, 0]	999
# You can copy and paste your other function into this code block before the add_digits function and use it, if you'd like.

# You can paste your functions from the last problem, here,
# if you want

def add_reversed_digits(reversed_digits1, reversed_digits2):
    dig1 = int(''.join([str(i) for i in reversed_digits1[::-1]]))
    dig2 = int(''.join([str(i) for i in reversed_digits2[::-1]]))
    return dig1 + dig2

digits1 = [9,9,9]
digits2 = [0,0,0]
digits1 = [3]
digits2 = [3,2,1]
print(add_reversed_digits(digits1, digits2))
