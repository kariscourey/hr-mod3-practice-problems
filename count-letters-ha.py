# Complete the function below to count the number of "H"s followed by "A"s in a string. The "A" does not have to immediately follow the "H".

# string	Output
# ""	0
# "HA"	1
# "HAHA"	2
# "HXAXHX"	1
# "HXAXHXA"	2
# "HHHHHAAAAA"	1
# The string "HA" has one "H" followed by an "A" (1)
# The string "HAHA" has one "H" followed by an "A" (1), and another "H" followed by an "A" (2)
# The string "HXAXHX" has one "H" followed by an "X" (ignored) followed by an "A" (1) followed by an "X" (ignored) followed by an "H" followed by an "X" (ignored)
# The string "HXAXHXA" has one "H" followed by an "X" (ignored) followed by an "A" (1) followed by an "X" (ignored) followed by an "H" followed by an "X" (ignored) followed by an "A" (2)
# The string "HHHHHAAAAA" has one "H" followed by an "H" (ignored) followed by an "H" (ignored) followed by an "H" (ignored) followed by an "H" (ignored) followed by an "A" (1) followed by an "A" (ignored) followed by an "A" (ignored) followed by an "A" (ignored) followed by an "A" (ignored)

def count_letters(string):

    count = 0
    h_check = False

    for i in string:
        if i.lower() == "h":
            h_check = True
        elif i.lower() == "a" and h_check == True:
            count += 1
            h_check = False

    return count
