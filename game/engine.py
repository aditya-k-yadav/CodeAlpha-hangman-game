from game.words import choose_word
from game.hint import give_hint

MAX_INCORRECT_GUESSES = 6
MAX_HINTS = 1


class HangmanGame:
    def __init__(self):
        self.word = choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.hints_used = 0

    def display_word(self):
        return " ".join(
            [letter if letter in self.guessed_letters else "_" for letter in self.word]
        )

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return "already_guessed"

        self.guessed_letters.append(letter)

        if letter in self.word:
            return "correct"
        else:
            self.incorrect_guesses += 1
            return "incorrect"

    def use_hint(self):
        if self.hints_used >= MAX_HINTS:
            return None

        hint_letter = give_hint(self.word, self.guessed_letters)
        self.hints_used += 1
        self.incorrect_guesses += 1

        return hint_letter

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        return self.incorrect_guesses >= MAX_INCORRECT_GUESSES