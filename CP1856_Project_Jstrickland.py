import random

def wager():
    player_money = 100.00
    while True
        player_wager = float(input("How much would you like to bet?: ")
            if player_wager > player_money:
                print("Insufficient funds. Please try again.")
            elif player_wager <= 0:
                print("Enter a number greater than 0. Please try again.")
            else:
                player_money -= player_wager
                break

def cards():
    suit = ["Diamonds", "Hearts", "Clubs", "Spades"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "1"]

def main():
    print("BLACKJACK!")

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


           
