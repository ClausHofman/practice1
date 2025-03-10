from helper_functions import (count_whitespaces_and_newlines, count_words, find_words_after, list_words_by_frequency, find_words_ending_with_from_file, 
                              remove_words_from_unique_words_set, list_words_of_length, read_input_string, find_words_ending_with_from_set, find_sentences_with_word)
import ast
import os

# 1. Variables for function list_words_of_length
FUNC1_WORD_LENGTH = 1
FUNC1_READ_FILENAME = 'unique_words.txt' # Should contain a python set of unique words
# 2. Variable for function remove_words_from_unique_words_set. Add words as neccessary
FUNC2_ADD_TO_REMOVED_WORDS = [""]
# 3. Variable for function read_input_string
INPUT_STRING_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\input.txt"
# 4. Variables for function list_words_by_frequency
FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt"
FUNC4_READ_UNIQUE_WORDS_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt"
# 5. Variables for function find_words_ending_with_from_set
FUNC5_SUFFIX = 'at'
FUNC5_READ_WORD_SET_FILEPATH = r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt'
func5_variable_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH).rsplit('.', 1)[0] # Split from FUNC5_READ_WORD_SET_FILEPATH and remove the file extension
FUNC5_WRITE_FILEPATH = fr'C:\Users\hoffi\Documents\GitHub\2025\practice1\from_{func5_variable_filename}_ending_with_{FUNC5_SUFFIX}.txt'
# 6. Variables for function find_words_ending_with_from_file
FUNC6_SUFFIX = 'ce'
FUNC6_READ_FILEPATH = FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH
FUNC6_WRITE_FILEPATH = f'ending_with_{FUNC6_SUFFIX}_from_{os.path.basename(FUNC6_READ_FILEPATH)}'
# Variable for function find_next_word_after
# 8. Variable for function find_next_word_after
FIND_WORDS_AFTER = 'a'
# 9. Variable for function find_sentences_with_word
FUNC9_READ_FILEPATH = INPUT_STRING_FILEPATH
FUNC9_WORD_TO_USE = 'watermelon'

# 1. Test list_words_of_length function #
#########################################

# Return words of the specified length from the unique words set
words_of_length = list_words_of_length(FUNC1_WORD_LENGTH, FUNC1_READ_FILENAME)

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

input_string = read_input_string(INPUT_STRING_FILEPATH)

# Return a tuple of whitespace count and newline count, not sure if this is useful for anything
whitespace_count, newline_count = count_whitespaces_and_newlines(input_string)
# Everything won't probably be a word but gives some idea of the word count, could try to invent logic to make the number more accurate
word_count = count_words(input_string)

# Just some information about the input string
print(f"Whitespace count: {whitespace_count}")
print(f"Newline count: {newline_count}")
print(f"Word count: {word_count}")

# 4. Write word frequencies from INPUT_STRING_FILEPATH to a file and also read and make a set from unique_words.txt #
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

# 5. Find words from a set of words ending with a specified suffix and write them to a target file using find_words_ending_with_from_set function #
###################################################################################################################################################

words_ending_with_suffix_from_set = find_words_ending_with_from_set(FUNC5_SUFFIX, FUNC5_READ_WORD_SET_FILEPATH, FUNC5_WRITE_FILEPATH)
# Optional print statement to show the words ending with the specified suffix
func5_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH)
print(f"Unique words ending with '{FUNC5_SUFFIX}' from {func5_filename}: {words_ending_with_suffix_from_set}")

# 6. Test find_words_ending_with_from_file function (find words from target file that end with the variable suffix) #
# File format should be word: frequency                                                                             #
#####################################################################################################################

# Returns a list of words ending with the specified suffix from the target file and writes them and their frequencies to the specified file.
# Boolean argument print_frequencies to either print the word frequencies list or not
words_ending_with_suffix_from_file = find_words_ending_with_from_file(FUNC6_SUFFIX, FUNC6_READ_FILEPATH, FUNC6_WRITE_FILEPATH, True)
# If any words were found, print them

func6_filename = os.path.basename(FUNC6_READ_FILEPATH)
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
# Check what word(s) come after the variable FIND_WORDS_AFTER
next_words_after_target = find_words_after(input_string, FIND_WORDS_AFTER) # Input string is formed earlier in the script (3. Read a string from a file...)
if next_words_after_target:
    print(f"Words after '{FIND_WORDS_AFTER}': {next_words_after_target}")
else:
    print(f"No words found after '{FIND_WORDS_AFTER}'")

# 9. Find sentences containing the specified word, existing words are in FUNC6_WRITE_FILEPATH of the find_words_ending_with_from_file (step 6) function #
#########################################################################################################################################################
# Example usage
word_to_find = FUNC9_WORD_TO_USE  # Replace with the word you want to search for
sentences_with_word = find_sentences_with_word(word_to_find, FUNC9_READ_FILEPATH)

# Print the sentences containing the word
func9_filepath = os.path.basename(FUNC9_READ_FILEPATH)
if sentences_with_word:
    print(f"Sentences containing the word '{word_to_find}' in {func9_filepath}:")
    for sentence in sentences_with_word:
        print(f"- {sentence}")
else:
    print(f"No sentences found containing the word '{word_to_find}' in {func9_filepath}")