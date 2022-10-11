def create_board(word):
    """Let the user know how many letters the secret word contains. Make the board that shows a blank for each letter"""
    print(f"This is the create_board function and the value of `word` is {word}")
    board_list = []
    for letter in word:
        board_list.append("_")
    print(f"Here is your word to guess: {' '.join(board_list)}")
    return board_list


def show_board(word, board, correct_list):   
    for letter in correct_list:
        for idx in range(len(word)):
            if word[idx] == letter:
                board[idx] = letter
    print(" ".join(board))

def get_user_guess():
    """Get a guessed letter from the user and return it"""
    # print("This is the get_user_guess function.")
    guess = input("Guess your letter: ")
    return guess

def play_game():
    """All game play happens in this function"""
    # computer picks a word to guess.
    # start with one word
    # TODO pick word from list
    word_to_guess = 'dream'.upper()
 
    game_board = create_board(word_to_guess)
    # print(f'The value of game_board is {game_board}')
    correct_guesses = []
    # print(f'The value of correct_guesses is {correct_guesses}')
    incorrect_guesses = []
    # print(f'The value of incorrect_guesses is {incorrect_guesses}')
    number_of_incorrect_guesses = 0

    # get a guess from the user
    # print(f'The value of new_guess is {new_guess}')

    # make a loop that stops either when the player runs out of guesses or completes the word

    while len(incorrect_guesses) < 8 and "_" in game_board:
        new_guess = get_user_guess().upper()
        # assess whether the guess was right or wrong
        if new_guess == '':
            print("Enter a letter dummy!")
        elif new_guess in correct_guesses or new_guess in incorrect_guesses:
            print(f"You already guessed '{new_guess}' dum dum!")
            print(f"These are the letters you guessed that are wrong: '{incorrect_guesses}' ")
        elif new_guess in word_to_guess:
            # and put it in the appropriate list, either correct_guesses or incorrect_guesses
            correct_guesses.append(new_guess)
            print('Good job little buddy you got one right!')
            if len(correct_guesses) == len(word_to_guess):
                print("I guess you're not a dum dum after all! Congradulations!")
        else:
            incorrect_guesses.append(new_guess)
            print('You were so close to not being a dummy!')

        show_board(word_to_guess, game_board, correct_guesses)



if __name__ == "__main__":
    play_game()
