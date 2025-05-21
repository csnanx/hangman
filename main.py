import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 6
random_word = random.choice(word_list)
print(random_word)

dashes = ""
for _ in random_word:
    dashes += "_"
print(dashes)

guessed_letters = []
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess not in random_word:
        lives -= 1

    for char in random_word:
        if char == guess:
            display += guess
            guessed_letters.append(guess)
        elif char in guessed_letters:
            display += char
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")