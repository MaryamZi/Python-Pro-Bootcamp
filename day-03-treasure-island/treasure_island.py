print('''
*******************************************************************************
************************ "Welcome to Treasure Island." ************************
*******************************************************************************
''')
print("Your mission is to find the treasure.")
at_crossroad = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\". ").lower()
at_lake = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()
at_island = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which colour do you choose? ").lower()

if at_crossroad == "left" and at_lake == "wait" and at_island == "yellow":
    print("Congratulations! You won!")
else:
    print("Game Over! :(")
