import random

def wager():
    player_money = 100.00
    while True:
        player_wager = float(input("How much would you like to bet?: "))
        if player_wager > player_money:
            print("Insufficient funds. Please try again.")
        elif player_wager <= 0:
            print("Enter a number greater than 0. Please try again.")
        else:
            player_money -= player_wager
            break    

def make_cards():
    suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []
    for suit in suits:
        for rank in ranks:
            if rank == "2":
                value = 2
            elif rank == "3":
                value = 3
            elif rank == "4":
                value = 4
            elif rank == "5":
                value = 5
            elif rank == "6":
                value = 6
            elif rank == "7":
                value = 7
            elif rank == "8":
                value = 8
            elif rank == "9":
                value = 9
            elif rank == "10":
                value = 10
            elif rank == "Jack":
                value = 10
            elif rank == "Queen":
                value = 10
            elif rank == "King":
                value = 10
            elif rank == "Ace":
                value = 1
            card = [suit, rank, value]
            deck.append(card)
    return deck

def draw_card(deck, player_hand):
    draw = random.randint(0, len(deck))
    drawn_card = deck[draw]
    player_hand.append(drawn_card)
    deck.pop(draw)
    
def main():
    player_hand = []
    dealer_hand = []
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    deck = make_cards()
    print(deck)
    draw_card(deck, player_hand)
    draw_card(deck, player_hand)
    draw_card(deck, player_hand)
    draw_card(deck, player_hand)
    draw_card(deck, player_hand)
    print(f"Player Hand: {player_hand}")

if __name__ == "__main__":
    main()


'''
Gameplay --
    1. Player bets an amount of money at the start of the game.
        a. Set player money at the beginning of the game and carry it throughout.
        b. If the player loses, they lose that amount. If they win they get back 1.5x the amount.

    2. Get cards
        a. Dealer gets TWO cards at the start. One is revealed and one is hidden.
           The dealer's turn occurs after the player's turn, then they show the other card.
        b. Dealer also has to hit (draw) if their hand total is less than 16. Dealer
           must stand (stop) on any total of 17 or higher.

    3. Hit or Stand
        a. Player chooses to hit or stand each turn.

    4. Win or Lose
        a. Get a higher total than the dealer to win.
        b. Exceeding 21 is an automatic loss.
'''


           
