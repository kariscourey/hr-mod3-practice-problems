# Complete the function below to count the number of "HACK"s in a string. The letters do not have to immediately follow one another.

# string	Output
# ""	0
# "HACK"	1
# "HAXXCK"	1
# "XHXAXCXKX"	1
# "HHHAAACCCKKK"	1
# "HXACXKXXHACXK"	2
# The string "HACK" has one "H" followed by an "A" followed by an "C" followed by an "K" (1)
# The string "HAXXCK" has one "H" followed by an "A" followed by an "X" (ignored) followed by an "X" (ignored) followed by an "C" followed by an "K" (1)
# The string "XHXAXCXKX" has
# an "X" (ignored) followed by
# an "H" followed by
# an "X" (ignored) followed by
# an "A" followed by
# an "X" (ignored) followed by
# an "C" followed by
# an "X" (ignored) followed by
# an "K" (1) followed by
# an "X" (ignored)

def count_letters(string):

    # count = 0
    # h_check = False
    # a_check = False
    # c_check = False

    # for i in string:
    #     if i.lower() == "h":
    #         h_check = True
    #     elif i.lower() == "a" and h_check == True:
    #         a_check = True
    #     elif i.lower() == "c" and a_check == True:
    #         c_check = True
    #     elif i.lower() == "k" and c_check == True:
    #         count += 1
    #         h_check = False
    #         a_check = False
    #         c_check = False

    # return count

    # letters = {
    #     'H': 'A',
    #     'A': 'C',
    #     'C': 'K',
    #     'K': 'H',
    # }
    # letter_to_find = 'H'
    # count = 0

    # for c in string:
    #     if c == letter_to_find:
    #         if letter_to_find == 'K': count += 1
    #         letter_to_find = letters[letter_to_find]

    # return count

    word_to_find = 'HACK'
    i = 0
    count = 0

    for c in string:
        index = i % len(word_to_find)
        if c == word_to_find[index]:
            if index == len(word_to_find) - 1: count += 1
            i += 1

    return count
