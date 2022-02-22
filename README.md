# Wordle

This is a clone of the game wordle found [here](https://www.nytimes.com/games/wordle/index.html). This is played in the command line, and is not very feature rich. Mostly this was used to see how difficult it would be to write a game like this (turned out way harder than what I expected).

## Configuration
All configuration is done from inside the python file itself.
```python
word_length = 5  # How long the answers and the guesses have to be. Default: 5
max_number_of_guesses = 6  # How many tries to guess the word: Default: 6
# Symbols for showing letter correctness
no_match_character = '-'  # Letter is not in the answer
partial_match_character = '+'  # Letter is in the answer, but not this position
full_match_character = '*'  # Letter is in the answer, and the right position
```

## Rules
With the default settings, you have 6 chances to guess a 5 letter English word (according to the enchant python dictionary).

After each guess, your word is checked to see if the individual letters exist in the word, and are in the correct position or not.

Example Game:
```
Answer: canal

Guess: stare
--+--
stare
Guess: llama
+-+-+
Guess: drama
--+-+
Guess: clams
*++--
Guess: canal
Congrats, you win! You guessed it in 5 tries!
```

Authors:
Jackson Taylor and Evan Wiedholz