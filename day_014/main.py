import random

from art import logo, vs
from data import data


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def main():
    print(logo)
    score = 0
    game_should_continue = True

    # Generate a random account from the game data
    account_b = random.choice(data)

    # Make the game repeatable
    while game_should_continue:
        # Making account at position B become the next account at position A
        account_a = account_b
        account_b = random.choice(data)

        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Clear the screen
        print("\n" * 20)
        print(logo)

        # Get follower count for each account
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # Check if user is correct
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Give user feedback on their guess and keep the score
        if is_correct:
            score += 1
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False


main()
