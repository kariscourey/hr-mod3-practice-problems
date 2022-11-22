# Today, Caris needs some help with a list of numbers they found in the grass while grazing.

# Caris is interested in knowing if there are two distinct entries in the list between two indexes, inclusive, such that when multiplied together they equal a specific number.

# For example, given the list [1, 5, 5, 2, 3], the target product of 25, and the indexes 0 and 2, you should limit your search to just [1, 5, 5] to see if any of those two numbers multiplied together equal 25. The answer is True since the 5 at index 1 and the 5 at index 2 are 25 when they're multiplied together. You include the values at the specified indexes as part of your search.

# Another example: given the list [1, 5, 5, 2, 3], the target product of 25, and the indexes 0 and 1, you should limit your search to just [1, 5] to see if any of those two numbers multiplied together equal 25. The answer is False since we can't multiply 5 by itself to get the answer.

# Your function should return True if you can find two numbers that multiply together to be the target. Otherwise, you should return False.

# nums	left	right	target	Output
# [1, 5, 5, 2, 3]	0	2	25	True
# [1, 5, 5, 2, 3]	0	1	25	False
# [1, 5, 5, 2, 3]	0	3	6	False
# [1, 5, 5, 2, 3]	0	4	10	True
# [2, 4, 2, 4, 2, 4]	0	2	8	True
# [2, 4, 2, 4, 2, 4]	0	5	5	False
# [2, 4, 2, 4, 2, 4]	0	1	1	False
# [2, 4, 2, 4, 2, 4]	0	3	16	True


def does_product_exist(nums, left, right, target):
    for i in nums[left:right + 1]:
        # print(i)
        for j in nums[left + 1:right + 1]:
            # print(j)
            if i * j == target:
                return True
    return False


nums = [1, 5, 5, 2, 3]
left = 0
right = 2
target= 25
print(does_product_exist(nums, left, right, target))
