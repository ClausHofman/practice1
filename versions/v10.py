from helper_functions import (count_whitespaces_and_newlines, count_words, find_words_after, list_words_by_frequency, find_words_ending_with_from_file, 
                              remove_words_from_unique_words_set, list_words_of_length, read_input_string, find_words_ending_with_from_set, find_words_starting_with_from_set, 
                              find_sentences_with_word)
import ast
import os
import helper_functions

# 1. Variables for function list_words_of_length
FUNC1_WORD_LENGTH = 4
FUNC1_READ_FILENAME = 'unique_words.txt' # Should contain a python set of unique words

# 2. Variable for function remove_words_from_unique_words_set. Add words as necessary
FUNC2_ADD_TO_REMOVED_WORDS = []

# 3. Variable for function read_input_string
INPUT_STRING_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\input.txt"

# 4. Variables for function list_words_by_frequency
FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt"
FUNC4_READ_UNIQUE_WORDS_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt"

# 5. Find words ending with a specified suffix/prefix from a set of words and write them to a target file
FUNC5_SUFFIX = ''
FUNC5_PREFIX = ''
FUNC5_READ_WORD_SET_FILEPATH = r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt'
# Don't necessarily need to touch these without a reason
func5_variable_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH).rsplit('.', 1)[0] # Split from FUNC5_READ_WORD_SET_FILEPATH and remove the file extension
FUNC5_WRITE_FILEPATH = fr'C:\Users\hoffi\Documents\GitHub\2025\practice1\from_{func5_variable_filename}_ending_with_{FUNC5_SUFFIX}.txt'
func5_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH).rsplit('.', 1)[0]  # Split from FUNC5_READ_WORD_SET_FILEPATH and remove the file extension
FUNC5_WRITE_PREFIX_FILEPATH = fr'C:\Users\hoffi\Documents\GitHub\2025\practice1\from_{func5_filename}_starting_with_{FUNC5_PREFIX}.txt'

# 6. Variables for function find_words_ending_with_from_file: FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH is used as the target file
FUNC6_SUFFIX = ''
FUNC6_PRINT = False

# Don't necessarily need to touch these without a reason
FUNC6_READ_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt"
FUNC6_WRITE_FILEPATH = f'ending_with_{FUNC6_SUFFIX}_from_{os.path.basename(FUNC6_READ_FILEPATH)}'

# 8. Variable for function find_next_word_after
FIND_WORDS_AFTER = ''

# 9. Variable for function find_sentences_with_word
FUNC9_WORD_TO_SEARCH = 'watermelon'

# Don't necessarily need to touch this without a reason
FUNC9_READ_FILEPATH = INPUT_STRING_FILEPATH


# 1. Test list_words_of_length function #
#########################################

# Return words of the specified length from the unique words set
words_of_length = list_words_of_length(FUNC1_WORD_LENGTH, FUNC1_READ_FILENAME)

# Write the words of the specified length to a file for easier inspection
with open(f'unique_words_of_length_{FUNC1_WORD_LENGTH}.txt', 'w') as file:
    for word in words_of_length:
        file.write(f"{word}\n")

# Print the words of the specified length
print(f"Words of length {FUNC1_WORD_LENGTH} in {FUNC1_READ_FILENAME}:")
for word in words_of_length:
    print(f"- {word}")

# 2. Test remove_words_from_unique_words_set function which removes words from the unique words set and adds them to a separate set (file) #
#####################################################################################################################################

words_to_remove = FUNC2_ADD_TO_REMOVED_WORDS  # Replace with the words you want to remove
remove_words_from_unique_words_set(words_to_remove, 'unique_words.txt', 'removed_words.txt')

# 3. Read a string from a file and print some additional information about the input string with the help of count_whitespaces_and_newlines and count_words functions #
#######################################################################################################################################################################
# The string that is used in a few functions in this script. Needs INPUT_STRING_FILEPATH to be set to a valid file path
input_string = read_input_string(INPUT_STRING_FILEPATH)

