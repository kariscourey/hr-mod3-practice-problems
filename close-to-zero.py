# Given a list of integer numbers nums, return the number in the list that is the closest to 0. If there are multiple answers, return the number with the largest value.

# nums	Output	Explanation
# [3, -2]	-2	-2 is only 2 away from 0
# [-4, 3]	3	3 is only 3 away from 0
# [2, -2]	2	2 because it is the larger of the two values
# [4, -2, 1]	1	1 because it is only 1 away from 0
# The list nums will always have at least one number in it.

# Your solution should take $O(n)$ time and use $O(c)$ space.

# The absolute value of a number refers to the distance of a number from 0. Please refer to the built-in abs function to understand how it works.

def closest_to_zero(nums):
    # min = abs(nums[0])
    # result = nums[0]
    # for i in nums:
    #     if abs(i) <= min:
    #         min = abs(i)
    #         if abs(i) == min and abs(result) > i:
    #             result = i
    # return result
    closest = nums[0]

    for i in nums[1:]:
        if abs(i) < abs(closest):
            closest = i
        elif abs(i) == abs(closest):
            closest = i if i > closest else closest

    return closest

# def closest_to_zero(nums):
#     delta = [abs(num) for num in nums]
#     lowest = min(delta)
#     if delta.count(lowest) > 1:
#         return abs(nums[delta.index(lowest)])
#     return nums[delta.index(lowest)]

# def closest_to_zero(nums):
#     lowest = min(nums, key=abs)
#     for num in nums:
#         if abs(lowest) == abs(num) and lowest < num:
#             return num
#     return lowest

# def closest_to_zero(nums):
#     closest = nums[0]
#     for num in nums:
#         if abs(closest) > abs(num):
#             closest = num
#         elif abs(closest) == abs(num) and closest < num:
#             closest = num
#     return closest


nums = [2, -2]
# nums = [4, -2, 1]
# nums = [3, -2]
print(closest_to_zero(nums))
