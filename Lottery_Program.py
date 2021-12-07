#                Program 1: Lottery
# The program will ask 3 numbers (0-9) from the user.
# It will then generate 3 random winning numbers (0-9).
# When the user's numbers matched the generated ones, it will display "Winner!"
# The program will ask at the end if the user wants to play/try again.

from random import randint

print("Welcome!\nLet's get to winning the lottery!")

def User_numb():
    numb_1 = int(input("Enter 1st number (0-9): "))
    numb_2 = int(input("Enter 2nd number (0-9): "))
    numb_3 = int(input("Enter 3rd number (0-9): "))

    while True:
        User_guess =(numb_1, numb_2, numb_3)
        winNumb_1 = randint (0, 9)
        winNumb_2 = randint (0, 9)
        winNumb_3 = randint (0, 9)
        Win_numb = (winNumb_1, winNumb_2, winNumb_3)
    
        if all(numb in Win_numb for numb in User_guess):
            print("Winner! You've won the lottery!")
        else:
            print("You lost. Better luck next time!")
    
        User_input = str(input("Try again? y/n\n: "))
    
        for char in User_input:
            if char in "yY":
                User_numb()
            elif char in "nN":
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid input.")
                exit()
                
User_numb()
