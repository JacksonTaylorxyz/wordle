import unittest
import wordle


class TestWordle(unittest.TestCase):
    def test_exact_match(self):
        answer = 'aaaaa'
        guess = 'aaaaa'

        expected_score = [wordle.full_match_character for i in range(
            len(answer))]

        actual_score = wordle.compare_guess_to_answer(guess, answer)
        self.assertEqual(actual_score, expected_score)

    def test_no_letters_match(self):
        answer = 'aaaaa'
        guess = 'bbbbb'

        expected_score = [wordle.no_match_character for i in range(
            len(answer))]

        actual_score = wordle.compare_guess_to_answer(guess, answer)
        self.assertEqual(actual_score, expected_score)

    def test_only_one_letter_full_match(self):
        answer = 'aaaaa'
        guess = 'abbbb'

        expected_score = [
                wordle.full_match_character,
                wordle.no_match_character,
                wordle.no_match_character,
                wordle.no_match_character,
                wordle.no_match_character
        ]

        actual_score = wordle.compare_guess_to_answer(guess, answer)
        self.assertEqual(actual_score, expected_score)

    def test_only_one_letter_partial_match(self):
        answer = 'abaaa'
        guess = 'bcccc'

        expected_score = [
                wordle.partial_match_character,
                wordle.no_match_character,
                wordle.no_match_character,
                wordle.no_match_character,
                wordle.no_match_character
        ]

        actual_score = wordle.compare_guess_to_answer(guess, answer)
        self.assertEqual(actual_score, expected_score)

    def test_multiple_letters_partial_match(self):
        answer = 'ababa'
        guess = 'bcbcc'

        expected_score = [
                wordle.partial_match_character,
                wordle.no_match_character,
                wordle.partial_match_character,
                wordle.no_match_character,
                wordle.no_match_character
        ]

        actual_score = wordle.compare_guess_to_answer(guess, answer)
        self.assertEqual(actual_score, expected_score)

    def test_multiple_letters_in_guess_match_one_letter_in_answer(self):
        answer = 'aab'
        guess = 'bbc'

        expected_score = [
                wordle.partial_match_character,
                wordle.no_match_character,
                wordle.no_match_character,
                # wordle.no_match_character,
                # wordle.no_match_character
        ]

        actual_score = wordle.compare_guess_to_answer(guess, answer)
        self.assertEqual(actual_score, expected_score)


if __name__ == '__main__':
    unittest.main()
