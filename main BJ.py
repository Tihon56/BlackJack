import random as r
import os

deck = [2,3,4,5,6,7,8,9,10,11,12,13,14]*4

#def for clearing terminal
def clear_console():
    os.system('cls')

#def for making starting hand
def make_a_hand (deck):
    hand = []
    for i in range(2):
        r.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

# def for counting points
def at_all (hand):
    at_all = 0
    for card in hand:
        if card=="J" or card=="Q" or card=="K": at_all+=10 #for pictures
        #condition for ace
        if card=="A":
            if at_all>=11:at_all+=1
            else: at_all+= 11
        if card!= "J" and card!= "Q" and card!= "K" and card != "A": at_all+=int(card)
    return at_all

# def for adding card in hand
def one_more(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

#dealer mind
def dealer_action(player_hand, dealer_hand):
    player_points = at_all(player_hand)
    dealer_points = at_all(dealer_hand) 
    while player_points>dealer_points and dealer_points<21:
         if player_points>21:break
         player_points = at_all(player_hand)
         dealer_points = at_all(dealer_hand)
         dealer_hand = one_more(dealer_hand)
    return (dealer_hand)

#final round
def final(player_hand,dealer_hand):
    player_points = at_all(player_hand)
    dealer_points = at_all(dealer_hand)
    if dealer_points>21 and player_points>21:
        if player_points > dealer_points: print('dealer won, you take too much')
        if player_points < dealer_points: print('player won, dealer tried his luck')
        if player_points == dealer_points: print('Draw! Guys it was...')
    if dealer_points>21 and player_points<=21:print('player won, dealer ate too much')
    if dealer_points<=21 and player_points>21:print('dealer won, player dont be jealous')
    if dealer_points<=21 and player_points<=21:
        if player_points > dealer_points: print('player won')
        if player_points < dealer_points: print('dealer won')
        if player_points == dealer_points: print('Draw!')
        

#game
def game():
    while True:
        #clearing main parametrs if player restarts
        dealer_hand = []
        player_hand = []
        choice = ''
        points = 0
        #game has begin
        print ("Welcome to BJ!")
        dealer_hand = make_a_hand(deck)
        player_hand = make_a_hand(deck)
        print(f'player hand:{player_hand}')
        print(f'dealer hand: {dealer_hand[1]}, ? ')
        #main block of the game
        while True:
            points = at_all(player_hand)
            #if he lose, we should stop player
            if points>21:
                print('you take too much')
                break
            print(f'you have {points} , would u take a card(y|n)?')
            add =''
            add = input()
            if add=='y':
                one_more(player_hand)
                print(f'Dealer hand: {dealer_hand[1]} , ? ')
                print(player_hand)
            elif add=='n':break
            else:
                clear_console()
                print("Are u stupid or what? Let,s try again.")
        dealer_action(player_hand,dealer_hand)
        final(player_hand,dealer_hand)
        print('print (y) if you want play again')
        choice = input()
        if choice == 'y':
            clear_console()
            pass
        else:break
print('Welcome Creator')
game()
        




                


