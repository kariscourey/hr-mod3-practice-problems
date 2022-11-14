# The function reverse_prefix gets a string s and a single letter letter. The function should find the first occurrence of letter in s and reverse only the letters from the beginning of the string up to and including the target letter. If the letter does not exist in the string, do nothing.

# For example, if you get the string "hackreactor" with the letter "c", then it would find the first c in "hackreactor", take all of the letters from the beginning of the string up to and including that "c" ("hackreactor"), and reverse them ("cahkreactor"). The answer would be the string "cahkreactor".

def reverse_prefix(s, letter):

    # try:
    #     pivot = s.index(letter)

    #     result = s[pivot::-1] + s[pivot + 1:]
    #     return result
    # except ValueError:
    #     return s

    index = s.find(letter)
    prefix = s[:index+1]
    return prefix[::-1] + s[index+1:]
    # s[::index]


print(reverse_prefix("abcdefd", "z"))
