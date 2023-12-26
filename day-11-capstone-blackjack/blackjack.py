import random

def draw_card(cards):
    card = random.choice(cards)
    cards.remove(card)
    return card

def draw_two_cards(cards):
    return [draw_card(cards), draw_card(cards)]

def replace_ace_if_over_21(current_cards):
    if sum(current_cards) > 21 and 11 in current_cards:
        current_cards.remove(11)
        current_cards.append(1)

continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y'

while continue_playing:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = draw_two_cards(cards)
    computer_cards = draw_two_cards(cards)

    computer_sum = sum(computer_cards)
    while computer_sum < 17:
        computer_cards.append(draw_card(cards))
        replace_ace_if_over_21(computer_cards)
        computer_sum = sum(computer_cards)

    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    game_ended = False
    win_message = "Congratulations! You won!"

    while not game_ended:
        draw_another = input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y'

        if draw_another:
            player_cards.append(draw_card(cards))
        else:
            game_ended = True

        replace_ace_if_over_21(player_cards)
        player_sum = sum(player_cards)

        if player_sum == 21:
            if player_sum == computer_sum:
                win_message = "It's a draw!"
            game_ended = True
        elif player_sum > 21 or computer_sum == 21:
            win_message = "You lost! :("
            game_ended = True
        elif computer_sum > 21:
            game_ended = True
        elif draw_another:
            print(f"Your cards: {player_cards}")
        else:
            if computer_sum == player_sum:
                win_message = "It's a draw!"
            if player_sum < computer_sum:
                win_message = "You lost! :("
            game_ended = True

    print(f"Your final hand: {player_cards}")
    print(f"Computer's final hand: {computer_cards}")
    print(win_message)

    continue_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y'
