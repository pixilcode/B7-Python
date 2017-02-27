#Excercise 3: Hangman
word = (input('Word >>> ')).lower();
answer = ('_' * len(word));
guesses = set(['']);
chances = int(input('Chances >>> '));
incorrect = 0;

for num in range(50):
    print();

while incorrect < chances:
    print('Already Guessed: ' + str(guesses));
    guess = ((input('Letter >>> '))[0:1]).lower();
    guesses.add(guess);
    letterNum = 0;
    correct = False;
    for letter in word:
        if guess == letter:
            answer = answer[0:letterNum] + guess + answer[letterNum + 1:];
            correct = True;
        
        letterNum += 1;

    if correct:
        print('Good job!');

    else:
        print('Incorrect');
        incorrect += 1;
    
    print(answer);
    complete = True;
    for letter in answer:
        if letter == '_':
            complete = False;
            break;

    if complete:
        print('Congratulations! You won!');
        break;
    
    print();
else:
    print('I\'m sorry. You lost.');
