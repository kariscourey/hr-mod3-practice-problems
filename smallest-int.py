# We don't know where Caris is grazing, but they have found another list of single-digit numbers. They'd like you take those numbers and, using them in any order, create the smallest integer possible from those numbers of a certain length of digits.

# For example, if Caris gives you the list [3, 1, 2, 6, 5, 9] and says the length of the number must be three digits, then the result you should give is 123 because that is the smallest three-digit integer you can make from the numbers in the list.

# nums	length	Output
# [3, 1, 2, 6, 5, 9]	3	123
# [3, 1, 2, 6, 5, 9]	5	12356
# [1]	1	1
# [5, 9, 8, 3]	1	3
# [5, 9, 8, 3]	2	35
# [5, 9, 8, 3]	4	3589

def make_integer(nums, length):
    i = 0
    result = []
    while i < length:
        mi = min(nums)
        result.append(str(mi))
        nums.pop(nums.index(mi))
        i += 1
    return int(''.join(result))

nums = [3, 1, 2, 6, 5, 9]
length = 3

print(make_integer(nums, length))
