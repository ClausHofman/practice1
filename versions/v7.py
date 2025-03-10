from helper_functions import count_whitespaces_and_newlines, count_words, find_next_word_after, list_words_by_frequency
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

def find_words_ending_with(suffix, word_frequencies):
    # This list comprehension iterates over each tuple (word, _) in the word_frequencies list.
    # For each word, it removes any trailing colons (:) using rstrip(':').
    # It then checks if the modified word ends with the specified suffix.
    # If it does, the modified word is included in the resulting list.
    return [word.rstrip(':') for word, _ in word_frequencies if word.rstrip(':').endswith(suffix)]

def find_words_ending_with_from_file(suffix, filename):
    file_path = os.path.join(r'C:\Users\hoffi\Documents\GitHub\2025\practice1', filename)
    word_frequencies = []
    with open(file_path, 'r') as file:
        for line in file:
            word, frequency = line.split(':')
            word_frequencies.append((word.strip(), int(frequency.strip())))
    return [word for word, _ in word_frequencies if word.endswith(suffix)]

# Example usage of find_words_ending_with_from_file (find words from target file that end with the variable suffix)
suffix = 'ing'
words_ending_with_suffix_from_file = find_words_ending_with_from_file(suffix, 'word_frequencies2.txt')
print(f"Words ending with '{suffix}' from file: {words_ending_with_suffix_from_file}")

# Make a set of unique words from word_frequencies text file which is the result of the latest run of the script
new_unique_words = set(word for word, _ in word_frequencies)
# Attempt to add the new unique words to the existing set of unique words
combined_unique_words = unique_words.union(new_unique_words)
# Check if there are any new words added to the set of unique words
new_words_added = new_unique_words - unique_words

# Update the unique words file with the combined set of unique words
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt', 'w') as file:
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
test_argument = "holy"
next_words_after_target = find_next_word_after(input_string, test_argument)
print(f"Words after '{test_argument}': {next_words_after_target}")
