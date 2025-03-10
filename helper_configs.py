import os

# Just some variables that can be fiddled with if needed, and some should be fiddled with to affect what is being searched for and how it's being searched
# The rest can be changed directly in the config dictionary at the bottom of this file
#######################################################################################################################################
# Below settings until "Paths and filenames" should be consistent across configurations because they affect filename creation
FIND_WORDS_FROM_FILE_SUFFIX = 'ing' # anything
FIND_WORDS_FROM_FILE_PREFIX = 'un' # anything
FIND_WORDS_FROM_FREQUENCIES_FILE_MODE = 'partial' # 'exact' or 'partial'
FUNC10_WORD_FREQUENCY = 1
# Paths and filenames #
#######################
# Get current working directory with os.getcwd() or replace with other path
unique_words_filename = 'unique_words.txt'
unique_words_filepath = os.path.join(os.getcwd(), unique_words_filename)

# Find words ending with a specified prefix/suffix from word frequencies file read and the write paths
FUNC6_READ_FILENAME = fr'{os.getcwd()}\word_frequencies2.txt'
find_words_ending_with_from_file_WRITE_PATH = f'ending_with_{FIND_WORDS_FROM_FILE_SUFFIX}_from_{os.path.basename(FUNC6_READ_FILENAME)}'
find_words_starting_with_from_file_WRITE_PATH = f'starting_with_{FIND_WORDS_FROM_FILE_PREFIX}_FROM_{os.path.basename(FUNC6_READ_FILENAME)}'
# Word frequency file path (format = word: number). Specify a frequency and write found words to a new file
FUNC10_READ_FILEPATH = fr'{os.getcwd()}\word_frequencies2.txt'
# Read a set of unique words
FUNC5_READ_WORD_SET_FILEPATH = fr'{os.getcwd()}\unique_words.txt' # File containing a set of words
func5_variable_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH).rsplit('.', 1)[0] # Split from FUNC5_READ_WORD_SET_FILEPATH and remove the file extension
FUNC5_WRITE_FILEPATH = fr'{os.getcwd()}\from_{func5_variable_filename}_ending_with_suffix.txt'
# DELETE THIS? #func5_filename = os.path.basename(FUNC5_READ_WORD_SET_FILEPATH).rsplit('.', 1)[0]  # Split from FUNC5_READ_WORD_SET_FILEPATH and remove the file extension
#######################################################################################################################################

