"""
Hasana Parker & Blessing Adomakoh
Assignment 5: Corpus Analysis
February 21st, 2022

"""

# ________________________________________
# Sentence Stats


def tokenize(sentence):
    """
    Function takes in a sentence and returns it as a lower cased list with no punctuation
    :param sentence: (str) any sentence
    :return: (lst) words in the sentence in a list
    """
    word_list = []
    words = sentence.split()
    punctuation = [".", ",", ";", ";", "!", "?"]
    for word in words:
        if word[-1] in punctuation:
            word = word[0:-1]  # keeping the part of the word from the beginning to the second last character.
        word_list.append(word.lower()) # appending a lower case version of the word.

    return word_list


def get_sentence_lengths(filename):
    """
    Functions gets a file and finds the lengths of each line, then appends the lengths to a list.
    :param filename: (str) is a file
    :return: (lst) a list of the lengths of each line.
    """
    file = open(filename, "r")
    list_of_lengths = []

    for line in file:
        list_of_lengths.append(len(tokenize(line)))  # append the length of the line without punctuation to list

    file.close()
    return list_of_lengths


def print_sentence_stats(filename):
    """
    the function takes a file and returns the total number of sentences in the file, the length
    of the longest sentence, the length of the shortest sentence
    :param filename: (str) a file
    :return: none
    """
    file = open(filename, "r")
    line_count = 0

    for line in file:
        line_count += 1  # counting each line in the file

    list_of_lengths = get_sentence_lengths(filename)

    file.close()

    print("Total sentences: " + "\t" + str(line_count))
    print("Longest sentence: " + "\t" + str(max(list_of_lengths)))
    print("Shortest sentence: " + "\t" + str(min(list_of_lengths)))
    print("Ave. sentence length: " + "\t" + str(sum(list_of_lengths) / line_count))


# ________________________________________
# Word Stats


def add_words_to_dict(diction, list_of_words):
    """
    This function counts how many times a key appears in the dictionary
    :param diction: (str) a dictionary where the key is a string and the value is an integer
    :param list_of_words: (lst) list of strings representing words
    :return: none
    """

    for word in list_of_words:
        if not word in diction:
            diction[word] = 1  # making it so that if the word is not present in the dictionary, set to 1
        else:
            diction[word] += 1 # keeps track of the amount of times a word appears.


def get_word_counts(filename):
    """
    This function takes a file and returns the frequency each word occurs
    :param filename: (str) a file
    :return: dictionary with the frequency each word (key) occurs
    """
    file = open(filename, "r")
    dictionary = {}

    for line in file:
        list_of_keys = tokenize(line)
        add_words_to_dict(dictionary, list_of_keys) # adding the keys to the dictionary

    file.close()

    return dictionary


def dict_count_max(dict_word_freq):
    """
    This function takes a dictionary of word frequencies and returns the word in the dictionary that occurs the most.
    :param dict_word_freq: (dict) a dictionary of words and their frequencies.
    :return: the word that occurs the most frequently.
    """
    max_key = -1
    max_value = -1

    for key in dict_word_freq:
        value = dict_word_freq[key] # setting the value of the key
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


def print_top_ten(filename):
    """
    This function makes a dictionary of the top ten words and their frequencies.
    :param filename: (file) any file
    :return: (dict) made up of words and their frequencies.
    """
    top_ten = {}
    file = open(filename, "r")
    list_of_frequency = get_word_counts(filename)

    for i in range(1, 11): # going from 1 to 10
        current_max_key = dict_count_max(list_of_frequency)
        print(str(i) + ": " + " " + current_max_key + "\t" + str(list_of_frequency[current_max_key]))
        list_of_frequency.pop(current_max_key) # removing from list_of_frequencies so that the word doesn't appear
        # as the max again when the for-loop runs again
    file.close()


def print_all_stats(filename):
    print("_" * 30)
    print_sentence_stats(filename)
    print("_" * 30)
    print("Top ten most frequent words")
    print_top_ten(filename)

# ________________________________________
# Analysis section

"""
normal.txt

______________________________
Total sentences: 	99903
Longest sentence: 	158
Shortest sentence: 	1
Ave. sentence length: 	23.068286237650522
______________________________
Top ten most frequent words
1:  the	168757
2:  of	88761
3:  and	69104
4:  in	62493
5:  to	50868
6:  a	45790
7:  is	24265
8:  as	22366
9:  was	21076
10:  for	18113
"""


"""
simple.txt
______________________________
Total sentences: 	99925
Longest sentence: 	142
Shortest sentence: 	1
Ave. sentence length: 	15.491488616462346
______________________________
Top ten most frequent words
1:  the	108686
2:  of	50234
3:  and	40835
4:  in	40083
5:  a	35467
6:  to	31609
7:  is	29803
8:  was	17395
9:  it	14357
10:  are	13248
"""


# 9
"""
The average sentence length of normal.txt is longer than the average sentence length
of simple.txt, which implies that normal.txt is made up of more complex sentences. Additionally,
simple.txt makes use of the pronoun "it" more often while normal.txt does not. This implies that normal.txt is more
direct and specific about their topic as opposed to referring to the subject arbitrarily. 
 
"""


# 10
def average_word_length(filename):
    """
    This function takes in a file and calculates the average word length.
    :param filename: (file)
    :return: (float) average word length.
    """
    file = open(filename, "r")
    summation = 0
    num_of_words = 0

    for line in file:
        list_of_words = tokenize(line)
        num_of_words += len(list_of_words)

        for word in list_of_words:
            summation += len(word)

    return summation / num_of_words


"""
The average word length of simple.txt is 4.710921990946952
The average word length of normal.txt is 5.058261531004851

The normal.txt file has a higher average word length than the simple.txt file therefore
the normal.txt makes use longer and more complex words.

"""