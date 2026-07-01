from game.engine import HangmanGame, MAX_INCORRECT_GUESSES, MAX_HINTS
from game.hangman_art import HANGMAN_STAGES


def play_console():
    game = HangmanGame()

    print("=" * 50)
    print("WELCOME TO HANGMAN!")
    print("=" * 50)

    while not game.is_won() and not game.is_lost():

        # 🔥 Show hangman visual
        print(HANGMAN_STAGES[game.incorrect_guesses])

        print("\nWord:", game.display_word())
        print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - game.incorrect_guesses}")
        print(f"Hints left: {MAX_HINTS - game.hints_used}")
        print(f"Guessed letters: {', '.join(game.guessed_letters) or 'None'}")

        choice = input("\nEnter a letter or type 'hint': ").lower().strip()

        # 💡 Hint logic
        if choice == "hint":
            hint = game.use_hint()
            if hint:
                print(f"💡 Hint: '{hint}' revealed (costs 1 life)")
            else:
                print("No hints left!")
            continue

        # ❌ Input validation
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        result = game.guess_letter(choice)

        if result == "already_guessed":
            print("You already guessed that letter!")
        elif result == "correct":
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess!")

    # 🔥 Final hangman stage
    print(HANGMAN_STAGES[game.incorrect_guesses])

    # 🏁 Result
    if game.is_won():
        print("\n" + "=" * 50)
        print(f"🎉 Congratulations! You guessed the word: '{game.word}'")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("💀 Game Over! You ran out of guesses.")
        print(f"The word was: '{game.word}'")
        print("=" * 50)