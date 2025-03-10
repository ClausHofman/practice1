import os

#######################################################################################################################################
FUNC5_SUFFIX = ''
FUNC5_PREFIX = ''
FUNC5_READ_WORD_SET_FILEPATH = r'C:\Users\hoffi\Documents\GitHub\2025\practice1\unique_words.txt' # File containing a set of words
func5_variable_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH).rsplit('.', 1)[0] # Split from FUNC5_READ_WORD_SET_FILEPATH and remove the file extension
FUNC5_WRITE_FILEPATH = fr'C:\Users\hoffi\Documents\GitHub\2025\practice1\from_{func5_variable_filename}_ending_with_{FUNC5_SUFFIX}.txt'
func5_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH).rsplit('.', 1)[0]  # Split from FUNC5_READ_WORD_SET_FILEPATH and remove the file extension
FUNC6_SUFFIX = ''
FUNC6_READ_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt"
FUNC6_WRITE_FILEPATH = f'ending_with_{FUNC6_SUFFIX}_from_{os.path.basename(FUNC6_READ_FILEPATH)}'
FUNC10_READ_FILEPATH = r"C:\Users\hoffi\Documents\GitHub\2025\practice1\word_frequencies2.txt"
FUNC10_SEARCH_MODE = ''
#######################################################################################################################################

