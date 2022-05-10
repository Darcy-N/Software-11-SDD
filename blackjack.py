import random
import os

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11 ]

def clear():
    os.system('cls||clear')

clear()

def drawCard():
    cardIndex = random.randrange(0, len(cards))
    cards.pop(cardIndex)
    card = cards[cardIndex]
    return card

PlayerCards = [drawCard(), drawCard()]
DealerCards = [drawCard(), drawCard()]

def asci(asciival): # I can't be bothered to make this side by side way too much effort
    print(" _____")
    print("|     |")
    if asciival == "?":
        print("|  " + asciival + "  |")
    else:
        if asciival >= 10:
            asciival = str(asciival)
            print("|  " + asciival + " |")
        else:
            asciival = str(asciival)
            print("|  " + asciival + "  |") 
    print("|     |")
    print(" ▔▔▔▔▔ ")

def DisplayCardPlayer():
    print("Player cards:")
    for j in PlayerCards:
        asci(j)

def DisplayCardDealer(isHidden):
    print("Dealer cards")
    if isHidden == "hidden":
        asci("?")
        asci(DealerCards[1])
    else:
        for j in DealerCards:
            asci(j)

def countPlayer():
    total = 0
    for i in PlayerCards:
        total += i
    return total

def countDealer():
    total = 0
    for i in DealerCards:
        total += i
    return total

def W():
    if countPlayer() == 21:
        print("Congratulations, you W!")
        print("")
        exit()
    else:
        pass

def acePlayer():
    if countPlayer() > 21:
        for i in PlayerCards: 
            if i == 11:
                i = 1
            else:
                pass

def aceDealer():
    if countDealer() > 21:
        for i in DealerCards: 
            if i == 11:
                i = 1
            else:
                pass
clear()
DisplayCardPlayer()
DisplayCardDealer("hidden")
print(f"You are at {countPlayer()}, the dealer is at ?")

def main():
    W()
    while countPlayer() != 21:
        W()
        if countPlayer() > 21:
            acePlayer()
        
            if countPlayer() > 21:
                clear()
                DisplayCardPlayer()
                DisplayCardDealer("no")
                print("You went over 21, you lose :(")
                print("")
                exit()
        else:
            pass
        choice = input("Hit or stand? (Hit/h or Stand/s) ")
        print("")
        choice = choice.lower()
        if choice == 'h':
            PlayerCards.append(drawCard()) 
            W()
            clear()
            DisplayCardPlayer()
            DisplayCardDealer("no")
            print(f"You are at {countPlayer()}, the dealer is at ?")
        elif choice == 's':
            while countDealer() <= 16:
                DealerCards.append(drawCard()) 
                aceDealer()
                if countDealer() > 21:
                    DisplayCardPlayer()
                    DisplayCardDealer("no")
                    print("The dealer bust, you Win!")
                    print("")
                    exit()
                elif countDealer() == 21:
                    DisplayCardPlayer()
                    DisplayCardDealer("no")
                    print("The dealer got to 21, you loose.")
                    print("")
                    exit()
                elif countDealer() >=16 and countDealer() <= 20:
                    break
            print("")
            if countPlayer() == countDealer():
                DisplayCardPlayer()
                DisplayCardDealer("no")
                print(f"You stood at {countPlayer()}, the dealer reached {countDealer()}, you tied!")
                exit()
            elif countPlayer() > countDealer():
                DisplayCardPlayer()
                DisplayCardDealer("no")
                print(f"You stood at {countPlayer()}, the dealer reached {countDealer()}, you Win!")
                exit()
            elif countDealer() > countPlayer():
                DisplayCardPlayer()
                DisplayCardDealer("no")
                print(f"You stood at {countPlayer()}, the dealer reached {countDealer()}, you lose :(")
                exit()

main()