# Program 2: Guess the number
# The program will generate 1 random number (0-100)
# It will dispaly whether the guessed number of the user is greater than or less than the generated number.
# It will keep on asking the user until the random number has been guessed correctly.

from random import randint

randNum = randint (0,100)

def numberGuess():
    guess = int(input("Try to guess the number: "))

    while True:
        if (guess > 100 or guess < 0):
            print("Out of range!\n")
            numberGuess()
        
        if (guess > randNum):
            print("The number you guessed is 'GREATER THAN' the generated number.\n")
            numberGuess()
            
        if (guess < randNum):
            print("The number you guessed is 'LESS THAN' the generated number.\n")
            numberGuess()
            
        if (guess == randNum): 
            print(f"You got it! You guessed {randNum}.\n")
        
        User_input = str(input("Do you want to guess again? y/n\n: "))
        
        for char in User_input:
            if char in "yY":
                numberGuess()
            elif char in "nN":
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid input.")
                exit()
    
numberGuess()
    