class Config:
    """
    Configuration class with default values and comments.
    """

    def __init__(self, config_data=None, **kwargs):
        """
        Initialize the configuration with default values or provided config_data.
        Additional keyword arguments can be used to update specific configuration values.
        """

        global FUNC10_SEARCH_MODE

        if config_data is None:
            config_data = {}
        
        # Update config_data with additional keyword arguments
        config_data.update(kwargs)

        # Whether function 1 is active
        self.FUNC1_ACTIVE = config_data.get('FUNC1_ACTIVE', False)
        # Length of words to list in function 1
        self.FUNC1_WORD_LENGTH = config_data.get('FUNC1_WORD_LENGTH', 5)
        # Filename to read unique words from
        self.FUNC1_READ_FILENAME = config_data.get('FUNC1_READ_FILENAME', 'unique_words.txt')
        # Words to remove in function 2
        self.FUNC2_ADD_TO_REMOVED_WORDS = config_data.get('FUNC2_ADD_TO_REMOVED_WORDS', [])
        # Filepath for input string
        self.INPUT_STRING_FILEPATH = config_data.get('INPUT_STRING_FILEPATH', 'input.txt')
        # Filepath to write word frequencies
        self.FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH = config_data.get('FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH', 'word_frequencies2.txt')
        # Filepath to read unique words
        self.FUNC4_READ_UNIQUE_WORDS_FILEPATH = config_data.get('FUNC4_READ_UNIQUE_WORDS_FILEPATH', 'unique_words.txt')
        # Suffix to find words ending with in function 5
        self.FUNC5_SUFFIX = config_data.get('FUNC5_SUFFIX', '')
        # Prefix to find words starting with in function 5
        self.FUNC5_PREFIX = config_data.get('FUNC5_PREFIX', '')
        # Filepath to read word set in function 5
        self.FUNC5_READ_WORD_SET_FILEPATH = config_data.get('FUNC5_READ_WORD_SET_FILEPATH', 'unique_words.txt')
        # Filepath to write words ending with suffix in function 5
        self.FUNC5_WRITE_FILEPATH = config_data.get('FUNC5_WRITE_FILEPATH', 'from_unique_words_ending_with_.txt')
        # Filepath to write words starting with prefix in function 5
        self.FUNC5_WRITE_PREFIX_FILEPATH = config_data.get('FUNC5_WRITE_PREFIX_FILEPATH', 'from_unique_words_starting_with_.txt')
        # Suffix to find words ending with in function 6
        self.FUNC6_SUFFIX = config_data.get('FUNC6_SUFFIX', '')
        # Filepath to read word frequencies in function 6
        self.FUNC6_READ_FILEPATH = config_data.get('FUNC6_READ_FILEPATH', 'word_frequencies2.txt')
        # Filepath to write words ending with suffix in function 6
        self.FUNC6_WRITE_FILEPATH = config_data.get('FUNC6_WRITE_FILEPATH', 'ending_with__from_word_frequencies2.txt')
        # Whether to print word frequencies in function 6
        self.FUNC6_PRINT = config_data.get('FUNC6_PRINT', False)
        # Word to find words after in function 7
        self.FIND_WORDS_AFTER = config_data.get('FIND_WORDS_AFTER', '')
        # Filepath to read input string in function 9
        self.FUNC9_READ_FILEPATH = config_data.get('FUNC9_READ_FILEPATH', 'input.txt')
        # Word to search in function 9
        self.FUNC9_WORD_TO_SEARCH = config_data.get('FUNC9_WORD_TO_SEARCH', '')
        # Mode for function 9
        self.FUNC9_MODE = config_data.get('FUNC9_MODE', 'line')
        # Search mode for function 9
        self.FUNC9_SEARCH_MODE = config_data.get('FUNC9_SEARCH_MODE', 'partial')
        # Whether search is case insensitive in function 9
        self.FUNC9_CASE_INSENSITIVE = config_data.get('FUNC9_CASE_INSENSITIVE', True)
        # Proximity word for function 9
        self.FUNC9_PROX_WORD = config_data.get('FUNC9_PROX_WORD', '')
        # Proximity distance for function 9
        self.FUNC9_PROX_DIST = config_data.get('FUNC9_PROX_DIST', 1)
        # Whether function 10 is active
        self.FUNC10_ACTIVE = config_data.get('FUNC10_ACTIVE', True)
        # Words to search in function 10
        self.FUNC10_WORDS_TO_SEARCH = config_data.get('FUNC10_WORDS_TO_SEARCH', [])
        # Filepath to read input string in function 10
        self.FUNC10_READ_FILEPATH = config_data.get('FUNC10_READ_FILEPATH', 'input.txt')
        # Sorting method for function 10
        self.FUNC10_SORTING = config_data.get('FUNC10_SORTING', 'frequency')
        # Search mode for function 10
        self.FUNC10_SEARCH_MODE = config_data.get('FUNC10_SEARCH_MODE', 'partial')
        # Word frequency for function 10
        self.FUNC10_WORD_FREQUENCY = config_data.get('FUNC10_WORD_FREQUENCY', 1)
        # Filepath to write word frequencies in function 10
        self.FUNC10_WRITE_FILEPATH = config_data.get('FUNC10_WRITE_FILEPATH', 'word_frequencies.txt')
        # Filepath to write removed words
        self.REMOVED_WORDS_PATH = config_data.get('REMOVED_WORDS_PATH', 'removed_words.txt')
        # Filepath to write newest unique words
        self.NEWEST_UNIQUE_WORDS_PATH = config_data.get('NEWEST_UNIQUE_WORDS_PATH', 'newest_unique_words.txt')
        # Filepath to read unique words
        self.UNIQUE_WORDS_PATH = config_data.get('UNIQUE_WORDS_PATH', r'C:/Users/hoffi/Documents/GitHub/2025/practice1/unique_words.txt')
        # Unique words filename
        self.UNIQUE_WORDS_FILENAME = config_data.get('UNIQUE_WORDS_FILE', 'unique_words.txt')
        # Setting to control updating the unique words file
        self.UPDATE_UNIQUE_WORDS_FILE = config_data.get('UPDATE_UNIQUE_WORDS_FILE', True)

        FUNC10_SEARCH_MODE = config_data.get('FUNC10_SEARCH_MODE', FUNC10_SEARCH_MODE)

