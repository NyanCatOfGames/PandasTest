# Number guessing game
from colorama import Fore, Style
from random import randint


def easy_game():
    actual_number = randint(1, 10)
    turns = 3

    for i in range(turns):
        print()
        print(Fore.YELLOW + f"You have {turns - i} turn(s) left.")
        guess = -1
        while guess not in range(1, 11):
            guess = int(input(Fore.CYAN + Style.BRIGHT + "Guess a number between 1 and 10! You will receive a hint of whether it is higher, or lower.\n Enter number here: "))
        
        if guess == actual_number:
            print(Fore.GREEN + Style.BRIGHT + "That is the correct number - Congratulations!")
            break

        if i < turns - 1:
            if guess > actual_number:
                print(Fore.YELLOW + "You guessed a number which was too big!")
            elif guess < actual_number:
                print(Fore.YELLOW + "You guessed a number which was too small!")
        else:
            print(Fore.RED + Style.BRIGHT + f"You lose - Unlucky! The correct number was {actual_number}")


def medium_game():
    actual_number = randint(1, 100)
    turns = 6

    for i in range(turns):
        print()
        print(Fore.YELLOW + f"You have {turns - i} turn(s) left.")
        guess = -1
        while guess not in range(1, 101):
            guess = int(input(Fore.CYAN + Style.BRIGHT + "Guess a number between 1 and 100! You will receive a hint of whether it is higher, or lower.\n    Enter number here: "))
        
        if guess == actual_number:
            print(Fore.GREEN + Style.BRIGHT + "That is the correct number - Congratulations!")
            break

        if i < turns - 1:
            if guess > actual_number:
                print(Fore.YELLOW + "You guessed a number which was too big!")
            elif guess < actual_number:
                print(Fore.YELLOW + "You guessed a number which was too small!")
        else:
            print(Fore.RED + Style.BRIGHT + f"You lose - Unlucky! The correct number was {actual_number}")


def hard_game():
    actual_number = randint(1, 1000)
    turns = 9

    for i in range(turns):
        print()
        print(Fore.YELLOW + f"You have {turns - i} turn(s) left.")
        guess = -1
        while guess not in range(1, 1001):
            guess = int(input(Fore.CYAN + Style.BRIGHT + "Guess a number between 1 and 1000! You will receive a hint of whether it is higher, or lower.\n   Enter number here: "))
        
        if guess == actual_number:
            print(Fore.GREEN + Style.BRIGHT + "That is the correct number - Congratulations!")
            break

        if i < turns - 1:
            if guess > actual_number:
                print(Fore.YELLOW + "You guessed a number which was too big!")
            elif guess < actual_number:
                print(Fore.YELLOW + "You guessed a number which was too small!")
        else:
            print(Fore.RED + Style.BRIGHT + f"You lose - Unlucky! The correct number was {actual_number}.")


print(Style.BRIGHT + "Hello and welcome to this number guessing game! I hope you have lots of fun. Feel free to explore the different difficulties!")
print()


while True:
    gametype = input(Fore.CYAN + "Do you want to play on easy, medium, or hard difficulty? If you do not want to play, enter 'Exit'.\n   Enter your choice here: ")
    
    if gametype in ["Easy", "Medium", "Hard", "Exit"]:
        if gametype == "Easy":
            easy_game()
        elif gametype == "Medium":
            medium_game()
        elif gametype == "Hard":
            hard_game()
        elif gametype == "Exit":
            print(Fore.RESET + Style.DIM + "Play again soon!")
            quit()
        else:
            print(Fore.RESET + Style.DIM + "Error in gametype")



