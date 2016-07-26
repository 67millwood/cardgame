# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
import itertools, random

# make a deck of cards

number_deck = list(itertools.product(range(2,11),['Spades','Hearts','Diamonds','Clubs']))
face_deck = list(itertools.product(['Jack', 'Queen', 'King', 'Ace'], ['Spades','Hearts','Diamonds','Clubs']))
deck = number_deck + face_deck

# print number_deck
# print face_deck
# print deck

# shuffle the cards
random.shuffle(deck)

# draw five cards
# print("You got:")
# for i in range(2):
#    print(deck[i][0], "of", deck[i][1])
   

 