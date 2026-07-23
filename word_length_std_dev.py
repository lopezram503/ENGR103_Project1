# GitHub username: lopezram503
# Date: 7/20/26
# Description: This code separates a sentence into individual words, finds the length of each word
# and returns the sample standard deviation of those word lengths.


def word_length_std_dev(sentence):

    """" Returns the sample standard deviation of the
         lengths of the words in a string."""

    individual_words = sentence.split() # This line splits the sentence into individual words

    word_lengths = [] # This line creates an empty list to store the length of each word

    for word in individual_words: # This line goes through each word in the sentence

        word_lengths.append(len(word)) # This line adds the number of letters in the word to the list

    total_letters = 0 # This line starts the total number of letters at 0

    for word_length in word_lengths: # This line adds all the word lengths together

        total_letters = total_letters + word_length

    average = total_letters / len(word_lengths) # This line finds the average word length

    total = 0 # This line starts the total for the squared differences at 0

    for word_length in word_lengths: # This line goes through each word length again
        difference = word_length - average # This line finds the difference between the word length and the average
        squared = difference ** 2 # This line squares the difference
        total = total + squared # This line adds the squared difference to the total

    new_number_of_words = len(word_lengths) - 1 # This line subtracts 1 from the total number of words

    variance = total / new_number_of_words # This line divides by the new number of words to find the variance

    standard_deviation = variance ** 0.5 # This line takes the square root of the variance

    return standard_deviation # This line returns the sample standard deviation


# print(word_length_std_dev('Turtle rabbit'))
# print(word_length_std_dev('Batman Robin Penguin'))
# print(word_length_std_dev('Batman fights crime and protects Gotham City every night'))
# print(word_length_std_dev('I am Batman'))

