# When babies babble, they say things like GAGAGOOGOO or BABABABA. For the purposes of this question, we'll define a baby talk word to be any non-empty string of letters that can be divided into two equal-length portions in such a way that the first portion is identical to the second.

# Based on that definition, the following strings are words in baby talk: GAGA, GOOGOO, BABA, GUBBAGUBBA, DOGGIEDOGGIE, FDSFDS, IWANTMOREMILKIWANTMOREMILK, and XX.

# The following strings are not words in baby talk: BABAB, GAGOO, BA, DOGGIE, and X.

# Complete the baby_talk function to find the longest substring consisting of baby talk, as defined above, and return that length. In the test cases below, the longest baby talk string in each input string is underlined.

# Input	Output
# GOOGOOGAGA	6
# BABABABA	8
# PTHHPTHHBAGOOGOOGAGABOOOOO	6
# XYBABABABAXYX	8
# BABAGOOGOOGOOGOOGOOGOOBA	18
# NOBABYTALKHERE	0

def baby_talk(s):
    # indices = {}
    # result = []
    # for index, value in enumerate(s):
    #     if value not in indices:
    #         indices[value] = index
    # keys = indices.keys()
    # values = indices.values()
    # for i in values:
    #     if (i - values[i+1]) < 1:
    #         result.append(i,i+1)
    # return keys, values
    # i = (s+s).find(s, 1, -1)
    # return None if i == -1 else s[:i]

    window = len(s)
    if window % 2 == 1:
        window -= 1
    while window > 0:
        high = len(s) - window + 1
        for i in range(0, high):
            substr = s[i:i+window]
            half = window // 2
            first = substr[:half]
            second = substr[half:]
            if second == first:
                return window
        window -= 2
    return window

s = 'BABAGOOGOOGOOGOOGOOGOOBA'
print(baby_talk(s))
