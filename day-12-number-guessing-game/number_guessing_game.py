import random

MODE_EASY_TURNS = 10
MODE_HARD_TURNS = 5

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

difficulty_easy = input("Choose a difficulty: 'easy' or 'hard': ").lower() == 'easy'
remaining_guesses = MODE_EASY_TURNS if difficulty_easy else MODE_HARD_TURNS

number = random.randint(1, 100)
correct_guess = False

while remaining_guesses > 0:
    print(f"You have {remaining_guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        correct_guess = True
        break

    print(f"Too {'high' if guess > number else 'low'}.\nGuess again.")
    remaining_guesses -= 1

if correct_guess:
    print("Congratulations, you won!")
else:
    print("You've run out of guesses. You lost. :(")

print(f"The number was {number}")
