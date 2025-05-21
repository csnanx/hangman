# Hangman Game

A simple Hangman game built with Python. This command-line game challenges players to guess a hidden word one letter at a time before running out of attempts.

## Features

- Play Hangman in the terminal
- Random word selection from a predefined list
- ASCII art of hangman to show progress

## Requirements

- Python 3 (No external libraries)

## How to Run

```python
python hangman.py
```

## How to Play

- The game will display blank spaces for each letter in a word.
- You guess one letter at a time.
- If the letter is correct, it will fill in the blanks.
- If incorrect, you lose a life and a part of the hangman is drawn.
- You win by guessing the word before your lives run out (hangman is fully drawn).