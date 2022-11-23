# Complete the function fix_misspellings to fix misspelled words.

# The input is a list of dictionaries. Each dictionary contains a misspelled word and the position of the letter that should not belong.

# For example, one of the dictionaries in the list could look like this:

# { "word": "possition", "position": "4" }

# The position of the letter needs to be removed is 4 which is the second s in the word "possition".

# Your job is to iterate over the list of dictionaries, remove the bad letter from the misspelled word, and return a list of just the corrected words in the order they were received in the input.

# # INPUT:
# [ { "word": "tablett", "position": 7 },
#   { "word": "marrble", "position": 4 },
#   { "word": "xdocker", "position": 1 },
# ]

# # OUTPUT: Words in order that they were received
# #         in the input
# [ "tablet", "marble", "docker" ]

def fix_misspellings(corrections):
    results = []
    for i in corrections:
        word = list(i['word'])
        word.pop(i['position'] - 1)
        results.append(''.join(word))
    return results


corrections = [
    { "word": "tablett", "position": 7 },
    { "word": "marrble", "position": 4 },
    { "word": "xdocker", "position": 1 },
]

print(fix_misspellings(corrections))
