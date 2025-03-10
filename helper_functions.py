from collections import Counter
import os
import string
import ast
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 1.
def list_words_of_length(active, length, unique_words_filename):
    if not active:
        return []
    unique_words_path = os.path.join(fr'{os.getcwd()}', unique_words_filename)
    
    try:
        with open(unique_words_path, 'r', encoding='utf-8') as file:
            # Use ast.literal_eval to safely evaluate and convert the string to a Python set
            unique_words = ast.literal_eval(file.read())
    except FileNotFoundError:
        logging.error(f"File not found: {unique_words_path}")
        return []
    
    # List comprehension to return words of the specified length
    words_of_length = sorted([word for word in unique_words if len(word) == length])
    
    return words_of_length

# 2.
def remove_words_from_unique_words_set(words_to_remove, unique_words_filename, removed_words_filename):
    if not all(isinstance(item, str) for item in words_to_remove):
        raise ValueError("Not all elements in the list are strings!")

    unique_words_path = os.path.join(fr'{os.getcwd()}', unique_words_filename)
    removed_words_path = os.path.join(fr'{os.getcwd()}', removed_words_filename)
    
    try:
        with open(unique_words_path, 'r', encoding='utf-8') as file:
            # Use ast.literal_eval to safely evaluate and convert the string to a Python set
            unique_words = ast.literal_eval(file.read())
    except FileNotFoundError:
        logging.error(f"File not found: {unique_words_path}")
        return
    
    removed_words = set()
    
    for word in [word.strip() for word in words_to_remove]:
        if word in unique_words:
            unique_words.remove(word)
            removed_words.add(word)
    
    if not words_to_remove:
        print("No words to remove.")
        return

    if removed_words:
        # Update the unique_words.txt file
        with open(unique_words_path, 'w', encoding='utf-8') as file:
            file.write(repr(unique_words))
            print(f"*** File updated: {unique_words_path} ***")
        
        # Add the removed words to removed_words.txt
        try:
            with open(removed_words_path, 'r', encoding='utf-8') as file:
                existing_removed_words = ast.literal_eval(file.read())
        except FileNotFoundError:
            logging.error(f"File not found: {removed_words_path}")
            existing_removed_words = set()
        
        combined_removed_words = existing_removed_words.union(removed_words)
        
        with open(removed_words_path, 'w', encoding='utf-8') as file:
            file.write(repr(combined_removed_words))
            print(f"*** File updated: {removed_words_path} ***")
        
        print(f"Words {', '.join(removed_words)} removed from {unique_words_filename} and added to {removed_words_filename}.")
    else:
        print(f"No words were removed.")

