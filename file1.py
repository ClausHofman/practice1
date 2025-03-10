from helper_functions import (count_whitespaces_and_newlines, count_words, find_words_after, list_words_by_frequency, find_words_ending_with_from_file, 
                              remove_words_from_unique_words_set, list_words_of_length, read_input_string, find_words_ending_with_from_set, find_words_starting_with_from_set, 
                              find_sentences_with_word, find_words_in_frequencies, find_words_starting_with_from_file)
from helper_configs import Config, config_a
import logging
import ast
import os

###################################################################################################################################################################
# import nltk
# from nltk.corpus import words
# from nltk.stem import WordNetLemmatizer
# import enchant
# nltk.download('words')
# nltk.download('wordnet')

# Initialize the lemmatizer
# lemmatizer = WordNetLemmatizer()
# # Set of English words from nltk words corpus
# english_words = set(words.words())
# english_dict = enchant.Dict("en_US")

# def identify_non_english_words(word_list):
#     non_english_words = []
#     for word in word_list:
#         # Lemmatize the word
#         lemma = lemmatizer.lemmatize(word.lower())
#         if not english_dict.check(lemma):
#             non_english_words.append(word)
#     return non_english_words
###################################################################################################################################################################

# Configure logging #
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#######################################################################
# !!! helper_configs.py to modify / make different configurations !!! #
#######################################################################
# Pick a configuration
CONFIGS = Config(config_a)

# 1. Test list_words_of_length function #
#########################################

# Return words of the specified length from the unique words set
words_of_length = list_words_of_length(CONFIGS.FUNC1_ACTIVE, CONFIGS.FUNC1_WORD_LENGTH, CONFIGS.FUNC1_READ_FILENAME)

# Write the words of the specified length to a file for easier inspection
with open(f'unique_words_of_length_{CONFIGS.FUNC1_WORD_LENGTH}.txt', 'w', encoding='utf-8') as file:
    for word in words_of_length:
        file.write(f"{word}\n")

# Print the words of the specified length
print(f"Words of length {CONFIGS.FUNC1_WORD_LENGTH} in {CONFIGS.FUNC1_READ_FILENAME}:")
for word in words_of_length:
    print(f"- {word}")

# 2. Test remove_words_from_unique_words_set function which removes words from the unique words set and adds them to a separate set (file) #
#####################################################################################################################################

words_to_remove = CONFIGS.FUNC2_ADD_TO_REMOVED_WORDS  # Replace with the words you want to remove
remove_words_from_unique_words_set(words_to_remove, 'unique_words.txt', 'removed_words.txt')

# 3. Read a string from a file and print some additional information about the input string with the help of count_whitespaces_and_newlines and count_words functions #
#######################################################################################################################################################################
# The string that is used in a few functions in this script. Needs INPUT_STRING_FILEPATH to be set to a valid file path
input_string = read_input_string(CONFIGS.INPUT_STRING_FILEPATH)

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
with open(CONFIGS.FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH, 'w', encoding='utf-8') as file:
    for word, frequency in word_frequencies:
        file.write(f"{word}: {frequency}\n")

try:
    with open(CONFIGS.FUNC4_READ_UNIQUE_WORDS_FILEPATH, 'r', encoding='utf-8') as file:
        # Read the set of unique words from the file
        # Use ast.literal_eval to safely evaluate the string as a Python literal
        unique_words = ast.literal_eval(file.read())
except FileNotFoundError:
    unique_words = set()

# Check if there are any non-English words in the unique words set with nltk words corpus
# non_english_words = identify_non_english_words(unique_words)
# print(f"Non-English words in the unique words set: {non_english_words}")

# 5. Find words from a set of words ending with a specified suffix/prefix and write them to a target file using find_words_ending_with_from_set function #
###################################################################################################################################################

words_ending_with_suffix_from_set = find_words_ending_with_from_set(CONFIGS.FUNC5_SUFFIX, CONFIGS.FUNC5_READ_WORD_SET_FILEPATH, CONFIGS.FUNC5_WRITE_FILEPATH)
# Optional print statement to show the words ending with the specified suffix
func5_filename = os.path.basename(CONFIGS.FUNC5_READ_WORD_SET_FILEPATH)
if CONFIGS.FUNC5_SUFFIX:
    print(f"Unique words ending with '{CONFIGS.FUNC5_SUFFIX}' from {func5_filename}: {words_ending_with_suffix_from_set}")

# Find words from a set of words starting with a specified prefix and write them to a target file

words_starting_with_prefix_from_set = find_words_starting_with_from_set(CONFIGS.FUNC5_PREFIX, CONFIGS.FUNC5_READ_WORD_SET_FILEPATH, CONFIGS.FUNC5_WRITE_PREFIX_FILEPATH)
# Optional print statement to show the words starting with the specified prefix
if CONFIGS.FUNC5_PREFIX:
    print(f"Unique words starting with '{CONFIGS.FUNC5_PREFIX}' from {func5_filename}: {words_starting_with_prefix_from_set}")

# 6a. find_words_ending_with_from_file function (find words from target file that end with the variable suffix) #
# File that's being read format should be word: frequency                                                                             #
#####################################################################################################################

# Returns a list of words ending with the specified suffix from the target file and writes them and their frequencies to the specified file.
words_ending_with_suffix_from_file = find_words_ending_with_from_file(CONFIGS.FIND_WORDS_FROM_FILE_SUFFIX,
                                                                      CONFIGS.find_words_ending_with_from_file_READ_FILEPATH,
                                                                      CONFIGS.find_words_ending_with_from_file_WRITE_PATH,
                                                                      CONFIGS.find_words_ending_with_from_file_PRINT)

