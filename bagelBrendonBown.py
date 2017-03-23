import random

#Variables , can technically be deleted
weights = []    #Correct answers
total = 0
guesses = 0
enterL = 0
enterH = 0
enter = 0
correctDisplay = []
enterIn = []
playing = True
win = False


#Makes correct answers
def generateAnswers(howMany, low, high):
    temp = []
    tot = 0
    generated = 0
    for i in range(howMany):
        generated = random.randint(low, high)
        temp.append(str(generated))
        tot += generated
    return temp, tot

#Lots of prints
def intro():
    print("-----------------------------------------------")
    print("Welcome to the bagel game!")
    print()
    print("Multiple numbers will be generated")
    print("You will be given the total of them")
    print("And will have to figure it out yourself!")
    print()
   

#Sets important variables
def initialize():
    guesses = eval(input("How many guesses would you like? >>> "))
    enterL = eval(input("Lowest number? >>> "))
    enterH = eval(input("Highest number? >>> "))
    enter = eval(input("And how many numbers would you like there to be? >>> "))
    weights, tot = generateAnswers(enter, enterL, enterH)
    return guesses, weights, tot, enter

#Checks if guess is in correct and updates accordingly        
def checkCorrect(guess, correct):
    IsIn = False
    for i in correct:
        if str(guess) == str(i):
            IsIn = True
            correctDisplay.append(i)
            weights.remove(i);
    return IsIn

#Takes an int and a list
def printBoard(boardIn):
    #Create an empty board
    board = [" _ "] * enter;
    #Put the correct guesses in the board
    for i in range(len(boardIn)):
        board[i] = " " + str(boardIn[i]) + " ";
    #Print out the board
    strBoard = "";
    for num in board:
        strBoard += num;
    print(strBoard);


#Displays guesses, total, and correct guesses so far
def display():
    print()
    print("You have %d guesses left"%(guesses))
    print("The total of the numbers is %d"%(tot))
    print("Here's what you have so far >>> ", end='')
    printBoard(correctDisplay)
    print()

#Asking for a number
def ask():
    display()
    temp = input("Enter a number to check >>> ")
    return temp

#Asking if they want to play again
def playAgain():
    temp = input("Would you like to play again? (Yes/No) >>> ")
    if temp.lower() == "yes" or temp.lower == "y":
        return True
    else:
        return False

while playing:
    intro()
    weights = []    #Just clearing for a new game
    total = 0
    guesses = 0
    enterL = 0
    enterH = 0
    enter = 0
    correctDisplay = []
    enterIn = []
    guesses, weights, tot, enter = initialize()
    while guesses > 0:
        a = ask()
        b = checkCorrect(a, weights)

        if b:
            print("This number is in the list!")
        else:
            print("Sorry, this number isn't in the list")
        if len(weights) == 0:
            win = True
            guesses = 0
        else:
            guesses -= 1
        print("-------------------------------------")
    if win:
        printBoard(correctDisplay)
        print("YOU WIN!")
    else:
        print()
        print("You lose! The numbers are ", end='')
        printBoard(weights)
        print()
    playing = playAgain()
