from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print("  ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Write your code below!
for turn in range(10):
    print()
    print('Turn', str(turn + 1))
    
    guess_row = int(input("Row >>> "))
    guess_col = int(input("Column >>> "))

    if guess_row - 1 == ship_row and guess_col - 1 == ship_col:
        
        print("Battleship sunk!")
        break
        
    else:
        if guess_row not in range(1,6) or guess_col not in range(1,6):
            print('Sorry, the ocean isn\'t that big')
        elif board[guess_row - 1][guess_col - 1] == 'X':
            print ('Don\'t waste your ammo on somewhere that you have already sunk')
        else:
            print('Miss')
            board[guess_row - 1][guess_col - 1] = 'X'
            print_board(board)
    
    if turn == 9:
        print()
        print('Game Over')
