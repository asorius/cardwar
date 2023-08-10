from copy import copy
from dataclasses import dataclass
import re
import sys
import random


def main():
    # deck = Deck().randomized_deck
    player_one = Player(Deck().randomized_deck)
    player_two = Player(Deck().randomized_deck)


@dataclass
class Card:
    name: str = ""
    value: int = 2
    suit: str = ""

    def __str__(self):
        return f"{self.value} of {self.name}"


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
    def __init__(self, deck):
        self.deck = deck

    def get_card_from_top(self, amount: int):
        deleted_items = []
        for _ in range(amount):
            deleted_items.append(self.deck.pop())
        return deleted_items


if __name__ == "__main__":
    main()
