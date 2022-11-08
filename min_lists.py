# The function find_lists_with_minimum_value takes in a list of lists. The function will consider all of the values in all of the lists and find the minimum value. Then, it will return a list that contains the indexes of the lists that contain the minimum value in increasing order.

# For example, consider this input:

# INPUT
# [
#   [6, 4, 5, 2, 6, 3, 2],
#   [3, 3, 3, 4],
#   [4, 2, 3, 2, 4],
# ]

# OUTPUT
# [0, 2]
# If you consider the values in all of the lists, the minimum value is 2. The lists that contain the value 2 are the ones at index 0 and index 2. That's what the function will return.

# Here's another example:

# # INPUT
# [
#   [7],
#   [9],
#   [8],
#   [1],
# ]

# # OUTPUT
# [3]
# The minimum value from all of the values in all of the lists is 1. The only list that contains that value is the fourth list at index 3. That's what the function will return.

def find_lists_with_minimum_value(lists):
    # big = []
    # result = []
    # for i in lists:
    #     big += i
    # big_min = min(big)
    # for index, value in enumerate(lists):
    #     if big_min in value:
    #         result.append(index)
    # return result
    mins = [min(lst) for lst in lists]
    min_of_mins = min(mins)
    [i for i, n in enumerate(mins) if n == min_of_mins]

lists = [
  [6, 4, 5, 2, 6, 3, 2],
  [3, 3, 3, 4],
  [4, 2, 3, 2, 4],
]
print(find_lists_with_minimum_value(lists))
