import time
import random
import os

class Player:
    #Here is where you name the player and select the games you want to play it will display also your current currency

    def __init__(self, name):
        self.name = name
        self.wallet = 500
        self.items = []

    def __repr__(self):
        return "{} currently holds ${} and has purchased these items: \n {}".format(self.name, self.wallet, self.items)
        



class Casino:


    def __init__(self, player):
        self.player = player
        self.casino_shop = {
            "Toy Car": 2000,
            "Python Course": 5000,
            "Brand New Desktop PC": 10000,
            "Ford Fiesta": 50000,
            "Mansion": 750000,
            "Unicorn": 1500000,
            "The Casino": 10000000
        }
        self.win_condition = False

    def show_shop(self):
        clearConsole()
        print("\n***** Welcome to the Shop! *****")
        for item, price in self.casino_shop.items():
            print(f"{item}: ${price}")
        print("\n")
    
    def purchase_item(self):
        clearConsole()
        self.show_shop()
        while True:
            item = input("Hello, Hello \n What would you like to buy? Enter the name (or type 'exit' to go back): ").strip()
            if item.lower() == "exit":
                break
            if item in self.casino_shop:
                price = self.casino_shop[item]
                if self.player.wallet >= price:
                    self.player.wallet -= price
                    self.player.items.append(item)
                    self.casino_shop.pop(item)
                    print(f"Congrats! You've bought a {item}. Your new balance is ${self.player.wallet}.")
                else:
                    print(f"Sorry, you don't have enough money to buy {item}.")
            else:
                print("Invalid item. Please try again.")
    

    def coin_game(self):
        clearConsole()
        print("************************************************")
        print("[******** - WELCOME TO FLIP THE COIN - ********]")
        print("************************************************")

        chance = random.randint(1, 2)  # Random outcome for heads or tails

        while True:
            try:
                # Asking the user for a valid bet
                bet = int(input("How much money are you willing to bet today? "))
                if bet > self.player.wallet:
                    print(f"Invalid bet amount. You have only ${self.player.wallet}.")
                elif bet <= 0:
                    print("Bet amount must be greater than zero.")
                else:
                    print(f"Bet placed: ${bet}")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Player choice input loop
        while True:
            player_input = input("Please choose Heads(H) or Tails(T): ").upper()
            if player_input not in ["H", "T"]:
                print("Invalid input. Please try again.")
                continue
            
            player_input = 1 if player_input == "H" else 2
            if player_input == chance:
                print("Congratulations! You won the toss!")
                self.player.wallet += bet * 2
            else:
                print("Sorry, you lost the toss.")
                self.player.wallet -= bet
            break
    
    def horse_betting(self):
        clearConsole()
        print("************************************************")
        print("[******** - WELCOME HORSE BETTING - ********]")
        print("************************************************")
        
        horses_list = ["Mulan", "Jack The Trecherous", "Bolt The Daredevil" , "Billy The Fool", "Star Platinum", "Dio The World", "Mob The Pyscho", "Vaundy The Empress", "Kim Possible", "Jay, the Donkey(Technically not a Horse)"]
        
        winners = random.sample(horses_list, len(horses_list))
        last_place = winners[-1]

        while True:
            print(horses_list, "\n")
            selected_horse = input("Please Select a Horse: ")
            if selected_horse not in horses_list:
                print("There is no horse named:", selected_horse)
                continue
            else:
                break
        print("[******** - Horse Betting Special Rules - ********]")
        print("1st Place: x7.5 Multiplier \n 2nd Place: x4 Multiplier \n 3rd Place: No Money Loss \n Last Place: Double Loss")

        while True:
            try:
                bet = int(input("How much money are you willing to bet today? "))
                print(f"You currently have ${self.player.wallet}")

                # Check if bet is within wallet balance
                if bet > self.player.wallet:
                    print("Invalid bet amount. Please bet within your wallet balance.")
                    print(f"You currently have ${self.player.wallet}")
                elif bet <= 0:
                    print("Bet amount must be greater than zero.")
                else:
                    break  # Valid bet; exit the loop
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if winners[0] == selected_horse:
            print("🎉Congratulations you came in 1st place!!")
            self.player.wallet += bet*7.5
        elif winners[1] == selected_horse:
            print("🎉Congratulations you came in 2nd place!!")
            self.player.wallet += bet*4
        elif winners[2] == selected_horse:
            print("🎉Congratulations you came in 3rd place!!")
        elif last_place == selected_horse:
            print("😞Oh no you came in Last")
            self.player.wallet -= bet*2
        else:
            print("Better luck next time. Your horse did not place in the top 3.")
            self.player.wallet -= bet

    def blackjack(self):
        clearConsole()
        print("************************************************")
        print("[******** - WELCOME TO BLACKJACK - ********]")
        print("************************************************")

        dealer_first_card = random.randint(1, 11)
        dealer_second_card = random.randint(1, 11)
        your_first_card = random.randint(1, 11)
        your_second_card = random.randint(1, 11)

        while True:
            try:
                bet = int(input("How much money are you willing to bet today? "))
                print(f"You currently have ${self.player.wallet}")

                # Check if bet is within wallet balance
                if bet > self.player.wallet:
                    print("Invalid bet amount. Please bet within your wallet balance.")
                    print(f"You currently have ${self.player.wallet}")
                elif bet <= 0:
                    print("Bet amount must be greater than zero.")
                else:
                    break  # Valid bet; exit the loop
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        
        print("Dealer is handing out cards...")
        time.sleep(2)
        player_total = your_first_card + your_second_card
        dealer_total = dealer_first_card + dealer_second_card
        print("************************************************")

        # Show initial player cards and dealer's first card
        print(f"Your cards: {your_first_card} and {your_second_card}, total: {player_total}")
        print(f"Dealer's visible card: {dealer_first_card}")

        win = bet * 3
        winbj = bet * 3.5
        lost = bet * 2

        while True:
            if player_total == 21:
                print("BLACKJACK! You hit 21!")
                self.player.wallet += winbj
                break
            elif player_total > 21:
                print("BUST! Your total is over 21. You lose.")
                self.player.wallet -= lost
                break

            try:
                stbet  = int(input("Do you want to (1-2): \n 1. Hit \n 2. Stand"))
                if stbet not in [1, 2]:
                    print("Invalid input please try again")
                    continue
                
                if stbet  == 2:
                    print("You chose to STAND")
                elif stbet ==1:
                    print("You chose to HIT")
                    new_card = random.randint(1, 11)
                    player_total += new_card
                    print(f"You drew a {new_card}. Your new total is {player_total}.")
                    time.sleep(2)

                    if player_total  > 21:
                        print("BUST! Your total is over 21. You lose.")
                        self.player.wallet -= lost
                        return
            except ValueError:
                print("Invalid input. Please enter 1 to Stand or 2 to Hit.")

            if player_total <=21:
                print("\nDealer's turn.")
                print(f"Dealer's hidden card was {dealer_second_card}, total: {dealer_total}")
                time.sleep(2)
            
            if dealer_total  < 17:
                new_card = random.randint(1,11)
                dealer_total += new_card
                print(f"Dealer draws a {new_card}. Dealer's total is now {dealer_total}.")
                time.sleep(2)

            # Determine the outcome
            print("\nFinal Results:")
            print(f"Your total: {player_total}")
            print(f"Dealer's total: {dealer_total}")

            time.sleep(1.5)

            if dealer_total > 21 or player_total > dealer_total:
                print("Congratulations! You won!")
                self.player.wallet += win
            elif dealer_total == player_total:
                print("It's a tie! No money won or lost.")
            else:
                print("Dealer wins. You lose.")
                self.player.wallet -= lost
            time.sleep(2)
            break


    def roulette(self):
        clearConsole()
        print("************************************************")
        print("[******** - WELCOME TO CASINO ROULETTE - ********]")
        print("************************************************")
        
        while True:
            # Request a valid bet from the player
            while True:
                try:
                    bet = int(input("How much money are you willing to bet today? "))
                    print(f"You currently have ${self.player.wallet}")

                    # Check if bet is within wallet balance
                    if bet > self.player.wallet:
                        print("Invalid bet amount. Please bet within your wallet balance.")
                    elif bet <= 0:
                        print("Bet amount must be greater than zero.")
                    else:
                        break  # Valid bet; exit the loop
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

           
            row = roulette_spin_row()

            print("Spinning...\n")
            print_row(row)  
            payout = get_payout(row, bet) 

            # Update wallet based on win/loss
            if payout > 0:
                print(f"You WON ${payout}!!!")
                self.player.wallet += payout
            else:
                print(f"You lost ${bet}!")
                self.player.wallet -= bet  # Deduct the bet amount from the wallet

            # Show current wallet balance
            print(f"Your current wallet balance is: ${self.player.wallet}")


            if self.player.wallet <= 0:
                print("You have run out of funds! Exiting Roulette.")
                time.sleep(1)
                break  # Exit if no funds remain

            # Ask if the player wants to play again
            while True:
                choice = input("Do you want to play again? (Y/N): ").upper()
                if choice not in ["Y", "N"]:
                    print("Invalid input, please try again.")
                elif choice == "N":
                    print("Exiting Roulette. Thanks for playing!")
                    time.sleep(1)
                    return  
                else:
                    break  
            

