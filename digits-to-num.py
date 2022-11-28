# Complete the function that is given a list of single digits by combining the entries into a single number and returning that number.

# digits	Output
# [1, 2, 3]	123
# [3]	3
# [9, 9, 0]	990
# [0, 0, 0]	0
# The input will never be an empty list.

def digits_to_number(digits):
    return int(''.join([str(i) for i in digits]))
    # return int(''.join(map(str,digits)))

digits = [1, 2, 3]
print(digits_to_number(digits))