# 3.
def read_input_string(file_path):
    """Read a string from a file and return it.

    Args:
        file_path (string): Full file path to read from

    Returns:
        string: The contents of the file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 4.
def list_words_by_frequency(input_string):
    alphabet = set(string.ascii_letters)
    words = []
    current_word = []
    consec_apostrophes = 0

    for char in input_string:
        if char in alphabet or char == "'" and consec_apostrophes == 0:
            if char == "'":
                consec_apostrophes += 1
            current_word.append(char)
        elif char == "'" and consec_apostrophes >= 1:
            continue
        else:
            if current_word:
                consec_apostrophes = 0
                words.append(''.join(current_word).lower())
                current_word = []

    if current_word:
        consec_apostrophes = 0
        words.append(''.join(current_word).lower())

    word_counts = Counter(words)
    sorted_word_counts = word_counts.most_common()

    return sorted_word_counts

# 5.
def find_words_ending_with_from_set(suffix, read_word_set_filepath, write_filepath):
    if not suffix:
        print("find_words_ending_with_from_set: Suffix is empty. No operation performed.")
        return []

    try:
        with open(read_word_set_filepath, 'r', encoding='utf-8') as file:
            # Use ast.literal_eval to safely evaluate and convert the string to a Python set
            unique_words = ast.literal_eval(file.read())
    except FileNotFoundError:
        logging.error(f"Invalid path: {read_word_set_filepath}")
        return []

    # List comprehension to return words that end with the specified suffix
    words_ending_with_suffix = [word for word in unique_words if word.endswith(suffix)]

    # Write the words ending with the specified suffix to the target file
    with open(write_filepath, 'w', encoding='utf-8') as file:
        make_line = len(write_filepath)
        extra_length = 14
        for word in words_ending_with_suffix:
            file.write(f"{word}\n")
        print((make_line + extra_length) * "-")
        print("Ran find_words_ending_with_from_set function and created the following file:")
        print(f"File created: {write_filepath}")
        print((make_line + extra_length) * "-")

    return words_ending_with_suffix

def find_words_starting_with_from_set(prefix, read_filepath, write_filepath):
    if not prefix:
        print("find_words_starting_with_from_set: Prefix is empty. No operation performed.")
        return []

    try:
        with open(read_filepath, 'r', encoding='utf-8') as file:
            words_set = ast.literal_eval(file.read())
    except FileNotFoundError:
        logging.error(f"Invalid path: {read_filepath}")
        words_set = set()

    words_starting_with_prefix = [word for word in words_set if word.startswith(prefix)]

    with open(write_filepath, 'w', encoding='utf-8') as file:
        make_line = len(write_filepath)
        extra_length = 14
        for word in words_starting_with_prefix:
            file.write(f"{word}\n")
        print((make_line + extra_length) * "-")
        print("Ran find_words_starting_with_from_set function and created the following file:")
        print(f"File created: {write_filepath}")
        print((make_line + extra_length) * "-")

    return words_starting_with_prefix

# 6.
def find_words_ending_with_from_file(suffix, read_filename, write_target_filename, print_frequencies=True):
    """Provide characters to find words ending with, the source file containing word frequencies, and the target file to write the results to.
    The source file format should be word: frequency on each line. For example: word: 5

    Args:
        suffix (string): Example: 'at'
        read_filename (string): filename.txt
        target_filename (string): filename2.txt
        print_frequencies (bool): If True, print the word frequencies list

    Returns:
        tuple: List of tuples containing words and their frequencies
    """
    if not suffix:
        print("find_words_ending_with_from_file: Suffix is empty. No operation performed.")
        return []

    read_file_path = os.path.join(fr'{os.getcwd()}', read_filename)
    write_target_file_path = os.path.join(fr'{os.getcwd()}', write_target_filename)
    word_frequencies = []
    try:
        with open(read_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Make a tuple of word and frequency by splitting the line at the colon
                    word, frequency = line.split(':')
                    # Append the tuple to the word_frequencies list after stripping whitespace and convert frequency to an integer
                    word_frequencies.append((word.strip(), int(frequency.strip())))
                except ValueError:
                    logging.error(f"Skipping line due to format error: {line.strip()}")
    except FileNotFoundError:
        logging.error(f"File not found: {read_file_path}")
        print(f"File not found: {read_file_path}")
        return []

    # Print list of tuples containing words and their frequencies if print_frequencies is True
    if print_frequencies:
        print(f"Word frequencies: {word_frequencies}")
    
    # List comprehension to return words that end with the specified suffix
    words_ending_with_suffix = [(word, frequency) for word, frequency in word_frequencies if word.endswith(suffix)]
    
    # Write the words ending with the specified suffix and their frequencies to the target file
    with open(write_target_file_path, 'w', encoding='utf-8') as target_file:
        make_line = len(write_target_file_path)
        extra_length = 14
        for word, frequency in words_ending_with_suffix:
            target_file.write(f"{word}: {frequency}\n")
        print((make_line + extra_length) * "-")
        print("Ran find_words_ending_with_from_file function and created the following file:")
        print(f"File created: {write_target_file_path}")
        print((make_line + extra_length) * "-")
    
    return words_ending_with_suffix

def find_words_starting_with_from_file(prefix, read_filename, write_target_filename, print_frequencies=True):
    """Provide characters to find words ending with, the source file containing word frequencies, and the target file to write the results to.
    The source file format should be word: frequency on each line. For example: word: 5

    Args:
        prefix (string): Example: 'an'
        read_filename (string): filename.txt
        target_filename (string): filename2.txt
        print_frequencies (bool): If True, print the word frequencies list

    Returns:
        tuple: List of tuples containing words and their frequencies
    """
    if not prefix:
        print("find_words_starting_with_from_file: Prefix is empty. No operation performed.")
        return []

    read_file_path = os.path.join(fr'{os.getcwd()}', read_filename)
    write_target_file_path = os.path.join(fr'{os.getcwd()}', write_target_filename)
    word_frequencies = []
    try:
        with open(read_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Make a tuple of word and frequency by splitting the line at the colon
                    word, frequency = line.split(':')
                    # Append the tuple to the word_frequencies list after stripping whitespace and convert frequency to an integer
                    word_frequencies.append((word.strip(), int(frequency.strip())))
                except ValueError:
                    logging.error(f"Skipping line due to format error: {line.strip()}")
    except FileNotFoundError:
        logging.error(f"File not found: {read_file_path}")
        print(f"File not found: {read_file_path}")
        return []

    # Print list of tuples containing words and their frequencies if print_frequencies is True
    if print_frequencies:
        print(f"Word frequencies: {word_frequencies}")
    
    # List comprehension to return words that start with the specified prefix
    words_starting_with_prefix = [(word, frequency) for word, frequency in word_frequencies if word.startswith(prefix)]
    
    # Write the words ending with the specified suffix and their frequencies to the target file
    with open(write_target_file_path, 'w', encoding='utf-8') as target_file:
        make_line = len(write_target_file_path)
        extra_length = 14
        for word, frequency in words_starting_with_prefix:
            target_file.write(f"{word}: {frequency}\n")
        print((make_line + extra_length) * "-")
        print("Ran find_words_starting_with_from_file function and created the following file:")
        print(f"File created: {write_target_file_path}")
        print((make_line + extra_length) * "-")
    
    return words_starting_with_prefix

# 8.
def find_words_after(input_string, target_word):
    words = input_string.split()
    result = []
    for i in range(len(words) - 1):
        if words[i].lower() == target_word.lower():
            result.append(words[i + 1])
    return result

# 9.
def find_sentences_with_word(word, read_filepath, mode='sentence', search_mode='contains', case_insensitive=False, proximity_word=None, proximity_distance=5):
    """
    Find sentences or words in a specific line that contain the specified word.

    Args:
        word (str): The word to search for.
        read_filepath (str): The file path to read the input string from.
        mode (str): The mode of operation. 'sentence' to find sentences containing the word,
                    'line' to find words in a specific line containing the word.
        search_mode (str): The search mode. 'contains' to find words containing the specified word,
                           'exact' to find exact matches of the word,
                           'prefix' to find words starting with the specified word,
                           'suffix' to find words ending with the specified word,
                           'regex' to use a custom regex pattern,
                           'proximity' to find sentences where the word is within a certain distance of another word,
                           'partial' to find words containing the specified partial string.
        case_insensitive (bool): If True, perform a case-insensitive search.
        proximity_word (str): The word to search for in proximity to the specified word (used in 'proximity' mode).
        proximity_distance (int): The maximum distance (in words) for the proximity search.

    Returns:
        list: A list of sentences or words containing the specified word.
    """
    if not word:
        return []
    
    # Read the input string from the file
    input_string = read_input_string(read_filepath)
    
    if case_insensitive:
        word = word.lower()
        input_string = input_string.lower()
    
    if mode == 'sentence':
        # Split the input string into sentences using common sentence separators
        sentences = re.split(r'[.!?]', input_string)
        
        # Strip leading and trailing whitespace from each sentence
        sentences = [sentence.strip() for sentence in sentences]
        
        if search_mode == 'contains':
            # Find sentences that contain the specified word
            sentences_with_word = [sentence for sentence in sentences if word in sentence]
        elif search_mode == 'exact':
            # Find sentences that contain the exact match of the specified word
            sentences_with_word = [sentence for sentence in sentences if re.search(rf'\b{word}\b', sentence)]
        elif search_mode == 'prefix':
            # Find sentences that contain words starting with the specified word
            sentences_with_word = [sentence for sentence in sentences if re.search(rf'\b{word}\w*\b', sentence)]
        elif search_mode == 'suffix':
            # Find sentences that contain words ending with the specified word
            sentences_with_word = [sentence for sentence in sentences if re.search(rf'\b\w*{word}\b', sentence)]
        elif search_mode == 'regex':
            # Find sentences that match the custom regex pattern
            sentences_with_word = [sentence for sentence in sentences if re.search(word, sentence)]
        elif search_mode == 'proximity' and proximity_word:
            # Find sentences where the word is within a certain distance of another word
            sentences_with_word = []
            for sentence in sentences:
                words = sentence.split()
                for i, w in enumerate(words):
                    if w == word:
                        for j in range(max(0, i - proximity_distance), min(len(words), i + proximity_distance + 1)):
                            if words[j] == proximity_word:
                                sentences_with_word.append(sentence)
                                break
        elif search_mode == 'partial':
            # Find sentences that contain words with the specified partial string
            sentences_with_word = [sentence for sentence in sentences if any(word in w for w in sentence.split())]
        else:
            logging.error(f"Invalid search mode: {search_mode}")
            return []
        
        return sentences_with_word
        
    if mode == 'line':
        # Split the input string into lines
        lines = input_string.split('\n')
        
        # Iterate all lines and store the lines that contain the searched word
        lines_with_word = []
        for line_number, line in enumerate(lines, start=1):
            if search_mode == 'contains' and word in line:
                lines_with_word.append((line_number, line.strip()))
            elif search_mode == 'exact' and re.search(rf'\b{word}\b', line):
                lines_with_word.append((line_number, line.strip()))
            elif search_mode == 'prefix' and re.search(rf'\b{word}\w*\b', line):
                lines_with_word.append((line_number, line.strip()))
            elif search_mode == 'suffix' and re.search(rf'\b\w*{word}\b', line):
                lines_with_word.append((line_number, line.strip()))
            elif search_mode == 'regex' and re.search(word, line):
                lines_with_word.append((line_number, line.strip()))
            elif search_mode == 'proximity' and proximity_word:
                words = line.split()
                for i, w in enumerate(words):
                    if w == word:
                        for j in range(max(0, i - proximity_distance), min(len(words), i + proximity_distance + 1)):
                            if words[j] == proximity_word:
                                lines_with_word.append((line_number, line.strip()))
                                break
            elif search_mode == 'partial' and any(word in w for w in line.split()):
                lines_with_word.append((line_number, line.strip()))
        
        return lines_with_word
        
    else:
        logging.error(f"Invalid mode: {mode}")
        return []

# 10.

import traceback

def find_words_in_frequencies(active, words, frequencies_filepath, sort_by='alphabetical', search_mode='exact', frequency=None, output_filepath=None, print_words=False):
    """
    Find words in the word frequencies file and return a message with the words found.

    Args:
        active (bool): If True, the function is active and will execute. If False, the function will pass.
        words (list): List of words to search for.
        frequencies_filepath (str): Path to the word frequencies file.
        sort_by (str): Sort order for the output message. 'alphabetical' or 'frequency'.
        search_mode (str): Search mode for the words. 'exact' for exact matches, 'partial' for partial matches.
        frequency (int, optional): If specified, list all words that have this frequency.
        output_filepath (str, optional): If specified, write the found words to this file.

    Returns:
        str: Message with the words found.
    """
    if not active:
        logging.info("find_words_in_frequencies function is not enabled.")
        return "find_words_in_frequencies function is not enabled."
    
    # Check if the words list is empty or contains only empty strings
    if not words and frequency is None:
        logging.warning("find_words_in_frequencies: Word search list is empty and no frequency specified!")
        return "find_words_in_frequencies: Word search list is empty and no frequency specified!"
    
    # Verify the file path
    if not os.path.exists(frequencies_filepath):
        logging.error(f"File not found: {frequencies_filepath}")
        return f"File not found: {frequencies_filepath}"

    # Read word frequencies from the file
    word_frequencies = {}
    try:
        with open(frequencies_filepath, 'r', encoding='utf-8') as file:
            for line in file:
                word, freq = line.split(':')
                word_frequencies[word.strip()] = int(freq.strip())
    except FileNotFoundError:
        logging.error(f"File not found: {frequencies_filepath}")
        return f"File not found: {frequencies_filepath}"
    except ValueError:
        logging.error(f"Error reading file: {frequencies_filepath}")
        traceback.print_exc()
        return f"Error reading file: {frequencies_filepath}"
    except UnicodeDecodeError as e:
        logging.error(f"Error decoding file: {e}")
        traceback.print_exc()
        return f"Error decoding file: {e}"

    print(f"TESTING: {words}")

    try:
        # Find words in the word frequencies
        found_words = {}
        searched_words = {}
        if frequency is not None:
            found_words = {word: freq for word, freq in word_frequencies.items() if freq == frequency}
        if search_mode == 'exact':
            searched_words = {word: word_frequencies[word] for word in words if word in word_frequencies}
        elif search_mode == 'partial':
            for word in words:
                for key in word_frequencies:
                    if word in key:
                        searched_words[key] = word_frequencies[key]
        else:
            raise ValueError("Invalid search mode. Use 'exact' or 'partial'.")
        
        print(f"TESTING2: {searched_words}")

        # Sort the found words
        if sort_by == 'alphabetical':
            sorted_words = sorted(found_words.keys())
        elif sort_by == 'frequency':
            sorted_words = sorted(found_words.keys(), key=lambda x: found_words[x], reverse=True)
        else:
            raise ValueError("Invalid sort order. Use 'alphabetical' or 'frequency'.")

        # Create the message
        if not sorted_words:
            logging.info("No words found.")
            return "No words found."

        message = "Words found:\n"
        for word in sorted_words:
            message += f"{word}: {found_words[word]}\n"
        if print_words:
            logging.info(message.strip())

        # Write the found words to a file if frequency is specified and output_filepath is provided
        if frequency is not None and output_filepath:
            with open(output_filepath, 'w', encoding='utf-8') as file:
                for word in sorted(found_words.keys(), key=len):
                    file.write(f"{word}: {found_words[word]}\n")
            logging.info(f"Words with frequency {frequency} written to {output_filepath}")

        return message.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        return f"An error occurred: {e}"

def count_whitespaces_and_newlines(input_string):
    whitespace_count = input_string.count(' ')
    newline_count = input_string.count('\n')
    return whitespace_count, newline_count

def count_words(input_string):
    alphabet = set(string.ascii_letters)
    word_count = 0
    current_word = []
    # print(f'Input string: {input_string}')

    for char in input_string:
        if char in alphabet or char == "'":
            current_word.append(char)
        else:
            if current_word:
                word = ''.join(current_word).lower()
                # print(f'Word: {word}')
                word_count += 1
                current_word = []
    if current_word:
        # print(f'Entering if statement with current_word: {current_word}')
        # word = ''.join(current_word).lower()
        # print(f'Word: {word}')
        word_count += 1

    return word_count
















# def first_word_length(input_string):
#     alphabet = list(string.ascii_letters)
#     first_word = ""
#     for char in input_string:
#         if char not in alphabet:
#             break
#         first_word += char
#     return len(first_word)                                                                                                                                                                                                                                                                                                                                    