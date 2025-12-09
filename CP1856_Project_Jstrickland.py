import db
import random
import sys

def check_money(player_money):
    if player_money < 5:
        choice = input("Your funds are insufficient. Would you like to purchase more? (Y/N): ").lower()
        if choice == "y":
            while True:
                try:
                    amount = float(input("How many funds would you like to add?:"))
                    if amount <= 0:
                        print("Please enter a number greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Please enter a vlaid number.")
            player_money += amount
            db.write_money(player_money)
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

def do_hit_or_stand(deck, player_hand):
    answer = input("\nHit or stand?: ").lower()
    if answer == "hit":
        draw_card_player(deck, player_hand)
        print(f"\nYou've been dealt the {player_hand[-1][1]} of {player_hand[-1][0]}")
        print("\nYour Hand")
        for card in player_hand:
            suit, rank, value = card
            print(f"{rank} of {suit}")
    elif answer == "stand":
        return "stand"
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")

def player_win(wager, player_money):
    winnings = wager * float(1.5)
    print(f"You've won ${winnings}")
    return player_money + winnings

def compare_hands(player_total, dealer_total):
    if player_total > dealer_total:
        return "win"
    elif player_total < dealer_total:
        return "lose"
    elif player_total == dealer_total:
        return "tie"

def check_total_player(player_hand):
    total = sum(row[2] for row in player_hand)
    return total

def check_total_dealer(dealer_hand):
    total = sum(row[2] for row in dealer_hand)
    return total

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
                value = 11
            card = [suit, rank, value]
            deck.append(card)
    return deck

def draw_card_dealer(deck, dealer_hand):
    draw = random.randint(0, len(deck)-1)
    drawn_card = deck[draw]
    deck.pop(draw)

    suit, rank, value = drawn_card

    if rank == "Ace":
        total = sum(card[2] for card in dealer_hand)
        if total + 11 > 21:
            value = 1

    dealer_hand.append((suit, rank, value))
    
def draw_card_player(deck, player_hand):
    draw = random.randint(0, len(deck)-1)
    drawn_card = deck[draw]
    deck.pop(draw)

    suit, rank, value = drawn_card

    if rank == "Ace":
        total = sum(card[2] for card in player_hand)
        if total + 11 > 21:
            value = 1
            print(f"You've been dealt the Ace of {suit}. To prevent a bust, it's value is 1.")
        else:
            while True:
                choice = input("You've been dealt an Ace! Will its value be 1 or 11?")
                if choice == "1" or choice == "11":
                    value = int(choice)
                    break
                else:
                    print("Invalid choice. Please type 1 or 11.")
    player_hand.append((suit, rank, value))
            

def dealer(dealer_hand, deck, player_total, wager, player_money):
    print(f"The dealer shows their other card, the {dealer_hand[1][1]} of {dealer_hand[1][0]}.")
    while True:
        dealer_total = check_total_dealer(dealer_hand)
        if dealer_total > 21:
            print("Dealer bust! Congratulations, you've won this round!")
            win = player_win(wager, player_money)
            db.write_money(player_money)
            break
        elif dealer_total < 17:
            draw_card_dealer(deck, dealer_hand)
            print(f"\nThe dealer drew the {dealer_hand[-1][1]} of {dealer_hand[-1][0]}")
            print("\nDealer's Hand")
            for card in dealer_hand:
                suit, rank, value = card
                print(f"{rank} of {suit}")
        else:
            compare = compare_hands(player_total, dealer_total)
            if compare == "win":
                print("Congratulations, you've beaten the dealer!")
                win = player_win(wager, player_money)
            elif compare == "lose":
                print("Sorry, the dealer wins this round. You lose!")
            elif compare == "tie":
                print("It's a tie! Wagers returned.")
                player_money += wager
                db.write_money(player_money)
            break
    return player_money

def main():
    player_money = db.read_money()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    
    while True:
        player_hand = [] 
        dealer_hand = []
        deck = make_cards()
        
        print(f"\nMoney: ${player_money}")

        player_money = check_money(player_money)
        wager = get_wager(player_money)
        player_money -= wager
        print(f"You've wagered ${wager}")

        for i in range(2):
            draw_card_dealer(deck, dealer_hand)
        print(f"\nThe dealer has drawn 2 cards, and reveals the {dealer_hand[0][1]} of {dealer_hand[0][0]}.")

        for i in range(2):
            draw_card_player(deck, player_hand)
        print(f"\nThe dealer has dealt you the...\
        \n{player_hand[0][1]} of {player_hand[0][0]}\
        \nand the {player_hand[1][1]} of {player_hand[1][0]}.")

        while True:
            hit_or_stand = do_hit_or_stand(deck, player_hand)
            player_total = check_total_player(player_hand)
            
            if hit_or_stand == "stand":
                break

            if player_total > 21:
                print("\nBust! Your total is higher than 21... Sorry, you lose.")
                break
            
        if player_total <= 21:
            dealer(dealer_hand, deck, player_total, wager, player_money)
        else:
            db.write_money(player_money)
            
            
        db.write_money(player_money)
        print(f"\nNew balance: ${player_money}")
        play_again = input("\nWould you like to play again? (Y/N): ").lower()
        if play_again != "y":
            print("Thanks for playing! Bye!")
            break

if __name__ == "__main__":
    main()
