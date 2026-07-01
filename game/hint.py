import random

def give_hint(word, guessed_letters):
    remaining_letters = [letter for letter in word if letter not in guessed_letters]

    if remaining_letters:
        hint_letter = random.choice(remaining_letters)
        guessed_letters.append(hint_letter)
        return hint_letter

    return None