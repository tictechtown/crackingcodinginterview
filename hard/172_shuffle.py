"""
Shuffle: 
Write a method to shuffle a deck of cards. 
It must be a perfect shuffle-in other words, each of the 52! permutations of the deck has to be equally likely. Assume that you are given a random number generator which is perfect.
"""

import random


def shuffle_card(deck: list[int]) -> list[int]:

    for i in range(len(deck)):
        swap_i = random.randint(0, i)
        (deck[i], deck[swap_i]) = (deck[swap_i], deck[i])

    return deck
