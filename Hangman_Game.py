import random

def hangman():
    # List of words to choose from
    words = ['kick', 'hangman', 'computer', 'codealpha', 'challenge']
    
    # Randomly choose a word
    word = random.choice(words)
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()   # Letters guessed by player
    wrong_guesses = 0
    max_wrong_guesses = 6


    print("🎮 Welcome to the Hangman Game!")
    print("You have", max_wrong_guesses, "lives. Good luck!")

    while wrong_guesses < max_wrong_guesses and word_letters:
        # Show current word progress
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("\nCurrent word:", ' '.join(display_word))

        # Take input
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess! You have", max_wrong_guesses - wrong_guesses, "tries left.")

    # End of game
    if not word_letters:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
hangman()