config_a = {
    # Whether function 1 is active
    "FUNC1_ACTIVE": False,
    # Length of words to list with list_words_of_length
    "FUNC1_WORD_LENGTH": 4,
    # Filename to read unique words from with list_words_of_length
    "FUNC1_READ_FILENAME": "unique_words.txt",
    # Words to remove with remove_words_from_unique_words_set
    "FUNC2_ADD_TO_REMOVED_WORDS": [],
    # Filepath for input string with read_input_string
    "INPUT_STRING_FILEPATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/input.txt",
    # Filepath to write word frequencies for list_words_by_frequency (step 4)
    "FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/word_frequencies2.txt",
    # Filepath to read unique words for list_words_by_frequency (step 4)
    "FUNC4_READ_UNIQUE_WORDS_FILEPATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/unique_words.txt",
    # Suffix to find words with find_words_ending_with_from_set (5)
    "FUNC5_SUFFIX": '',
    # Prefix to find words with find_words_starting_with_from_set (5)
    "FUNC5_PREFIX": '',
    # Filepath to read word set with find_words_ending_with_from_set
    "FUNC5_READ_WORD_SET_FILEPATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/unique_words.txt",
    # Filepath to write words ending with suffix with find_words_ending_with_from_set
    "FUNC5_WRITE_FILEPATH": fr'C:/Users/hoffi/Documents/GitHub/2025/practice1/from_unique_words_ending_with_.txt',
    # Filepath to write words starting with prefix with find_words_starting_with_from_set
    "FUNC5_WRITE_PREFIX_FILEPATH": fr'C:/Users/hoffi/Documents/GitHub/2025/practice1/from_unique_words_starting_with_.txt',
    # Suffix to find words find_words_ending_with_from_file
    "FUNC6_SUFFIX": '',
    # Filepath to read word frequencies with find_words_ending_with_from_file
    "FUNC6_READ_FILEPATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/word_frequencies2.txt",
    # Filepath to write words ending with suffix with find_words_ending_with_from_file
    "FUNC6_WRITE_FILEPATH": f'ending_with_{FUNC6_SUFFIX}_from_{os.path.basename(FUNC6_READ_FILEPATH)}',
    # Whether to print word frequencies in find_words_ending_with_from_file
    "FUNC6_PRINT": False,
    # Word to find words with find_words_after
    "FIND_WORDS_AFTER": "",
    # Input string filepath for find_sentences_with_word
    "FUNC9_READ_FILEPATH": "C:/Users/hoffi/Documents/GitHub/2025/practice1/input.txt",
    # Word to search in function 9
    "FUNC9_WORD_TO_SEARCH": "",
    # Mode for find_sentences_with_word - 'sentence' or 'line'
    "FUNC9_MODE": "line",
    # Search mode: 'exact', 'partial', 'prefix', 'suffix', 'regex', 'proximity'
    "FUNC9_SEARCH_MODE": "partial",
    # Whether search is case insensitive in find_sentences_with_word
    "FUNC9_CASE_INSENSITIVE": True,
    # Proximity word for find_sentences_with_word
    "FUNC9_PROX_WORD": "",
    # Proximity distance for find_sentences_with_word
    "FUNC9_PROX_DIST": 1,
    # Whether find_words_in_frequencies is active
    "FUNC10_ACTIVE": True,
    # Words to search in find_words_in_frequencies
    "FUNC10_WORDS_TO_SEARCH": ['Hello from helper_configs.py'],
    # Filepath to read input string in find_words_in_frequencies
    "FUNC10_READ_FILEPATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/word_frequencies2.txt",
    # Sorting method: 'alphabetical' or 'frequency'
    "FUNC10_SORTING": "frequency",
    # Search mode: 'exact' or 'partial'
    "FUNC10_SEARCH_MODE": "partial",
    # Word frequency for find_words_in_frequencies
    "FUNC10_WORD_FREQUENCY": 1,
    # Filepath to write word frequencies in find_words_in_frequencies
    "FUNC10_WRITE_FILEPATH": fr'C:/Users/hoffi/Documents/GitHub/2025/practice1/words_{FUNC10_SEARCH_MODE}_in_{os.path.basename(FUNC10_READ_FILEPATH)}',
    # Filepath to write removed words
    "REMOVED_WORDS_PATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/removed_words.txt",
    # Filepath to write newest unique words
    "NEWEST_UNIQUE_WORDS_PATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/newest_unique_words.txt",
    # Filepath to read unique words
    "UNIQUE_WORDS_FILEPATH": r"C:/Users/hoffi/Documents/GitHub/2025/practice1/unique_words.txt",
    # Unique words filename
    "UNIQUE_WORDS_FILENAME": "unique_words.txt",
    # Setting to control updating the unique words file
    "UPDATE_UNIQUE_WORDS_FILE": True
}
