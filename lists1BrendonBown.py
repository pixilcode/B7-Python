#1D List Excercises

#Excercise 1: Shopping List
shoppingList = [];

complete = False;

while not complete:
    addItem = input('Add item? (Y/N) >>> ');
    if addItem.upper() == 'Y':
        shoppingList.append(input('Item >>> '));
    else:
        complete = True;
        break;

print();
print('Shopping List');
print('-' * 13);
for item in shoppingList:
    print(item);

print('*' * 30);

#Excercise 2: TV Stations
tvStations = [[], [], [], [], [], [], []];
days = (('Su', 'Sunday'), ('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'));

complete = False;

while not complete:
    addItem = input('Add show? (Y/N) >>> ');
    if(addItem.upper() == 'Y'):
        show = input('Show >>> ');
        showDay = input('Day of the Week (Su, Mo, Tu, We, Th, Fr, Sa) >>> ');
        for day in range(len(days)):
            if showDay == days[day][0]:
                tvStations[day].append(show);
                break;
        else:
            print('The given day is invalid');
    else:
        complete = True;
        break;

for day in range(len(days)):
    print(days[day][1], end = '');
    for show in tvStations[day]:
        print(show.rjust(5), end = '');
    print();

print('*' * 30);

#Excercise 3: Hangman
word = input('Word >>> ');
answer = ('_' * len(word));
guesses = set([]);
chances = int(input('Chances >>> '));

for num in range(50):
    print();

for chance in range(chances):
    print('Already Guessed: ' + str(guesses));
    guess = (input('Letter >>> '))[0:1];
    guesses.add(guess);
    letterNum = 0;
    for letter in word:
        if guess == letter:
            answer = answer[0:letterNum] + guess + answer[letterNum + 1:];
        
        letterNum += 1;
    
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
