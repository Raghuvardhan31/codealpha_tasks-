import random
import os

def display_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ---------
        """
    ]
    return stages[attempts]

def hangman():
    words = ["python", "programming", "hangman", "developer", "software", "engineer", "algorithm", "debugging"]
    word_to_guess = random.choice(words)
    word_length = len(word_to_guess)
    guessed_word = ["_"] * word_length
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    while attempts < max_attempts and "_" in guessed_word:
        # Refresh the terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display the game state
        print("Welcome to Hangman!")
        print(display_hangman(attempts))
        print(f"The word has {word_length} letters: {' '.join(guessed_word)}")
        print(f"You have {max_attempts - attempts} incorrect guesses left.")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")

        # Get the user's guess
        guess = input("Guess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            input("Press Enter to continue...")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            input("Press Enter to continue...")
            continue

        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts += 1

    # Final refresh and game result
    os.system('cls' if os.name == 'nt' else 'clear')
    print(display_hangman(attempts))
    print(f"The word was: {word_to_guess}")
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word!")
    else:
        print("You lost! Better luck next time.")

# Run the game
hangman()
