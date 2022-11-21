# Complete the function below to count the number of "H" letters in a string.

# string	Output
# ""	0
# "WOIEJRF"	0
# "HHHHHAH"	6

def count_letters(string):

    # count = 0

    # for i in string:
    #     if i.lower() == "h":
    #         count += 1

    # return count

    return sum([1 for letter in string if letter.lower() == "h"])
