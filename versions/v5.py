import string
from collections import Counter

def count_whitespaces_and_newlines(input_string):
    whitespace_count = input_string.count(' ')
    newline_count = input_string.count('\n')
    return whitespace_count, newline_count

def first_word_length(input_string):
    alphabet = list(string.ascii_letters)
    first_word = ""
    for char in input_string:
        if char not in alphabet:
            break
        first_word += char
    return len(first_word)

def count_words(input_string, contractions=None):
    if contractions is None:
        contractions = []
    alphabet = set(string.ascii_letters)
    word_count = 0
    current_word = []

    for char in input_string:
        if char in alphabet or (char == "'" and current_word):
            current_word.append(char)
        else:
            if current_word:
                word = ''.join(current_word).lower()
                if word in contractions or all(c in alphabet or c == "'" for c in word):
                    word_count += 1
                current_word = []

    if current_word:
        word = ''.join(current_word).lower()
        if word in contractions or all(c in alphabet or c == "'" for c in word):
            word_count += 1

    return word_count

# Example usage:
example_string = "This is a test string.\nWith a newline."
# Read input string from a file
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\input.txt', 'r') as file:
    input_string = file.read()

whitespace_count, newline_count = count_whitespaces_and_newlines(input_string)
first_word_len = first_word_length(input_string)

try:
    with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\english_contractions.txt', 'r') as file:
        contractions = eval(file.read())
except FileNotFoundError:
    contractions = []

lowercase_contractions = [contraction.lower() for contraction in contractions]

print(lowercase_contractions)

word_count = count_words(input_string, lowercase_contractions)

print(f"Whitespace count: {whitespace_count}")
print(f"Newline count: {newline_count}")
print(f"Length of the first word: {first_word_len}")
print(f"Word count: {word_count}")

def find_next_word_after(input_string, target_word):
    words = input_string.split()
    result = []
    for i in range(len(words) - 1):
        if words[i].lower() == target_word.lower():
            result.append(words[i + 1])
    return result

test_argument = "what"
next_words_after_target = find_next_word_after(input_string, test_argument)

def count_unique_words(input_string):
    alphabet = set(string.ascii_letters)
    words = set()
    current_word = []

    for char in input_string:
        if char in alphabet or char == "'":
            current_word.append(char)
        else:
            if current_word:
                words.add(''.join(current_word).lower())
                current_word = []

    if current_word:
        words.add(''.join(current_word).lower())

    return len(words)

def count_total_words(input_string):
    alphabet = set(string.ascii_letters)
    word_count = 0
    current_word = []

    for char in input_string:
        if char in alphabet or char == "'":
            current_word.append(char)
        else:
            if current_word:
                word_count += 1
                current_word = []

    if current_word:
        word_count += 1

    return word_count

def list_words_by_frequency(input_string):
    alphabet = set(string.ascii_letters)
    words = []
    current_word = []

    for char in input_string:
        if char in alphabet or char == "'":
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

unique_word_count = count_unique_words(input_string)
total_word_count = count_total_words(input_string)
print(f"Unique word count: {unique_word_count}")
print(f"Total word count: {total_word_count}")

word_frequencies = list_words_by_frequency(input_string)
with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies.txt', 'w') as file:
    for word, frequency in word_frequencies:
        file.write(f"{word}: {frequency}\n")

try:
    with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt', 'r') as file:
        unique_words = eval(file.read())
except FileNotFoundError:
    unique_words = set()

new_unique_words = set(word for word, _ in word_frequencies)
combined_unique_words = unique_words.union(new_unique_words)
new_words_added = new_unique_words - unique_words

with open(r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt', 'w') as file:
    file.write(repr(combined_unique_words))

if new_words_added:
    print(f"New words added: {', '.join(new_words_added)}")
else:
    print("No new words added.")

test_argument = "what"
next_words_after_target = find_next_word_after(input_string, test_argument)
print(f"Words after '{test_argument}': {next_words_after_target}")
