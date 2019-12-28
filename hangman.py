from string import ascii_lowercase
from words import get_random_word


def get_num_attempts():
    """ Get user-inputted number of incorrect attempts for the game. """
    while True:
        num_attempts = input('How many incorrect attempts do you want? [1-25]: ')
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print('{0} is not an integer between 1 and 25'.format(num_attempts))
        except ValueError:
            print('{0} is not an integer between 1 and 25'.format(num_attempts))


def get_min_word_length():
    """ Get user-inputted minimum word length for the game."""
    while True:
        min_word_length = input()

