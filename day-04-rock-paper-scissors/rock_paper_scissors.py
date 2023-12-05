import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print("Welcome to the the RPS Game!")
user_input = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors: "))

if user_input < 0 or user_input > 2:
    print("You typed an invalid number.")
else:
    computer = random.randint(0, 2)
    print(f"You chose\n{images[user_input]}")
    print(f"The computer chose\n{images[computer]}")

    if user_input == computer:
        print("It's a tie!")
    elif user_input + 1 == computer or (user_input == 2 and computer == 0):
        print("You lost!")
    else:
        print("You won!")
