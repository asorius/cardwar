import re
import sys


def main():
    suit_card_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    deck = []
    for _ in range(4):
        for val in suit_card_values:
            deck.append(val)
    print(deck)


if __name__ == "__main__":
    main()
