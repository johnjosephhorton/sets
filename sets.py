# This code checks whether there are any sets in an arrangement of cards.
# Authors: John and Ada Horton
# Date: November 16th, 2018

import itertools

# Card dimensions
colors = ["red", "green", "purple"]
shadings = ["empty", "striped", "solid"]
shapes = ["oval", "squiggle", "diamond"]
numbers = ["one", "two", "three"]

# Create cards w/ index. Label your cards with these numbers. 
counter = 1 
cards = {}
for color in colors:
    for shading in shadings:
        for shape in shapes:
            for number in numbers:
                cards[counter] = {"color":color, "shading":shading, "shape":shape, "number": number}
                counter += 1

# Tests whether cards make up a set 
def IsSet(cards):
    keys = ["color", "shading", "shape", "number"]
    for key in keys:
        attributes = [card[key] for card in cards]
        num_unique = len(set(attributes))
        if num_unique == 3 or num_unique == 1:
            pass
        else:
            return False
    return True

# Enter the card indices here - it will then print out the sets (if any)
deck = [41, 40, 78, 28, 23, 80, 59, 38, 9, 65, 1, 14]
for x in itertools.combinations(deck,3):
    potential_set = [cards[i] for i in x]
    if IsSet(potential_set):
        print(x)

        



