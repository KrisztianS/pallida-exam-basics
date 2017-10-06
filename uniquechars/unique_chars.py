# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
from collections import OrderedDict

def unique_characters(string):
    character_counter = []
    for character in string[::]:
        if character not in character_counter:  
            character_counter.append(character)
    return character_counter

print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]
