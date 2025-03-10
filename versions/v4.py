import string
from collections import Counter

def count_whitespaces_and_newlines(input_string):
    """
    Counts the number of whitespace characters and newline characters in the input string.

    Args:
    input_string (str): The string to be analyzed.

    Returns:
    tuple: A tuple containing the count of whitespace characters and newline characters.
    """
    whitespace_count = input_string.count(' ')
    newline_count = input_string.count('\n')
    return whitespace_count, newline_count

def first_word_length(input_string):
    """
    Finds the length of the first word in the input string until a non-letter character is encountered.

    Args:
    input_string (str): The string to be analyzed.

    Returns:
    int: The length of the first word.
    """
    alphabet = list(string.ascii_letters)
    first_word = ""
    for char in input_string:
        if char not in alphabet:
            break
        first_word += char

    return len(first_word)

def count_words(input_string):
    """
    Counts the number of words in the input string. A word is defined as a sequence of letters.

    Args:
    input_string (str): The string to be analyzed.

    Returns:
    int: The number of words in the input string.
    """
    alphabet = set(string.ascii_letters)
    in_word = False
    word_count = 0

    for char in input_string:
        if char in alphabet:
            if not in_word:
                word_count += 1
                in_word = True
        else:
            in_word = False

    return word_count

# Example usage:
example_string = "This is a test string.\nWith a newline."
# Read input string from a file
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\input.txt', 'r') as file:
    input_string = file.read()

whitespace_count, newline_count = count_whitespaces_and_newlines(input_string)
first_word_len = first_word_length(input_string)
word_count = count_words(input_string)

print(f"Whitespace count: {whitespace_count}")
print(f"Newline count: {newline_count}")
print(f"Length of the first word: {first_word_len}")
# Check if the input string contains a specific word and store the next word
def find_next_word_after(input_string, target_word):
    """
    Finds the word that comes after the target word in the input string.

    Args:
    input_string (str): The string to be analyzed.
    target_word (str): The word to search for.

    Returns:
    list: A list containing the word that comes after the target word, if found.
    """
    words = input_string.split()
    result = []
    for i in range(len(words) - 1):
        if words[i].lower() == target_word.lower():
            result.append(words[i + 1])
    return result

# Example usage:
test_argument = "what"
next_words_after_target = find_next_word_after(input_string, test_argument)
def count_unique_words(input_string):
    """
    Counts the number of unique words in the input string. A word is defined as a sequence of letters.

    Args:
    input_string (str): The string to be analyzed.

    Returns:
    int: The number of unique words in the input string.
    """
    alphabet = set(string.ascii_letters)
    words = set()
    current_word = []

    for char in input_string:
        if char in alphabet:
            current_word.append(char)
        else:
            if current_word:
                words.add(''.join(current_word).lower())
                current_word = []

    if current_word:
        words.add(''.join(current_word).lower())

    return len(words)

def count_total_words(input_string):
    """
    Counts the total number of words in the input string. A word is defined as a sequence of letters.

    Args:
    input_string (str): The string to be analyzed.

    Returns:
    int: The total number of words in the input string.
    """
    alphabet = set(string.ascii_letters)
    word_count = 0
    current_word = []

    for char in input_string:
        if char in alphabet:
            current_word.append(char)
        else:
            if current_word:
                word_count += 1
                current_word = []

    if current_word:
        word_count += 1

    return word_count

def list_words_by_frequency(input_string):
    """
    Lists all words in the input string from most common to least common.

    Args:
    input_string (str): The string to be analyzed.

    Returns:
    list: A list of tuples where each tuple contains a word and its frequency, sorted by frequency.
    """
    alphabet = set(string.ascii_letters)
    words = []
    current_word = []

    for char in input_string:
        if char in alphabet:
            current_word.append(char)
        else:
            if current_word:
                words.append(''.join(current_word).lower())
                current_word = []

    if current_word:
        words.append(''.join(current_word).lower())

    word_counts = Counter(words)
    sorted_word_counts = word_counts.most_common()

    return sorted_word_counts

# Example usage:
unique_word_count = count_unique_words(input_string)
total_word_count = count_total_words(input_string)
print(f"Unique word count: {unique_word_count}")
print(f"Total word count: {total_word_count}")

# List words by frequency and write to a file
word_frequencies = list_words_by_frequency(input_string)
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies.txt', 'w') as file:
    for word, frequency in word_frequencies:
        file.write(f"{word}: {frequency}\n")

# Read unique words from the file
try:
    with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt', 'r') as file:
        unique_words = eval(file.read())
except FileNotFoundError:
    unique_words = set()

# Combine the old set with the new set of unique words
new_unique_words = set(word for word, _ in word_frequencies)
combined_unique_words = unique_words.union(new_unique_words)

# Determine the new words added
new_words_added = new_unique_words - unique_words

# Write the combined set of unique words back to the file
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt', 'w') as file:
    file.write(repr(combined_unique_words))

# Inform if new words were added
if new_words_added:
    print(f"New words added: {', '.join(new_words_added)}")
else:
    print("No new words added.")

# Check if the input string contains a specific word and store the next word
def find_next_word_after(input_string, target_word):
    """
    Finds the word that comes after the target word in the input string.

    Args:
    input_string (str): The string to be analyzed.
    target_word (str): The word to search for.

    Returns:
    list: A list containing the word that comes after the target word, if found.
    """
    words = input_string.split()
    result = []
    for i in range(len(words) - 1):
        if words[i].lower() == target_word.lower():
            result.append(words[i + 1])
    return result

# Example usage:
test_argument = "what"
next_words_after_target = find_next_word_after(input_string, test_argument)
print(f"Words after '{test_argument}': {next_words_after_target}")