class Config:
    """
    Configuration class with default values and comments.
    """

    def __init__(self, config_data: dict=None, **kwargs):
        """
        Initialize the configuration with default values or provided config_data.
        Additional keyword arguments can be used to update specific configuration values.
        """

        if config_data is None:
            config_data = {}
        
        # Update config_data with additional keyword arguments
        config_data.update(kwargs)

        # Whether list_words_of_length is active
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
        # Suffix to find words with find_words_ending_with_from_set
        self.FUNC5_SUFFIX = config_data.get('FUNC5_SUFFIX', '')
        # Prefix to find words with find_words_starting_with_from_set
        self.FUNC5_PREFIX = config_data.get('FUNC5_PREFIX', '')
        # Filepath to read word set in function 5
        self.FUNC5_READ_WORD_SET_FILEPATH = config_data.get('FUNC5_READ_WORD_SET_FILEPATH', 'unique_words.txt')
        # Filepath to write words ending with suffix in function 5
        self.FUNC5_WRITE_FILEPATH = config_data.get('FUNC5_WRITE_FILEPATH', 'from_unique_words_ending_with_.txt')
        # Filepath to write words starting with prefix in function 5
        self.FUNC5_WRITE_PREFIX_FILEPATH = config_data.get('FUNC5_WRITE_PREFIX_FILEPATH', 'from_unique_words_starting_with_.txt')
        
        # Suffix to find words ending with in find_words_ending_with_from_file
        self.FIND_WORDS_FROM_FILE_SUFFIX = config_data.get('FIND_WORDS_FROM_FILE_SUFFIX', '')
        # Filepath to read word frequencies in find_words_ending_with_from_file
        self.find_words_ending_with_from_file_READ_FILEPATH = config_data.get('find_words_ending_with_from_file_READ_FILEPATH', 'word_frequencies2.txt')
        # Filepath to write words ending with suffix in find_words_ending_with_from_file
        self.find_words_ending_with_from_file_WRITE_PATH = config_data.get('find_words_ending_with_from_file_WRITE_PATH', 'ending_with__from_word_frequencies2.txt')
        # Whether to print word frequencies in find_words_ending_with_from_file
        self.find_words_ending_with_from_file_PRINT = config_data.get('find_words_ending_with_from_file_PRINT', False)

        # Prefix to find words starting with in find_words_starting_with_from_file
        self.FIND_WORDS_FROM_FILE_PREFIX = config_data.get('FIND_WORDS_FROM_FILE_PREFIX', '')
        # Filepath to read word frequencies in find_words_starting_with_from_file
        self.find_words_starting_with_from_file_READ_FILEPATH = config_data.get('find_words_starting_with_from_file_READ_FILEPATH', 'word_frequencies2.txt')
        # Filepath to write words starting with prefix in find_words_starting_with_from_file
        self.find_words_starting_with_from_file_WRITE_PATH = config_data.get('find_words_starting_with_from_file_WRITE_PATH', 'starting_with__from_word_frequencies2.txt')
        # Whether to print word frequencies in find_words_ending_with_from_file
        self.find_words_starting_with_from_file_PRINT = config_data.get('find_words_starting_with_from_file_PRINT', False)
        
        # Word to find words after in function 7
        self.FIND_WORDS_AFTER = config_data.get('FIND_WORDS_AFTER', '')

        # Filepath to read input string in function 9
        self.FUNC9_READ_FILEPATH = config_data.get('FUNC9_READ_FILEPATH', 'input.txt')
        # Word to search in function 9
        self.FUNC9_WORD_TO_SEARCH = config_data.get('FUNC9_WORD_TO_SEARCH', '')
        # Mode for function 9
        self.DETERMINE_SENTENCES_MODE = config_data.get('DETERMINE_SENTENCES_MODE', 'line')
        # Search mode for function 9
        self.SENTENCE_SEARCH_MODE = config_data.get('SENTENCE_SEARCH_MODE', 'partial')
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
        self.FIND_WORDS_FROM_FREQUENCIES_FILE_MODE = config_data.get('FIND_WORDS_FROM_FREQUENCIES_FILE_MODE', 'partial')
        # Word frequency for function 10
        self.FUNC10_WORD_FREQUENCY = config_data.get('FUNC10_WORD_FREQUENCY', 1)
        # Filepath to write word frequencies in function 10
        self.FUNC10_WRITE_FILEPATH = config_data.get('FUNC10_WRITE_FILEPATH', 'word_frequencies.txt')
        # Enable printing words to terminal
        self.FUNC10_PRINT = config_data.get('FUNC10_PRINT', False)
        # Filepath to write removed words
        self.REMOVED_WORDS_PATH = config_data.get('REMOVED_WORDS_PATH', 'removed_words.txt')
        # Filepath to write newest unique words
        self.NEWEST_UNIQUE_WORDS_PATH = config_data.get('NEWEST_UNIQUE_WORDS_PATH', 'newest_unique_words.txt')
        # Filepath to read unique words
        self.UNIQUE_WORDS_PATH = config_data.get('UNIQUE_WORDS_PATH', f'{unique_words_filepath}')
        # Unique words filename
        self.UNIQUE_WORDS_FILENAME = config_data.get('UNIQUE_WORDS_FILE', unique_words_filename)
        # Setting to control updating the unique words file
        self.UPDATE_UNIQUE_WORDS_FILE = config_data.get('UPDATE_UNIQUE_WORDS_FILE', True)

