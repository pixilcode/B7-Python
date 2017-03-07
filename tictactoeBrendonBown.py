# Tic-Tac-Toe

import random
import time

def drawBoard(board):
    #This function prints out the board that it was passed

    #"board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9]);
    print('-+-+-');
    print(board[4] + '|' + board[5] + '|' + board[6]);
    print('-+-+-');
    print(board[1] + '|' + board[2] + '|' + board[3]);

def inputPlayerLetter():
    #Lets the player type which letter they want to be
    #Returns a list with the player's letter as the first item and the computer's letter as teh second
    letter = '';
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?');
        letter = input().upper();

    #The first element in the list is the player's letter; the second is the computer's letter
    if letter == 'X':
        return ['X', 'O'];
    else:
        return ['O', 'X'];

def whoGoesFirst():
    #Ask if they want to go first
    print('Should I provide you with the first move so that you can have a chance at beating me? (y/n)');
    answer = input().upper();

    #If their answer is yes, let them go first
    if answer == 'Y':
        print('Alright, I can give you the advantage because I will still win.');
        return 'player';
    else:
        print('Your confidence will be your downfall.');
        return 'computer';

def makeMove(board, letter, move):
    board[move] = letter;

def isWinner(bo, le):
    #Given a board and a player's letter, this function returns True if that player has won
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #Across top
            (bo[4] == le and bo[5] == le and bo[6] == le) or #Across middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or #Across bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or #Down left
            (bo[8] == le and bo[5] == le and bo[2] == le) or #Down middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or #Down right
            (bo[7] == le and bo[5] == le and bo[3] == le) or #Diagonal UL to BR
            (bo[9] == le and bo[5] == le and bo[1] == le))   #Diagonal BL to UR

def getBoardCopy(board):
    #Make a copy of the board list and return it
    boardCopy = [];
    for i in board:
        boardCopy.append(i);
    return boardCopy;

def isSpaceFree(board, move):
    #Return True if the passed move is free on the passed board
    return board[move] == ' ';

def getPlayerMove(board, playerName):
    #Let the player enter their move
    move = ' ';
    print('Alright, '+ playerName + ', make your move.');
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)');
        move = input();

    print('Interesting choice.');
    return move;

def getBestMove(board):
    #The heirarchy of moves and an array to hold the options
    bestMove = [[5], [7, 9, 1, 3], [8, 4, 2, 6]];
    moveOptions = [];

    #No moves have been found yet
    foundMoves = False;

    #For each move in each move set, check to see if there are viable options and add them to the option list
    for moveSet in bestMove:
        for move in moveSet:
            if isSpaceFree(board, move):
                foundMoves = True;
                moveOptions.append(move);

        if foundMoves:
            break;

    #If moves were found, return a random choice from the available moves, otherwise return nothing
    if foundMoves:
       return random.choice(moveOptions);
    else:
        return None;


def chooseMove(board, compLet, playLet):

    #Check if the player can win on the next move
    cBoard = getBoardCopy(board);
    openSpaces = [];

    #Cycle through each square
    for i in range(len(cBoard)):
        #Ignore index 0
        if i == 0:
            continue;

        if isSpaceFree(cBoard, i):
            #See if the computer can win
            cBoard[i] = compLet;

            #If it can and if it doesn't mess up, win
            if (isWinner(cBoard, compLet) and randint(1, 4) > 1):
                return i;

            #Switch the sign
            cBoard[i] = playLet;

            #If the player can win next turn and the computer can see that, play there
            if (isWinner(cBoard, playLet) and randint(1, 6) > 1):
                return i;

    return getBestMove(board);

def printStringSlowly(phrase, opening = '', end = '', separationTime = 1):
    print(opening, end = '');
    time.sleep(separationTime);
    for letter in phrase:
        print(letter, end = '');
        if not(letter == ' '):
            time.sleep(separationTime);

    print(end);

#Game Loop
#Introduction
print('So, a human has decided to challenge me.');
time.sleep(2);
playerName = input('What is your name, human? ');
time.sleep(1);
print('Well, ' + playerName + ', are you ready to lose?');
time.sleep(2);
print('Because if you aren\'t, you should probably just give up now.');
time.sleep(2);
printStringSlowly(['un', 'beat', 'a', 'ble'], opening = 'For I am ', end = '.');
print('Shall we begin?');

#Loop
while True:
    #Reset the board
    gameBoard = [' '] * 10;

    #Get letters
    playerLetter, computerLetter = inputPlayerLetter();

    #Get who goes first
    turn = whoGoesFirst();

    #Start the game
    gameIsPlaying = True;
    while gameIsPlaying:
        if turn == 'player':
            #Player's turn
            drawBoard(gameBoard);
            move = getPlayerMove(gameBoard);
            makeMove(gameBoard, playerLetter, move);

            #Check to see if the player is the winner
            if isWinner(gameBoard, playerLetter):
                drawBoard(gameBoard);
                print('I am impressed with your skill.');
