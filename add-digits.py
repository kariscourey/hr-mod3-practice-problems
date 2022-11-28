# You are given a function that has two lists of digits. The function should convert each list to an integer, add them together, then return the sum.

# digits1	digits2	Output
# [1, 2, 3]	[1, 2, 3]	246
# [3]	[1, 2, 3]	126
# [9, 9, 9]	[0, 0, 0]	999
# You can copy and paste your other function into this code block before the add_digits function and use it, if you'd like.

# You can paste your function from the last problem, here,
# if you want

def add_digits(digits1, digits2):
    dig1 = int(''.join([str(i) for i in digits1]))
    dig2 = int(''.join([str(i) for i in digits2]))
    return dig1 + dig2

digits1 = [1, 2, 3]
digits2 = [1, 2, 3]
print(add_digits(digits1, digits2))
