import random

from data import data

print("Welcome to the Higher Lower Game")


def remove_and_get_member():
    index = random.randint(0, len(data) - 1)
    return data.pop(index)


def get_formatted_string(value):
    return f"{value['name']}, a {value['description']}, from {value['country']}"


def is_correct_guess(a_has_more_followers, user_guess):
    return user_guess == "A" if a_has_more_followers else user_guess == "B"


value_a = remove_and_get_member()
value_b = remove_and_get_member()

score = 0

while True:
    print(f"Compare A: {get_formatted_string(value_a)}")
    print(f"Against B: {get_formatted_string(value_b)}")
    guess = input("Who has more followers? 'A' or 'B'? ")

    a_has_more_followers = value_a['follower_count'] > value_b['follower_count']

    if not is_correct_guess(a_has_more_followers, guess):
        print(f"Sorry, you lost! Final score: {score}")
        break

    score += 1
    if len(data) == 0:
        print(f"Congratulations, you won! Final score: {score}")
        break

    print(f"That was correct. Current score: {score}")
    if not a_has_more_followers:
        value_a = value_b
    value_b = remove_and_get_member()