def roulette_spin_row():
    symbols = ["⋆", "༺Ƹ", "(ꐦ ◣‸◢)", "Ʒ༻", "✦ʚ♡ɞ✦"]
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("***************************")
    print(" | ".join(row))
    print("***************************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "⋆":
            return bet * 1.5
        elif row[0] == "༺Ƹ" or row[0] == "Ʒ༻":
            return bet * 3
        elif row[0] == "(ꐦ ◣‸◢)":
            return bet * 5
        elif row[0] == "✦ʚ♡ɞ✦":
            return bet * 7.5
    return 0

def main():
        while True:
            try:
                print("Are you above 18? \n 1. Yes \n 2. No")
                choice = int(input())
                if choice not in [1, 2]:
                    print("Invalid input please try again")
                    continue
                elif choice == 2:
                    print("You are still welcome to play in our casino just dont tell your parents \n Nor the police....")
                else:
                    print("Have Fun!!")
                break
            except ValueError:
                print("Invalid input please try again")

        while True:
            name = input("What is your name dear customer? ")

            if name.isdigit():
                print("Invalid input please try again (name cant be numbers)")
                continue
            elif len(name) > 10:
                print("Damn what a long ass name")
                break
            elif name.lower() == "mars":
                print("That's a great name, if I may say so!")
                break
            else:
                break
        return name

def clearConsole():
	command = 'clear'
	if os.name in ('nt','dos'):
		command = 'cls'
	os.system(command)

def main_menu(casino):
    while True:
        if player.wallet <= 0:
            time.sleep(2)
            print("""
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                """)
            print("Exiting Game...")
            time.sleep(5)
            exit()

        elif len(casino.casino_shop) == 0:
            time.sleep(2)
            print("You bought all the items in the casino")
            print("""
                ˚∧＿∧  　+        —̳͟͞͞💗
                (  •‿• )つ  —̳͟͞͞ 💗         —̳͟͞͞💗 +
                (つ　 <                —̳͟͞͞💗
                ｜　 _つ      +  —̳͟͞͞💗         —̳͟͞͞💗 ˚
                `し´
                """)
            print("Congratulations \n YOU HAVE COMPLETLY RUINED ME!!")
            print("Exiting Game...")
            time.sleep(5)
            exit()
        
        else:
            time.sleep(1.5)
            clearConsole()
            print("************************************************")
            print("[******** - WELCOME TO MARS GRAND CASINO - ********]")
            print("************************************************")
            print("\n")
            print(f"Current Balance: ${player.wallet: .2f}")
            print("\n")
            print("************************************************")
            print("What would you like to do?")
            print("1. Play Coin Toss Game")
            print("2. Play Horse Betting")
            print("3. Play Blackjack")
            print("4. Play Roulette")
            print("5. View and Purchase Items from Shop")
            print("6. Check Wallet Balance and Invetory")
            print("7. Exit")
            
            try:
                choice = int(input("Enter your choice (1-7): "))
                
                if choice == 1:
                    casino.coin_game()
                elif choice == 2:
                    casino.horse_betting()
                elif choice == 3:
                    casino.blackjack()
                elif choice == 4:
                    casino.roulette()
                elif choice == 5:
                    casino.purchase_item()
                elif choice == 6:
                    print(casino.player)  # This will print the player’s current wallet balance and purchased items
                    time.sleep(2.5)
                elif choice == 7:
                    print("Thank you for visiting the Mars Grand Casino! Come back soon!")
                    break  # Exit the loop and end the game
                else:
                    print("Invalid input. Please choose a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        

player_name = main()
player = Player(player_name)
casino = Casino(player)
main_menu(casino)
