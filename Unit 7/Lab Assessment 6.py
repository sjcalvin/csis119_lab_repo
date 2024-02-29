# We will need to use the random package. Let's import that.
import random 

#### Task #01 Create Deck
def create_standard_deck():

    # Define a list to hold the suits.
    suits = ['hearts', 'clubs', 'spades', 'diamonds']

    # And, define a list to hold the card values.
    values = list(range(2, 15))  # 2 to 14 inclusive, representing 2 to Ace

    # Next, define a list comprehension containing a tuple, representing each card.
    deck = [(suit, value) for suit in suits for value in values]

    # Lastly, sort the cards.
    deck.sort()  # Sorting the deck in alphabetical order of suits and ascending order of values

    # Return the list of card tuples.
    return deck

# Task #02 Define a function for dealing a card from the deck to the dealer and players.
def draw_card(deck):

    # Choose a random card (tuple from the deck.)
    card = random.choice(deck)
    
    # Remove the card from from the deck.
    deck.remove(card)

    # Return the card.
    return card    

# Task #03 Determine if the player has won, lost, or has room to hit.
def get_points(hand):

    # Get the value of the hand before checking if the card is an ace.
    points = sum(card[1] if card[1] <= 10 else 1 for card in hand)

    # Iterate through the cards in the hand.
    for card in hand:

        # If the card is a face card...
        if 11 <= card[1] < 14:

            # Add 9 to the card's points to bring the card's total points to ten.
            points += 9

        # If the card is an ace and using it as 11 doesn't break the hand...
        elif card[1] == 14 and points + 10 <= 21:

            # Add ten to the card's points to bring the ace's value to 11.
            points += 10

    # Return the hand's points.
    return points

# Task #04 Define a function to check if the player has won, lost, or has room to hit.
def check_cards(player):

    # Calculate the player's score.
    score = get_points(player)

    # If the the score is 21...
    if score == 21:

        # Return "WIN."
        return 'WIN'
    
    # If the score is greater than 21...
    elif score > 21:

        # Retrun "BUST."
        return 'BUST'
    
    # Otherwise...
    else:

        # Return "OK."
        return 'OK'

# Main Blackjack Game
def create_blackjack_game():
    '''
    result == 1 Player Wins.
    result == 
    
    '''
    # FIRST SECTION INSERT YOUR CODE HERE.

    # Define an empty list for the player and the dealer.
    player = []
    dealer = []

    # Generate a deck.
    deck = create_standard_deck()

    # Draw two cards for each player
    player.append(draw_card(deck))
    dealer.append(draw_card(deck))

    player.append(draw_card(deck))
    dealer.append(draw_card(deck))

    # Display initial hands
    display_player(player)
    display_dealer(dealer, start=True)

    # Calculate initial score
    player_count = get_points(player)
    dealer_count = get_points(dealer)

    # SECOND SECTION INSERT YOUR CODE HERE
    
    # Infinite Loop to drive the program.
    while True:

        # Get user input.
        player_action = input('Do you want to hit (h) or stay (s)? Enter (q) to quit: ')

        # If the player wants to quit the game...
        if player_action.lower() == 'q':
            
            # Return 0.
            return 0

        # If the player wants to hit.
        if player_action.lower() == 'h':

            # Draw another card.
            player.append(draw_card(deck))

            # Then display the player's hand.
            display_player(player)

            # Check if the player has won, busted, or is still in the game.
            result = check_cards(player)

            # If the player wins...
            if result == 'WIN':

                # Return 1.
                return 1
            
            # If the player busts...
            elif result == 'BUST':

                # Return -1.
                return -1

        # If the player decides to stay.
        elif player_action.lower() == 's':

            # Break the loop.
            break
        
        # For any other input.
        else:

            input('Invalid input. Do you want to hit (h) or stay (s)? Enter (q) to quit: ')

    # THIRD SECTION INSERT YOUR CODE HERE
            
    # Dealer Logic.
            
    # While the dealer_count is less than 17...
    while dealer_count < 17:

        # Draw a new card.
        dealer.append(draw_card(deck))

        # Display the dealer's hand.
        display_dealer(dealer)

        # Check if the dealer has won, busted, or is still in the game.

        # Check the Dealer's hand.
        result = check_cards(dealer)

        # If the result is a win...
        if result == 'WIN':

            # Return -1 dealer wins.
            return -1
        
        # If the result is a bust,
        elif result == 'BUST':

            # Return 1 dealer busts.
            return 1 

    # Final comparison to determine the winner
    # Player wins.
    if player_count > dealer_count:

        return 1
    
    # Dealer Wins
    elif player_count < dealer_count:
        
        return -1
    
    # Dealer wins in the case of a tie.
    else:
        return -1

# Display functions for UI.
# Player.
def display_player(player):

    # Print the player's hand.
    print(f"Player's hand: {player}")

# Dealer.
def display_dealer(dealer, start=False):
    
    # If the dealer is starting.
    if start:

        # Print the dealer's hand with the last card facing down.
        print(f"Dealer's hand: [{dealer[0]}, 'X']")
    
    # Otherwise...
    else:

        # Print the dealer's hand.
        print(f"Dealer's hand: {dealer}")

# Main Program.
def main():

    # Play the game.
    result = create_blackjack_game()

    # If the result is 1...
    if result == 1:

        # The player wins!
        print ('Player Wins!')

    # If the result is -1...
    elif result == -1:

        # The Dealer Wins.
        print('Dealer Wins!')

    # Otherwise:
    else:

        # The player quitted the game.
        print('Game quitted.')

if __name__ == '__main__':

    main()
    