# func6_filename = os.path.basename(CONFIGS.find_words_ending_with_from_file_READ_FILEPATH)
# if CONFIGS.FIND_WORDS_FROM_FILE_SUFFIX:
    # print(f"Words ending with '{CONFIGS.FIND_WORDS_FROM_FILE_SUFFIX}' from {func6_filename}: {words_ending_with_suffix_from_file}")

# 6b. find_words_starting_with_from_file function (find words from target file that begin with the variable prefix) #
# File that's being read format should be word: frequency                                                                             #
#####################################################################################################################

# Returns a list of words starting with the specified prefix from the target file and writes them and their frequencies to the specified file.
words_starting_with_prefix_from_file = find_words_starting_with_from_file(CONFIGS.FIND_WORDS_FROM_FILE_PREFIX,
                                                                      CONFIGS.find_words_starting_with_from_file_READ_FILEPATH,
                                                                      CONFIGS.find_words_starting_with_from_file_WRITE_PATH,
                                                                      CONFIGS.find_words_starting_with_from_file_PRINT)


# 7. Updating the set of unique words with the new words from the latest run of the script #
############################################################################################

if CONFIGS.UPDATE_UNIQUE_WORDS_FILE:
    # Make a set of unique words from word_frequencies (created in step 4 with list_words_by_frequency) text file which is the result of the latest run of the script.
    new_unique_words = set(word for word, _ in word_frequencies)
    # Read removed_words.txt and remove any words that are in the removed words set from the new_unique_words set
    removed_words_path = os.path.join(r'C:\Users\hoffi\Documents\GitHub\2025\practice1', 'removed_words.txt') # Hardcoded path, but unlikely to change

    try:
        with open(removed_words_path, 'r', encoding='utf-8') as file:
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
        with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\newest_unique_words.txt', 'w', encoding='utf-8') as file: # Hardcoded path, but unlikely to change
            for word in new_words_added:
                file.write(f"{word}\n")
        print(f"Updated newest_unique_words.txt")

    # Update the unique words file with the combined set of unique words
    with open(CONFIGS.UNIQUE_WORDS_PATH, 'w', encoding='utf-8') as file:
        # repr: Return a string containing a printable representation of an object
        file.write(repr(combined_unique_words))

    # If new words were added, print them
    if new_words_added:
        print(f"New words added: {', '.join(new_words_added)}")
    else:
        print("No new words added.")

    # Print the total number of unique words
    unique_word_count = len(combined_unique_words)
    print(f"{CONFIGS.UNIQUE_WORDS_FILENAME} word count: {unique_word_count}")
else:
    pass

# 8. Testing the find_next_word_after function with find_words_after function #
###################################################################################
# Check what word(s) come after the variable FIND_WORDS_AFTER unless it's empty
if CONFIGS.FIND_WORDS_AFTER:
    next_words_after_target = find_words_after(input_string, CONFIGS.FIND_WORDS_AFTER)  # Input string is formed earlier in the script (3. Read a string from a file...)
    if next_words_after_target:
        print(f"Words after '{CONFIGS.FIND_WORDS_AFTER}': {next_words_after_target}")
    else:
        print(f"No words found after '{CONFIGS.FIND_WORDS_AFTER}'")

# 9. Find sentences from a file (FUNC9_READ_FILEPATH=INPUT_STRING_FILEPATH, it's usually location of input.txt) that contain a specified word #
###############################################################################################################################################
# Valid words to search should be in the following file but it could change (check step 3 and 4): "C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt"

if not CONFIGS.FUNC9_WORD_TO_SEARCH:
    pass
else:
    sentences_with_word = find_sentences_with_word(CONFIGS.FUNC9_WORD_TO_SEARCH, CONFIGS.FUNC9_READ_FILEPATH, CONFIGS.DETERMINE_SENTENCES_MODE, CONFIGS.SENTENCE_SEARCH_MODE, CONFIGS.FUNC9_CASE_INSENSITIVE, CONFIGS.FUNC9_PROX_WORD, CONFIGS.FUNC9_PROX_DIST)

    # Print the sentences containing the word
    func9_filepath = os.path.basename(CONFIGS.FUNC9_READ_FILEPATH)
    if sentences_with_word:
        print(f"Sentences containing the word '{CONFIGS.FUNC9_WORD_TO_SEARCH}' in {func9_filepath}:")
        for item in sentences_with_word:
            if CONFIGS.DETERMINE_SENTENCES_MODE == 'line':
                # unpack the tuple
                line_number, sentence = item
                print(f"- Line {line_number}: {sentence}")
            else:
                print(f"- {item}")

# 10. Find and display searched word or words from a word frequencies file #
############################################################################

find_words_in_frequencies(CONFIGS.FUNC10_ACTIVE, CONFIGS.FUNC10_WORDS_TO_SEARCH, CONFIGS.FUNC10_READ_FILEPATH, CONFIGS.FUNC10_SORTING, CONFIGS.FIND_WORDS_FROM_FREQUENCIES_FILE_MODE, CONFIGS.FUNC10_WORD_FREQUENCY, CONFIGS.FUNC10_WRITE_FILEPATH, CONFIGS.FUNC10_PRINT)
