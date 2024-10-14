import random

from blackjack_art import logo


def deal_cart():
    """
    Returns a random card from the deck.

    :return: A randomly selected card from the deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    Take a list of cards and return the score calculated from the cards

    :param cards: List of integers representing the cards in hand.
    :return: The score of the hand. Returns 0 if the hand is a Blackjack (21 with 2 cards).
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """
    Compares the user score u_score against the computer score c_score.

    :param user_score: Integer representing the user's score.
    :param computer_score: Integer representing the computer's score.
    :return: A string indicating the result of the comparison.
    """
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """
    Play a game of Blackjack between the user and the computer.

    The function initializes the game, deals the initial cards, and handles the game logic
    including user inputs and determining the winner.

    :return: None
    """
    print(logo)
    user_cards = []
    user_score = -1
    computer_cards = []
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cart())
        computer_cards.append(deal_cart())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_cart())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cart())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
