import time
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.OKGREEN + "                                                 Welcome To BlackJack" + bcolors.ENDC)

def start():
    FirstNumber = random.randint(1,11)
    RandomNumber = random.randint(1,10)
    print("")
    betAmount = int(input(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "How Much Would You Like To Bet?: "))
    print("")
    print(bcolors.FAIL + "Game: " + bcolors.ENDC + "You Are Betting " + bcolors.OKGREEN + f"${betAmount}" + bcolors.ENDC)
    print("")
    print(bcolors.HEADER + "Dealer: "+ bcolors.ENDC + "Starting Game!")
    print("")
    time.sleep(.5)
    print(bcolors.OKBLUE + "You: " + bcolors.ENDC + f"{FirstNumber}")
    tempNum1 = FirstNumber
    print("")
    FirstNumber = random.randint(1,11)
    time.sleep(.5)
    print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + f"{FirstNumber}")
    tempNum2 = FirstNumber
    print("")
    time.sleep(.5)
    finalNum1 = tempNum1 + RandomNumber
    print(bcolors.OKBLUE + "You: " + bcolors.ENDC + bcolors.WARNING + f"{finalNum1}" + bcolors.ENDC)
    print("")
    time.sleep(.5)
    RandomNumber = random.randint(1, 10)
    finalNum2 = tempNum2 + RandomNumber
    print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + bcolors.WARNING + f"{finalNum2}" + bcolors.ENDC)
    print("")
    FinalInput = input(bcolors.FAIL + "Game: "+ bcolors.ENDC + bcolors.WARNING + "Hit Stand Or Double Down (H, S, D) " + bcolors.ENDC)
    if FinalInput == "H":
        RandomNumber = random.randint(1,10)
        finalNum1 = finalNum1 + RandomNumber
        if finalNum1 >= 21.01:
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Have Gone Bust!" + bcolors.ENDC)
            print("")
            print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Got {finalNum1}!")
            start()
        print("")
        print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Are At " + bcolors.WARNING + f"{finalNum1}" + bcolors.ENDC)
        print("")
        FinalInput = input(bcolors.FAIL + "Game: "+ bcolors.ENDC + bcolors.WARNING + "Hit Stand Or Double Down (H, S, D) " + bcolors.ENDC)
        if FinalInput == 'H':
            RandomNumber = random.randint(1, 10)
            finalNum1 = finalNum1 + RandomNumber
            if finalNum1 >= 21.01:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Have Gone Bust!" + bcolors.ENDC)
                print("")
                print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Got {finalNum1}!")
                start()
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Are At " + bcolors.WARNING + f"{finalNum1}" + bcolors.ENDC)
            print("")
            FinalInput = input(bcolors.FAIL + "Game: " + bcolors.ENDC + bcolors.WARNING + "Hit Stand Or Double Down (H, S, D) " + bcolors.ENDC)
            RandomNumber = random.randint(1,10)
            finalNum1 = finalNum1 + RandomNumber
            if finalNum1 >= 21.01:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Have Gone Bust!" + bcolors.ENDC)
                print("")
                print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Got {finalNum1}!")
                start()
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Are At " + bcolors.WARNING + f"{finalNum1}" + bcolors.ENDC)
            print("")
            FinalInput = input(bcolors.FAIL + "Game: " + bcolors.ENDC + bcolors.WARNING + "Hit Stand Or Double Down (H, S, D) " + bcolors.ENDC)
            RandomNumber = random.randint(1, 10)
            finalNum1 = finalNum1 + RandomNumber
            if finalNum1 >= 21.01:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolor.ENDC + "You Have Gone Bust!" + bcolors.ENDC)
                print("")
                print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Got {finalNum1}!")
                start()
            print("")
            print(bcolors.HEADER + "Dealer: " +bcolors.ENDC + "You Are At " + bcolors.WARNING + f"{finalNum1}" + bcolors.ENDC)
            print("")
            FinalInput = input(bcolors.FAIL + "Game: " + bcolors.ENDC + bcolors.WARNING + "Hit Stand Or Double Down (H, S, D) " + bcolors.ENDC)
            RandomNumber = random.randint(1, 10)
            finalNum1 = finalNum1 + RandomNumber
            if finalNum1 >= 21.01:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Have Gone Bust!")
                print("")
                print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Got {finalNum1}!")
                start()
            FinalInput = input(bcolors.FAIL + "Game: " + bcolors.ENDC + bcolors.WARNING + "You Must Stand! (S) ")
    if FinalInput == "S":
        RandomNumber = random.randint(1,10)
        finalNum2 = finalNum2 + RandomNumber
        print("")
        print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "Dealer Is At " + bcolors.WARNING + f"{finalNum2}" + bcolors.ENDC)
        if finalNum2 >= 21.01:
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "Dealer Went Over 21 You Win!" + bcolors.ENDC)
            print(bcolors.FAIL + "Game:" + bcolors.ENDC + f" You Won ${betAmount * 2}")
        if finalNum2 >= 17:
            if finalNum1 == finalNum2:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "Push You Both Got The Same Number!")
            if finalNum1 >= finalNum2:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Win!")
                print("")
                print(bcolors.FAIL + "Game:" + bcolors.ENDC + f" You Won ${betAmount * 2}")
            if finalNum2 >= finalNum1:
                print("")
                print(bcolors.HEADER + "Dealer:" + bcolors.ENDC + " Dealer Wins!")
        if finalNum2 <= 17:
            if finalNum2 >= 21.01:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "Dealer Went Over 21 You Win!" + bcolors.ENDC)
                print("")
                print(bcolors.FAIL + "Game:" + bcolors.ENDC + f" You Won ${betAmount * 2}")
            if finalNum1 == finalNum2:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "Push You Both Got The Same Number!")
            if finalNum1 >= finalNum2:
                print("")
                print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Win!")
                print("")
                print(bcolors.FAIL + "Game:" + bcolors.ENDC + f" You Won ${betAmount * 2}")
            if finalNum2 >= finalNum1:
                print("")
                print(bcolors.HEADER + "Dealer:" + bcolors.ENDC + " Dealer Wins!")
            if finalNum2 >= finalNum1:
                print("")
                print(bcolors.HEADER + "Dealer:" + bcolors.ENDC + bcolors.FAIL + " You Went bust Dealer Wins!" + bcolors.ENDC)
            if finalNum1 <= finalNum2:
                print("")
                print(bcolors.HEADER + "Dealer:" + bcolors.ENDC + bcolors.OKGREEN + " Dealer Went Bust You Win!" + bcolors.ENDC)
                print("")
                print(bcolors.FAIL + "Game:" + bcolors.ENDC + f" You Won ${betAmount * 2}")
                start()
            if finalNum2 >= 17.01:
                if finalNum1 == finalNum2:
                    print("")
                    print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "Push You Both Got The Same Number!")
                if finalNum2 >= finalNum1:
                    print("")
                    print(bcolors.HEADER + "Dealer:" + bcolors.ENDC + bcolors.FAIL + " You Went bust Dealer Wins!" + bcolors.ENDC)
                if finalNum1 <= finalNum2:
                    print("")
                    print(bcolors.HEADER + "Dealer:" + bcolors.ENDC + bcolors.OKGREEN + " Dealer Went Bust You Win!" + bcolors.ENDC)
                    print("")
                    print(bcolors.FAIL + "Game:" + bcolors.ENDC + f" You Won ${betAmount * 2}")
                    start()
    if FinalInput == "D":
        RandomNumber = random.randint(1, 10)
        RandomNumber2 = random.randint(1, 10)
        finalNum1 = finalNum1 + RandomNumber
        finalNum2 = finalNum2 + RandomNumber2

        print("")
        print(bcolors.FAIL + "Game: " +bcolors.ENDC + "Dealer Got " + f"{bcolors.WARNING}{finalNum2}" + bcolors.ENDC)
        if finalNum1 >= 21.01:
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Have Gone Bust!" + bcolors.ENDC)
            print("")
            print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Got {finalNum1}!")
            print("")
            print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Lost ${betAmount} While Doubling Down!")
            start()
        if finalNum2 >= finalNum1:
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + "You Have Gone Bust Dealer Wins!")
            print("")
            print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Got {finalNum1}!")
            print("")
            print(bcolors.FAIL + "Game: " + bcolors.ENDC + f"You Lost ${betAmount} While Doubling Down!")
        if finalNum1 >= finalNum2:
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + f"You Won With {bcolors.WARNING}{finalNum1}!" + bcolors.ENDC)
            print("")
            print(bcolors.HEADER + "Dealer: " + bcolors.ENDC + bcolors.WARNING + bcolors.ENDC + f"You Won{bcolors.OKGREEN} ${betAmount * 2}" + bcolors.ENDC + " While Doubling Down!")
            start()
    start()
start()