# Return a tuple of whitespace count and newline count, not sure if this is useful for anything
whitespace_count, newline_count = count_whitespaces_and_newlines(input_string)
# Everything won't probably be a word but gives some idea of the word count, could try to invent logic to make the number more accurate
word_count = count_words(input_string)

# Just some information about the input string
print(f"Whitespace count: {whitespace_count}")
print(f"Newline count: {newline_count}")
print(f"Word count: {word_count}")

# 4. Write word frequencies from input_string/INPUT_STRING_FILEPATH to a file and also read and make a set from unique_words.txt #
#####################################################################################################################
# Input string is formed earlier in the script (3. Read a string from a file...)
word_frequencies = list_words_by_frequency(input_string)
with open(FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH, 'w') as file:
    for word, frequency in word_frequencies:
        file.write(f"{word}: {frequency}\n")

try:
    with open(FUNC4_READ_UNIQUE_WORDS_FILEPATH, 'r') as file:
        # Read the set of unique words from the file
        # Use ast.literal_eval to safely evaluate the string as a Python literal
        unique_words = ast.literal_eval(file.read())
except FileNotFoundError:
    unique_words = set()

# 5. Find words from a set of words ending with a specified suffix/prefix and write them to a target file using find_words_ending_with_from_set function #
###################################################################################################################################################

words_ending_with_suffix_from_set = find_words_ending_with_from_set(FUNC5_SUFFIX, FUNC5_READ_WORD_SET_FILEPATH, FUNC5_WRITE_FILEPATH)
# Optional print statement to show the words ending with the specified suffix
func5_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH)
if FUNC5_SUFFIX:
    print(f"Unique words ending with '{FUNC5_SUFFIX}' from {func5_filename}: {words_ending_with_suffix_from_set}")

# Find words from a set of words starting with a specified prefix and write them to a target file

words_starting_with_prefix_from_set = find_words_starting_with_from_set(FUNC5_PREFIX, FUNC5_READ_WORD_SET_FILEPATH, FUNC5_WRITE_PREFIX_FILEPATH)
# Optional print statement to show the words starting with the specified prefix
if FUNC5_PREFIX:
    print(f"Unique words starting with '{FUNC5_PREFIX}' from {func5_filename}: {words_starting_with_prefix_from_set}")

# 6. Test find_words_ending_with_from_file function (find words from target file that end with the variable suffix) #
# File format should be word: frequency                                                                             #
#####################################################################################################################

# Returns a list of words ending with the specified suffix from the target file and writes them and their frequencies to the specified file.
# Boolean argument print_frequencies to either print the word frequencies list or not
words_ending_with_suffix_from_file = find_words_ending_with_from_file(FUNC6_SUFFIX, FUNC6_READ_FILEPATH, FUNC6_WRITE_FILEPATH, FUNC6_PRINT)
# If any words were found, print them

func6_filename = os.path.basename(FUNC6_READ_FILEPATH)
if FUNC6_SUFFIX:
    print(f"Words ending with '{FUNC6_SUFFIX}' from {func6_filename}: {words_ending_with_suffix_from_file}")

# 7. Updating the set of unique words with the new words from the latest run of the script #
############################################################################################

# Make a set of unique words from word_frequencies (created in step 4 with list_words_by_frequency) text file which is the result of the latest run of the script.
new_unique_words = set(word for word, _ in word_frequencies)
# Read removed_words.txt and remove any words that are in the removed words set from the new_unique_words set
removed_words_path = os.path.join(r'C:\Users\hoffi\Documents\GitHub\2025\practice1', 'removed_words.txt')

try:
    with open(removed_words_path, 'r') as file:
        removed_words = ast.literal_eval(file.read())
except FileNotFoundError:
    removed_words = set()

# Optional warning message if a word that is in removed_words.txt is attempted to be added
warn_if_removed_word_added = True  # Set to True to enable warning messages

if warn_if_removed_word_added:
    for word in new_unique_words:
        if word in removed_words:
            print(f"Warning: The word '{word}' is in removed_words.txt, not added.")
# Remove any words that are in the removed words set from the new_unique_words set
new_unique_words = new_unique_words - removed_words


