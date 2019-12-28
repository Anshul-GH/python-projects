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
        min_word_length = input('What minimum word length do you want? [4-16]: ')
        try:
            min_word_length = int(min_word_length)
            if 4 <= min_word_length <= 16:
                return min_word_length
        
        # Print the current game state
        print('Word {0}'.format(get_display_word(word, idxs)))
        print('Attempts Remaining: {0}'. format(attempts_remaining))
        print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))

        # Get player's next letter guess
        next_letter = get_next_letter(remaining_letters)

        # Check if letter guess is in word
        if next_letter in word:
            # Guessed correctly
            print('{0} is in the word!'.format(next_letter))

            # Reveal matching letters
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            # Guessed incorrectly
            print('{0} is NOT in the word!'.format(next_letter))

            # Decrement num of attempts left and append guess to wrong guesses
            attempts_remaining -= 1
            wrong_letters.append(next_letter)
        
        # Check if the word is completely solved
        if False not in idxs:
            words_solved = True
        print()
    
    # The game is over: reveal the word
    print('The word is {0}'.format(word))

    # Notify player of victory or defeat
    if words_solved:
        print('Congratulations! You won!')
    else:
        print('Try again next time!')

    # Ask player if he/she wants to try again
    try_again = input('Would you like to try again? [Y/N]: ')
    return try_again.lower() == 'y'

if __name__ == '__main__':
    while play_hangman():
        print()






