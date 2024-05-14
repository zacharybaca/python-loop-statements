"""Task 1: Random Choice Game
Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not."""

import random

list_of_items = ["computer", "mobile phone", "xbox", "car"]

users_guess = input("Which Item Was Picked at Random: ")

random_choice = random.choice(list_of_items)

print(random_choice)

if random_choice == users_guess:
    print("Congratulations! You Guessed Right")
else:
    print("I'm Sorry. Your Guess is Incorrect")