# Add the new unique words to the existing set of unique words
combined_unique_words = unique_words.union(new_unique_words)
# Check if there are any new words added to the set of unique words
new_words_added = new_unique_words - unique_words

# Write the latest new unique words to a separate file for further inspection
if new_words_added:
    with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\newest_unique_words.txt', 'w') as file:
        for word in new_words_added:
            file.write(f"{word}\n")
    print(f"Updated newest_unique_words.txt")

# Update the unique words file with the combined set of unique words
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt', 'w') as file:
    # repr: Return a string containing a printable representation of an object
    file.write(repr(combined_unique_words))

# If new words were added, print them
if new_words_added:
    print(f"New words added: {', '.join(new_words_added)}")
else:
    print("No new words added.")

# Print the total number of unique words
unique_word_count = len(combined_unique_words)
print(f"Unique words.txt word count: {unique_word_count}")

# 8. Testing the find_next_word_after function with find_words_after function #
###################################################################################
# Check what word(s) come after the variable FIND_WORDS_AFTER unless it's empty
if FIND_WORDS_AFTER:
    next_words_after_target = find_words_after(input_string, FIND_WORDS_AFTER)  # Input string is formed earlier in the script (3. Read a string from a file...)
    if next_words_after_target:
        print(f"Words after '{FIND_WORDS_AFTER}': {next_words_after_target}")
    else:
        print(f"No words found after '{FIND_WORDS_AFTER}'")

# 9. Find sentences from a file (FUNC9_READ_FILEPATH=INPUT_STRING_FILEPATH, it's usually location of input.txt) that contain a specified word #
###############################################################################################################################################
# Valid words to search should be in the following file but it could change (check step 3 and 4): "C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt"
sentences_with_word = find_sentences_with_word(FUNC9_WORD_TO_SEARCH, FUNC9_READ_FILEPATH)

# Print the sentences containing the word
func9_filepath = os.path.basename(FUNC9_READ_FILEPATH)
if sentences_with_word:
    print(f"Sentences containing the word '{FUNC9_WORD_TO_SEARCH}' in {func9_filepath}:")
    for sentence in sentences_with_word:
        print(f"- {sentence}")
else:
    print(f"No sentences found containing the word '{FUNC9_WORD_TO_SEARCH}' in {func9_filepath}")
    
# Provide these variables to helper_functions.py

helper_functions.FUNC1_WORD_LENGTH = FUNC1_WORD_LENGTH
helper_functions.FUNC1_READ_FILENAME = FUNC1_READ_FILENAME
helper_functions.FUNC2_ADD_TO_REMOVED_WORDS = FUNC2_ADD_TO_REMOVED_WORDS
helper_functions.INPUT_STRING_FILEPATH = INPUT_STRING_FILEPATH
helper_functions.FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH = FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH
helper_functions.FUNC4_READ_UNIQUE_WORDS_FILEPATH = FUNC4_READ_UNIQUE_WORDS_FILEPATH
helper_functions.FUNC5_SUFFIX = FUNC5_SUFFIX
helper_functions.FUNC5_PREFIX = FUNC5_PREFIX
helper_functions.FUNC5_READ_WORD_SET_FILEPATH = FUNC5_READ_WORD_SET_FILEPATH
helper_functions.FUNC5_WRITE_FILEPATH = FUNC5_WRITE_FILEPATH
helper_functions.FUNC5_WRITE_PREFIX_FILEPATH = FUNC5_WRITE_PREFIX_FILEPATH
helper_functions.FUNC6_SUFFIX = FUNC6_SUFFIX
helper_functions.FUNC6_READ_FILEPATH = FUNC6_READ_FILEPATH
helper_functions.FUNC6_WRITE_FILEPATH = FUNC6_WRITE_FILEPATH
helper_functions.FUNC6_PRINT = FUNC6_PRINT
helper_functions.FIND_WORDS_AFTER = FIND_WORDS_AFTER
helper_functions.FUNC9_READ_FILEPATH = FUNC9_READ_FILEPATH
helper_functions.FUNC9_WORD_TO_SEARCH = FUNC9_WORD_TO_SEARCH