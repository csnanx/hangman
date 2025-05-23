import random
from hangman_art import stages
from hangman_words import word_list

lives = 6
random_word = random.choice(word_list)

dashes = ""
for _ in random_word:
    dashes += "_"
print(f"Word to guess: {dashes}")

correct_letters = []
game_over = False

while not game_over:
    print(f"**********{lives}/6 LIVES LEFT**********")
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess not in random_word:
        lives -= 1
        print(f"Your guess {guess} is not in the word.\nYou lose a life.")
    elif guess in correct_letters:
        print(f"You've already guessed {guess}")

    for char in random_word:
        if char == guess:
            display += guess
            correct_letters.append(guess)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("**********You WIN**********")
    elif lives == 0:
        game_over = True
        print("**********You LOSE**********")

    print(stages[lives])
