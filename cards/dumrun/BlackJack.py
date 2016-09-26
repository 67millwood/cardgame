import carddeck
import itertools, random

player_total = 0
p_number = 0
dealer_total = 0
d_number = 0
ace_is_one = 0
five_card_win = False
# Dealing the first 2 cards
print "Your first two cards are:"
count = 0
for i in range(2):
	print carddeck.deck[i]
	count += 1
	# this pulls out the number from the 2D list pair and then makes it an integer so we can add them up
	# this is done a bunch of times throughout the program
	if carddeck.deck[i][0] in ['King', 'Queen', 'Jack']:
		number = 10
	elif carddeck.deck[i][0] == 'Ace':
		number = 11
		ace_is_one -= 10
	else: 
		number = int(carddeck.deck[i][0])

	player_total += number

if player_total == 22:
	print "Two Aces...wow.  Your total after 2 cards is 12"	
	player_total = 12
	ace_is_one = 0

else:
	print "Your total after 2 cards is: ", player_total

# Dealing the player more cards
while count < 5:
	choice = raw_input ("Would you like another card?")
	if choice in ['y', 'yes', 'Y', 'Yes']:
		print "Here is card number ", (count + 1), " ", carddeck.deck[count + 1]
		count += 1
	
		if carddeck.deck[count][0] in ['King', 'Queen', 'Jack']:
			number = 10
		elif carddeck.deck[count][0] == 'Ace':
			number = 11
			ace_is_one -= 10
		else: 
			number = int(carddeck.deck[count][0])
		
		player_total += number
		
		if player_total > 21:
			if ace_is_one < 0:
				player_total += ace_is_one
				print "Now you have: ", player_total
				ace_is_one = 0
			else:
				print "You busted with ", player_total
				break
		else:
			print "Now you have: ", player_total
	else:
		break
else:
	print "You have 5 cards.  You win!"
	five_card_win = True
	
# Dealer Cards
ace_is_one = 0
raw_input ("Ready for the Dealer?  Press ENTER >")
print "Dealer cards are:"
for i in range(2):
	print carddeck.deck[i+count + 1]
	
	if carddeck.deck[i+count + 1][0] in ['King', 'Queen', 'Jack']:
		number = 10
	elif carddeck.deck[i+count + 1][0] == 'Ace':
		number = 11
		ace_is_one -= 10
	else: 
		number = int(carddeck.deck[i+count + 1][0])

	dealer_total += number
	
if dealer_total == 22:
	print "Two Aces...wow.  Dealer total after 2 cards is 12"	
	dealer_total = 12
	ace_is_one = 0
else:
	print "Dealer total after 2 cards is: ", dealer_total

# Dealer additional cards
# Dealer must hit on 16 or lower

while dealer_total <= 16:
	print "Dealer must take another card...."
	raw_input ("Press ENTER to deal > ")
	print "Dealer draws a :", carddeck.deck[count + 3]
	
	if carddeck.deck[count + 3][0] in ['King', 'Queen', 'Jack']:
		number = 10
	elif carddeck.deck[count + 3][0] == 'Ace':
		number = 11
		ace_is_one = -10
	else: 
		number = int(carddeck.deck[count + 3][0])
	
	# this deals with the ace being worth 11 or 1
	# if the person is over 21, it sets the value of the Ace back to 1 from 11 and retotals
	dealer_total += number
	if dealer_total > 21:
		if ace_is_one < 0: 
			dealer_total += ace_is_one
			print "Dealer has: ", dealer_total
			ace_is_one = 0
		else:
			print "Dealer is busted"
			break
	else:
		print "Dealer now has: ", dealer_total
	count += 1
else:
	print "Dealer stands with: ", dealer_total
		
# Who wins?

raw_input ("Press ENTER to see who wins >")
if dealer_total > 21 and player_total > 21: 
	print "You and the House busted...but that means you lose"
elif dealer_total > 21:
	print "House busted...you win."
elif player_total > 21:
	print "You busted....House wins."
elif player_total == 21:
	print "21...winner winner chicken dinner"
elif five_card_win == True:
	print "Player had 5 cards...automatic win"
elif dealer_total == player_total:
	print "House wins on a push."
elif dealer_total > player_total:
	print "You got destroyed"
else:
	print "Player wins with:", player_total

		

	
	
	
	
	
	
