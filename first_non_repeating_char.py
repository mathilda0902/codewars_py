# First non-repeating character
# Write a function named firstNonRepeatingLetter† that takes a string input, and
# returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same
# character, but the function should return the correct case for the initial letter.
# For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return the empty string ("").

def first_non_repeating_letter1(string):
    for i, e in enumerate(string):
        if e.lower() not in string[i+1:].lower() and e.lower() not in string[:i].lower():
            return e

def first_non_repearting_letter2(string):
    string_lower = string.lower()
    for i, e in enumerate(string_lower):
        if string_lower.count(e) == 1:
            return string[i]
    return ''
