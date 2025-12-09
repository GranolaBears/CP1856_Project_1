import sys

def write_money(player_money):
    try:
        with open("money.txt", "w") as file:
            file.write(str(player_money))
    except Exception as e:
        print(type(e), e)
        sys.exit()

def read_money():
    try:
        with open("money.txt", "r") as file:
            money = file.read()
            return float(money)
    except FileNotFoundError:
        default_money = 100.0
        try:
            with open("money.txt", "w") as file:
                file.write(str(default_money))
            return default_money
        except Exception as e:
            print(type(e), e)
            sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()
    
