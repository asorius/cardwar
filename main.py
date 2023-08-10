from copy import copy
from dataclasses import dataclass
import re
import sys
import random


def main():
    deck = Deck().randomized_deck
    mid_index = int(len(deck) / 2)
    player_one = Player(deck[:mid_index])
    player_two = Player(deck[mid_index:])
    try:
        while True:
            player_one_card: Card = player_one.get_top_card()
            player_two_card: Card = player_two.get_top_card()
            print(
                f"Player one draws {player_one_card} ({len(player_one.deck) } cards left)"
            )
            print(
                f"Player two draws {player_two_card} ({len(player_two.deck)} cards left)"
            )
            if player_one_card.value == player_two_card.value:
                print("War is on!")
                war(player_one, player_two)
            elif player_one_card.value > player_two_card.value:
                player_one.deck.append(player_two_card)
                print(f"• Player one gets {player_two_card}")
            else:
                player_two.deck.append(player_one_card)
                print(f"• Player two gets {player_one_card}")

            if not player_one.deck:
                print("*** Player one is out of cards. PLAYER TWO WINS")
                break
            if not player_two.deck:
                print("*** Player two is out of cards. PLAYER ONE WINS")
                break
            input("♥ ♦ ♣ ♠ Press enter to initiate next round ♥ ♦ ♣ ♠ ")
    except EOFError:
        sys.exit("\nExiting program..")
    except KeyboardInterrupt:
        sys.exit("\nExiting program..")


@dataclass
class Card:
    name: str = ""
    value: int = 2
    suit: str = ""

    def __str__(self):
        return f"{self.name} of {self.suit}"


class Deck(Card):
    @property
    def base(self):
        SUITS = {
            "hearts": "♥",
            "diamonds": "♦",
            "clubs": "♣",
            "spades": "♠",
        }
        CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        deck = []
        for suit, suit_char in SUITS.items():
            for val in CARD_VALUES:
                match val:
                    case 14:
                        deck.append(Card(suit=suit_char, value=val, name="Ace"))
                    case 13:
                        deck.append(Card(suit=suit_char, value=val, name="King"))
                    case 12:
                        deck.append(Card(suit=suit_char, value=val, name="Queen"))
                    case 11:
                        deck.append(Card(suit=suit_char, value=val, name="Jack"))
                    case _:
                        deck.append(Card(suit=suit_char, value=val, name=str(val)))
        return deck

    @property
    def randomized_deck(self):
        randomized_list = copy(self.base)
        random.shuffle(randomized_list)
        return randomized_list


class Player:
    def __init__(self, deck: list[Card]):
        self.deck = deck

    def get_top_card(self):
        return self.deck.pop()

    def get_multiple_cards(self, amount: int):
        deleted_items = []
        for _ in range(amount):
            deleted_items.append(self.deck.pop())
        return deleted_items


def war(player_one: Player, player_two: Player):
    if len(player_one.deck) < 2:
        print("Player one is out of cards. PLAYER ONE WINS")
        return
    if len(player_two.deck) < 2:
        print("Player two is out of cards. PLAYER ONE WINS")
        return

    mystery_card_one, player_one_card = player_one.get_multiple_cards(2)
    mystery_card_two, player_two_card = player_two.get_multiple_cards(2)
    print("(War-mode) Player one draws card and places it down.")
    print(
        f"(War-mode) Player one draws {player_one_card} ({len(player_one.deck) } cards left)"
    )
    print("(War-mode) Player two draws card and places it down.")
    print(
        f"(War-mode) Player two draws {player_two_card} ({len(player_two.deck)} cards left)"
    )
    if player_one_card.value == player_two_card.value:
        print("*** War is on! ***")
        war(player_one, player_two)
    elif player_one_card.value > player_two_card.value:
        player_one.deck.append(mystery_card_two)
        player_one.deck.append(player_two_card)
        print(f"(War-mode) • Player one gets {mystery_card_two} {player_two_card}")
    else:
        player_two.deck.append(mystery_card_one)
        player_two.deck.append(player_one_card)
        print(f"(War-mode) • Player two gets { mystery_card_one} {player_one_card}")


if __name__ == "__main__":
    main()
