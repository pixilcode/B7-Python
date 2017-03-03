# Tic-Tac-Toe

import random

def drawBoard(board):
    #This function prints out the board that it was passed

    #"board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9]);
    print('-+-+-');
    print(board[4] + '|' + board[5] + '|' + board[6]);
    print('-+-+-');
    print(board[1] + '|' + board[2] + '|' + board[3]);

def inputPlayerLetter():
    #Lets the player type which letter they want to be.
    #Returns a list with the player's letter as the first item and the computer's letter as teh second.
    letter = '';
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?');
        letter = input().upper();

    #The first element in the list is the player's letter; the second is the computer's letter.
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
        return 'player';
    else:
        return 'player';

def makeMove(board, letter, move):
    board[move] = letter;

def isWinner(bo, le):
    #Given a board and a player's letter, this function returns True if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #Across top
            (bo[4] == le and bo[5] == le and bo[6] == le) or #Across middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or #Across bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or #Down left
            (bo[8] == le and bo[5] == le and bo[2] == le) or #Down middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or #Down right
            (bo[7] == le and bo[5] == le and bo[3] == le) or #Diagonal UL to BR
            (bo[9] == le and bo[5] == le and bo[1] == le))   #Diagonal BL to UR

def getBoardCopy(board):
    #Make a copy of the board list and return it.
    boardCopy = [];
    for i in board:
        boardCopy.append(i);
    return boardCopy;

def isSpaceFree(board, move):
    #Return True if the passed move is free on the passed board.
    return board[move] = ' ';

def getPlayerMove(board):
    #Let the player enter their move.
    move = ' ';
    print('Alright, human, make your move.');
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)');
        move = input();

    return move;

def chooseMove(board, compLet, playLet):

    #Check if the player can win on the next move
    cBoard = getBoardCopy(board);
    
    #Computer and player chance of winning
    compWin = [];
    playWin = [];
    
    for i in range(len(cBoard)):
        #Ignore index 0
        if i = 0:
            continue;

        #See if the computer can win
        cBoard[i] = compLet;

        if (isWinner(cBoard, compLet) and randint