# Make more configs if needed and change the config in file1.py
config_a = {
    # 1.
    # Whether list_words_of_length is active
    "FUNC1_ACTIVE": False,
    # Length of words to list with list_words_of_length
    "FUNC1_WORD_LENGTH": 4,
    # Filename to read unique words from with list_words_of_length
    "FUNC1_READ_FILENAME": f'{unique_words_filename}',

    # 2.
    # Words to remove with remove_words_from_unique_words_set
    "FUNC2_ADD_TO_REMOVED_WORDS": [],

    # 3.
    # Filepath for input string with read_input_string
    "INPUT_STRING_FILEPATH": fr'{os.getcwd()}/input.txt',

    # 4.
    # Filepath to write word frequencies for list_words_by_frequency
    "FUNC4_WRITE_WORD_FREQUENCIES_FILEPATH": fr'{os.getcwd()}/word_frequencies2.txt',
    # Filepath to read unique words for list_words_by_frequency
    
    "FUNC4_READ_UNIQUE_WORDS_FILEPATH": f'{unique_words_filepath}',

    # 5.
    # Suffix to find words with find_words_ending_with_from_set (5)
    "FUNC5_SUFFIX": '',
    # Prefix to find words with find_words_starting_with_from_set (5)
    "FUNC5_PREFIX": '',
    # Filepath to read word set with find_words_ending_with_from_set
    "FUNC5_READ_WORD_SET_FILEPATH": fr'{unique_words_filepath}/{unique_words_filename}',
    # Filepath to write words ending with suffix with find_words_ending_with_from_set
    "FUNC5_WRITE_FILEPATH": fr'{os.getcwd()}/from_unique_words_ending_with_.txt',
    # Filepath to write words starting with prefix with find_words_starting_with_from_set
    "FUNC5_WRITE_PREFIX_FILEPATH": fr'{os.getcwd()}/from_unique_words_starting_with_.txt',

    # 6a. find_words_ending_with_from_file
    # Filepath to read word frequencies with find_words_ending_with_from_file
    "find_words_ending_with_from_file_READ_FILEPATH": fr'{os.getcwd()}/word_frequencies2.txt',
    # Suffix to find words with find_words_ending_with_from_file
    "FIND_WORDS_FROM_FILE_SUFFIX": '',
    # Whether to print word frequencies in find_words_ending_with_from_file
    "find_words_ending_with_from_file_PRINT": False,
    # Filepath to write words ending with suffix with find_words_ending_with_from_file
    "find_words_ending_with_from_file_WRITE_PATH": f'ending_with_{FIND_WORDS_FROM_FILE_SUFFIX}_from_{os.path.basename(FUNC6_READ_FILENAME)}',

    # 6b. find_words_starting_with_from_file
    # Filepath to read word frequencies with find_words_starting_with_from_file
    "find_words_starting_with_from_file_READ_FILEPATH": fr'{os.getcwd()}/word_frequencies2.txt',
    # Prefix to find words with find_words_starting_with_from_file
    "FIND_WORDS_FROM_FILE_PREFIX": '',
    # Enable printing
    "find_words_starting_with_from_file_PRINT": False,
    # Filepath to write words starting with prefix with find_words_starting_with_from_file
    "find_words_starting_with_from_file_WRITE_PATH": f'starting_with_{FIND_WORDS_FROM_FILE_PREFIX}_from_{os.path.basename(FUNC6_READ_FILENAME)}',

    # 7.
    # Filepath to write removed words
    "REMOVED_WORDS_PATH": fr'{os.getcwd()}/removed_words.txt',
    # Filepath to write newest unique words
    "NEWEST_UNIQUE_WORDS_PATH": fr'{os.getcwd()}/newest_unique_words.txt',
    ### Update unique words file ###
    "UNIQUE_WORDS_FILEPATH": unique_words_filepath,
    # Unique words filename
    "UNIQUE_WORDS_FILENAME": f"{unique_words_filename}",
    # Setting to control updating the unique words file
    "UPDATE_UNIQUE_WORDS_FILE": True,

    # 8.
    # Word to find words with find_words_after
    # TODO: function might need some additions / improvements
    "FIND_WORDS_AFTER": "",

    # 9.
    # Input string filepath for find_sentences_with_word
    "FUNC9_READ_FILEPATH": fr'{os.getcwd()}/input.txt',
    # Word to search in function 9
    "FUNC9_WORD_TO_SEARCH": "right",
    # Mode for find_sentences_with_word - 'sentence' or 'line'
    "DETERMINE_SENTENCES_MODE": "line",
    # Search mode: 'exact', 'partial', 'prefix', 'suffix', 'regex', 'proximity'
    "SENTENCE_SEARCH_MODE": "exact",
    # Whether search is case insensitive in find_sentences_with_word
    "FUNC9_CASE_INSENSITIVE": True,
    # Proximity word for find_sentences_with_word
    "FUNC9_PROX_WORD": "",
    # Proximity distance for find_sentences_with_word
    "FUNC9_PROX_DIST": 1,

    # 10.
    # Whether find_words_in_frequencies is active
    "FUNC10_ACTIVE": False,
    # Words to search in find_words_in_frequencies
    "FUNC10_WORDS_TO_SEARCH": [],
    # Filepath to read input string in find_words_in_frequencies
    "FUNC10_READ_FILEPATH": fr'{os.getcwd()}/word_frequencies2.txt',
    # Sorting method: 'alphabetical' or 'frequency'
    "FUNC10_SORTING": "frequency",
    # Search mode: 'exact' or 'partial'
    "FIND_WORDS_FROM_FREQUENCIES_FILE_MODE": "partial",
    # Word frequency for find_words_in_frequencies
    "FUNC10_WORD_FREQUENCY": FUNC10_WORD_FREQUENCY,
    # Filepath to write word frequencies in find_words_in_frequencies
    "FUNC10_WRITE_FILEPATH": fr'{os.getcwd()}/words_of_frequency_{FUNC10_WORD_FREQUENCY}_in_{os.path.basename(FUNC10_READ_FILEPATH)}',
    # Enable printing words to terminal
    "FUNC10_PRINT": False
}
