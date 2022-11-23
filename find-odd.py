# Complete the function find_odd to find the single number in a list that occurs an odd number of times.

# For example, assume you are given the following list:

# [3, 3, 18, 4, 4, 4, 4]
# The single number in the list that occurs an odd number of times is the number 18.

# You are not guaranteed to have them grouped like that. Here's that list, again, in a "messed up" order.

# [3, 4, 4, 3, 4, 18, 4]
# The answer would still be 18.

def find_odd(nums):
    check = {}
    for i in nums:
        if i not in check:
            check[i] = 0
        check[i] += 1
    for i in check:
        if check[i] % 2 == 1:
            return i

nums = [3, 4, 4, 3, 4, 18, 4]
print(find_odd(nums))
