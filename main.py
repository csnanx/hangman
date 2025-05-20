import random

word_list = ["aardvark", "baboon", "camel"]
random_word = random.choice(word_list)
print(random_word)

dashes = ""
for _ in random_word:
    dashes += "_"
print(dashes)

guess = input("Guess a letter: ").lower()

display = ""
for char in random_word:
    if char == guess:
        display += guess
    else:
        display += "_"
    
print(display)