# Reversing an integer means to reverse all its digits.

# Reversing 2021 results in 1202
# Reversing 1900 results in 91 because the leading zeroes of 0091 go away
# To check if a number is double-reversible, you would take these steps:

# Reverse the input n (say 17) to get the reversed value (71)
# Reverse the reversed value (71) from the previous step (17)
# Return True if the value in step 2 is equal to n
# Return False if the value in step 2 is not equal to n
# n, the input	reversed n	reversed reversed n	Output
# 526	625	526	True
# 1800	81	18	False
# 0	0	0	True
# 770	77	77	False
# Complete the function is_double_reversible to check if a number is the same as its doubly reversed version.

# Challenge mode: If you feel up to it, write your function so that it's O(c). That means you cannot use the str function or any loops

def is_double_reversible(num):
    # str_num = str(num)
    # # if str_num == '0':
    # #     return True
    # # return str_num[-1] != '0'

    # reverse = int(str_num[::-1])
    # reverse2 = int(str(reverse)[::-1])
    # return reverse2 == num

    if num == 0:
        return True
    return num % 10 != 0


print(is_double_reversible(656))
