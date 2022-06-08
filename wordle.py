#!/usr/bin/env python3
# Authors: Jackson Taylor and Evan Wiedholz
# Date: 03/01/2022
# Description: Clone of the newly popular game from New York Times, "Wordle"
import enchant
import random
from re import match as re_match
from string import printable


word_length = 5  # How long the answers and the guesses have to be. Default: 5
max_number_of_guesses = 6  # How many tries to guess the word: Default: 6
# Symbols for showing letter correctness
no_match_character = '-'  # Letter is not in the answer
partial_match_character = '+'  # Letter is in the answer, but not this position
full_match_character = '*'  # Letter is in the answer, and the right position

# Object used to check if words are words
enchant_dict = enchant.Dict("en_US")
alphabet = printable[10:36]


def get_user_guess():
    while True:
        guess = input("Guess: ").lower()
        if not re_match('^[a-z]{' + str(word_length) + '}$', guess):
            print(
                "Guess must be {} characters long and only include letters!"
                .format(word_length))
            continue

        if not enchant_dict.check(guess):
            print("Guess must be an english word!")
            continue

        return guess


# This could potentially be really slow in some cases, depending on how long
# the word is. This could be changed to use a library called Random-Word, but
# that looks like it requires an internet connection to work.
# One idea would be to keep a list of all words in some files in a data
# directory or something, but then you almost lose the ability to have
# word_length be configurable.
def generate_correct_answer():
    while True:
        answer = ''.join(
            [alphabet[
                random.randint(0, len(alphabet) - 1)] for x in range(
                        word_length)])

        if enchant_dict.check(answer):
            return answer


# Evan is mostly the author for this function. Unless you can do something
# crazy pythonic, I think this would probably be one of the easier solutions.
def compare_guess_to_answer(guess, answer):
    score = [no_match_character for _ in guess]

    guess_unmatched_character_position = {}
    answer_unmatched_character_position = {}

    for i in range(len(answer)):
        answer_unmatched_character_position[i] = answer[i]
        guess_unmatched_character_position[i] = guess[i]

    # Match everything that's a full match
    for index in range(len(guess)):
        # If the letter in the index of the guess is the same as the one in
        # the answer
        if (answer_unmatched_character_position[index] ==
           guess_unmatched_character_position[index]):
            score[index] = full_match_character
            del answer_unmatched_character_position[index]
            del guess_unmatched_character_position[index]

    # Go back and check for any partial matches
    for key, value in guess_unmatched_character_position.items():
        # Does the letter exist somewhere in the answer?
        if value in answer_unmatched_character_position.values():
            # Get a list of the remaining keys (indexes of the unaccounted
            # for letters in the answer)
            key_list = list(answer_unmatched_character_position.keys())
            # Get a list of the remaining values in the answer
            # (literal letters)
            val_list = list(answer_unmatched_character_position.values())

            # Mark the score
            score[key] = partial_match_character
            # Get the key for where this letter exists in the answer (the
            # index), and then remove it from the answers unmatched character
            # positions
            del answer_unmatched_character_position[
                key_list[val_list.index(value)]]

    return score


if __name__ == '__main__':
    answer = generate_correct_answer()

    number_of_guesses = 0

    guessed_correctly = False

    while number_of_guesses < max_number_of_guesses and not guessed_correctly:
        number_of_guesses += 1
        guess = get_user_guess()

        if guess == answer:
            guessed_correctly = True
        else:
            print(''.join(compare_guess_to_answer(guess, answer)))
            print(guess)

    if not guessed_correctly:
        print("You lose!  Answer was: {}".format(answer))
    else:
        print("Congrats, you win! You guessed it in {} tries!".format(
            number_of_guesses))
