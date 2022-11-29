# Write the simplest code you can to make the function roman_numeral pass its tests. It now tests 3 -> "III" in addition to all of the previous tests.

# class TestChallenge(TestCase):
#     # Previous tests for 1 -> "I" and 2 -> "II"

#     def test_3(self):
#         input = 3
#         expected = "III"

#         result = roman_numeral(input)

#         self.assertEqual(result, expected)
# Again, this isn't a trick. Write the simplest code you can to return "I" for 1, "II" for 2, and "III" for 3.

def roman_numeral(num):
    if num == 1:
        return 'I'
    elif num == 2:
        return 'II'
    return 'III'

# Do you have something that looks like this?

# def roman_numeral(num):
#     if num == 1:
#       return "I"
#     elif num == 2:
#       return "II"
#     elif num == 3:
#       return "III"
# If you do, then that's great! That's very simple code. You have written code that meets every single test.

# After each time you write code to make a test pass, you should take the opportunity to think about how to make it simpler.

# A long chain of if-elif is not necessarily the "simplest" code. "Simple" is a qualitative assessment. Generally, we measure "simple" as striking the balance between these two concepts:

# Easy to understand
# Fewer lines of code.
# Can you write roman_numeral as a single line of code for the current test cases for the inputs 1, 2, and 3?

# Hint: What happens when you multiply a string by an integer in Python?

def roman_numeral(num):
    return num * 'I'

# Write the simplest code you can to make the function roman_numeral pass its tests. It now tests 8 -> "VIII" in addition to all of the previous tests.

# class TestChallenge(TestCase):
#     # Previous tests for 1 -> "I", 2 -> "II", 3 -> "III",
#     #   4 -> "IV", 5 -> "V", 6 -> "VI", and 7 -> "VII"

#     def test_8(self):
#         input = 8
#         expected = "VIII"

#         result = roman_numeral(input)

#         self.assertEqual(result, expected)

def roman_numeral(num):
    if num == 4:
        return 'IV'
    elif num == 5:
        return 'V'
    elif num == 6:
        return 'VI'
    elif num == 7:
        return 'VII'
    elif num == 8:
        return 'VIII'
    else:
        return num * 'I'

# Do you have something like this?

# def roman_numeral(num):
#     if num == 8:
#         return "VIII"
#     elif num == 7:
#         return "VII"
#     elif num == 6:
#         return "VI"
#     elif num == 5:
#         return "V"
#     elif num == 4:
#         return "IV"
#     else:
#       return num * "I"
# If so, now's the opportunity to refactor. Look at the conditional statements for the numbers 5 - 8. Can you see a pattern there similar to what you did for the numbers 1 - 3?

# See if you refactor the function to have no more than eight lines. It currently has 13 lines.

def roman_numeral(num):
    if num >= 5:
        return 'V' + (num - 5) * 'I'
    elif num == 4:
        return 'IV'
    else:
      return num * "I"


# Write the simplest code you can to make the function roman_numeral pass its tests. It now tests 10 -> "X" in addition to all of the previous tests.

# class TestChallenge(TestCase):
#     # Previous tests for 1 -> "I", 2 -> "II", 3 -> "III",
#     #   4 -> "IV", 5 -> "V", 6 -> "VI", 7 -> "VII",
#     #   8 -> "VIII", and 9 -> "IX"

#     def test_10(self):
#         input = 10
#         expected = "X"

#         result = roman_numeral(input)

#         self.assertEqual(result, expected)

def roman_numeral(num):
    if num >= 10:
        return 'X' + (num - 10) * 'I'
    elif num == 9:
        return 'IX'
    elif num >= 5:
        return 'V' + (num - 5) * 'I'
    elif num == 4:
        return 'IV'
    else:
      return num * "I"
