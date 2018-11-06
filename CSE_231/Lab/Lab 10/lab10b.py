import cards

# Create the deck of cards

the_deck = cards.Deck()
the_deck.shuffle()



player1_deck = []
player2_deck = []
for i in range(5):
    player1_deck.append( the_deck.deal() )
    player2_deck.append( the_deck.deal() )


answer = ""
while len(player1_deck) != 0 and len(player2_deck) != 0 and answer.lower() != 'n':
    player1_card = player1_deck.pop( 0 )

    print( "First card dealt to player #1:", player1_card )




    player2_card = player2_deck.pop( 0 )

    print( "First card dealt to player #2:", player2_card )
    player1_rank = player1_card.rank()
    player2_rank = player2_card.rank()
    if player1_rank == 1:
        player1_rank = 14
    if player2_rank == 1:
        player2_rank = 14
    print()
    if player1_rank == player2_rank:
        print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
        player1_deck.append(player1_card)
        player2_deck.append(player2_card)
        print("Hand 1: ", player1_deck)
        print("Hand 2: ", player2_deck)
        answer = input("Keep playing? (y/n)")
    elif player1_rank > player2_rank:
        print( "Player #1 wins:", player1_card, "of higher rank than", player2_card )
        player1_deck.append(player1_card)
        player1_deck.append(player2_card)
        print("Hand 1: ", player1_deck)
        print("Hand 2: ", player2_deck)
        answer = input("Keep playing? (y/n)")
    else:
        print( "Player #2 wins:", player2_card, "of higher rank than", player1_card )
        player2_deck.append(player1_card)
        player2_deck.append(player2_card)
        print("Hand 1: ", player1_deck)
        print("Hand 2: ", player2_deck)
        answer = input("Keep playing? (y/n)")
if len(player1_deck) > len(player2_deck):
    print("Player 1 wins!!!")
elif len(player2_deck) > len(player1_deck):
    print("Player 2 wins!!!")    
elif len(player1_deck) == len(player2_deck):
    print("It's a tie")