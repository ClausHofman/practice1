from helper_functions import count_whitespaces_and_newlines, count_words, find_next_word_after, list_words_by_frequency, find_words_ending_with_from_file
import ast
import os

def read_input_string(filename):
    file_path = os.path.join(r'C:\Users\hoffi\Documents\GitHub\2025\practice1', filename)
    with open(file_path, 'r') as file:
        return file.read()

# Read input string
input_string = read_input_string('input.txt')

# Return a tuple of whitespace count and newline count
whitespace_count, newline_count = count_whitespaces_and_newlines(input_string)
word_count = count_words(input_string)

print(f"Whitespace count: {whitespace_count}")
print(f"Newline count: {newline_count}")
print(f"Word count: {word_count}")

# Write word frequencies from input.txt to a file
word_frequencies = list_words_by_frequency(input_string)
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt', 'w') as file:
    for word, frequency in word_frequencies:
        file.write(f"{word}: {frequency}\n")

try:
    with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt', 'r') as file:
        # Read the set of unique words from the file
        # Use ast.literal_eval to safely evaluate the string as a Python literal
        unique_words = ast.literal_eval(file.read())
except FileNotFoundError:
    unique_words = set()

def find_words_ending_with_from_set(suffix, unique_words_filename, target_filename):
    unique_words_path = os.path.join(r'C:\Users\hoffi\Documents\GitHub\2025\practice1', unique_words_filename)
    target_file_path = os.path.join(r'C:\Users\hoffi\Documents\GitHub\2025\practice1', target_filename)
    
    try:
        with open(unique_words_path, 'r') as file:
            # Use ast.literal_eval to safely evaluate and convert the string to a Python set
            unique_words = ast.literal_eval(file.read())
    except FileNotFoundError:
        print(f"File not found: {unique_words_path}")
        return []
    
    # List comprehension to return words that end with the specified suffix
    words_ending_with_suffix = [word for word in unique_words if word.endswith(suffix)]
    
    # Write the words ending with the specified suffix to the target file
    with open(target_file_path, 'w') as target_file:
        for word in words_ending_with_suffix:
            target_file.write(f"{word}\n")
    
    return words_ending_with_suffix

# Test find_words_ending_with_from_set function #
#################################################
# Characters to find words ending with
suffix = 'at'
# Should contain a Python set of unique words
source_file = 'unique_words.txt'
# For forming the target filename
filename_base = source_file.rsplit('.', 1)[0]
# Construct the target filename
target_filename = f'{filename_base}_ending_with_{suffix}.txt'
words_ending_with_suffix_from_set = find_words_ending_with_from_set(suffix, source_file, target_filename)
# Optional print statement to show the words ending with the specified suffix
print(f"Unique words ending with '{suffix}' from {source_file}: {words_ending_with_suffix_from_set}")

# Test find_words_ending_with_from_file function (find words from target file that end with the variable suffix) #
##################################################################################################################
suffix = 'ce'
# Source file containing word frequencies in the format word: frequency
frequency_file = 'word_frequencies.txt'
# Returns a list of words ending with the specified suffix from the target file and writes them and their frequencies to the specified file
words_ending_with_suffix_from_file = find_words_ending_with_from_file(suffix, frequency_file, f'ending_with_{suffix}_from_{frequency_file}')
# If any words were found, print them
print(f"Words ending with '{suffix}' from {frequency_file}: {words_ending_with_suffix_from_file}")

# Updating the set of unique words with the new words from the latest run of the script #
#######################################################################################
# Make a set of unique words from word_frequencies text file which is the result of the latest run of the script
new_unique_words = set(word for word, _ in word_frequencies)
# Attempt to add the new unique words to the existing set of unique words
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

# Find the next word after a target word
test_argument = "what"
next_words_after_target = find_next_word_after(input_string, test_argument)
print(f"Words after '{test_argument}': {next_words_after_target}")
