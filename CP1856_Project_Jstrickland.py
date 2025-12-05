import db
import random
import sys

def check_money(player_money):
    if player_money < 5:
        choice = input("Your funds are insufficient. Would you like to purchase more? (Y/N): ").lower()
        if choice == "y":
            amount = float(input("How many funds would you like to add?:"))
            player_money += amount
            write_money(player_money)
        return player_money

def get_wager(player_money):
    while True:
        try:
            wager = float(input("Bet amount: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if wager > player_money:
            print("Insufficient funds. Please try again.")
        elif wager < 5:
            print("Minimum bet is $5. Please enter a valid number greater than 5.")
        elif wager > 1000:
            print("Maximum bet is $1,000. Please enter a valid number less than 1000.")
        else:
            return wager    

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

def draw_card_dealer(deck, dealer_hand):
    draw = random.randint(0, len(deck))
    drawn_card = deck[draw]
    dealer_hand.append(drawn_card)
    deck.pop(draw)
    
def draw_card_player(deck, player_hand):
    draw = random.randint(0, len(deck))
    drawn_card = deck[draw]
    player_hand.append(drawn_card)
    deck.pop(draw)

def main():
    player_hand = []
    dealer_hand = []
    player_money = db.read_money()
    deck = make_cards()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    print(f"\nMoney: ${player_money}")
    wager = get_wager(player_money)
    player_money -= wager
    print(f"You've wagered ${wager}")

    for i in range(2):
        draw_card_dealer(deck, dealer_hand)
    print(f"The dealer has drawn 2 cards, and reveals the {dealer_hand[0][1]} of {dealer_hand[0][0]}.")

    for i in range(2):
        draw_card_player(deck, player_hand)
    print(f"\nThe dealer has dealt you the\
    \n{player_hand[0][1]} of {player_hand[0][0]}\
    \nand the {player_hand[1][1]} of {player_hand[1][0]}.")

    while True:
        hit_or_stand = input("Hit or stand?: ").lower()
        if hit_or_stand == "hit":
            draw_card_player(deck, player_hand)
            print("\nYour Hand")
            for card in player_hand:
                suit, rank, value = card
                print(f"{rank} of {suit}")
        else:
            continue
    
    win = random.choice([True, False])

    if win:
        winnings = wager * float(1.5)
        print(f"You've won ${winnings}")
        player_money += winnings
    else:
        print("You lose :(")

    db.write_money(player_money)
    print(f"New balance: ${player_money}")


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

''' TODO --
    1. Implement gameplay.
        c. hit or stand mechanic.
        d. bust
        e. compare hands
        f. win or lose
'''
           
