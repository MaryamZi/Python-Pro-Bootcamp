import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)

letter_arr = ["_"] * len(word)
already_guessed = []

while "_" in letter_arr:
    guess = input("Make a guess: ").lower()

    if guess in word:
        for index in range(len(word)):
            char = word[index]
            if guess == char:
                letter_arr[index] = guess
    else:
        if len(stages) == 1:
            print(f"{stages.pop()}\n\nGame over, you lost!")
            break
        elif guess in already_guessed:
            print(f"You already used '{guess}' as a guess")
        else:
            print(f"{stages.pop()}\n\nThe word does not have '{guess}'")
            already_guessed.append(guess)

    formatted_string = ""

    for letter in letter_arr:
        formatted_string += letter

    print(formatted_string)

if not "_" in word:
    print("Congratulations, you won!")
