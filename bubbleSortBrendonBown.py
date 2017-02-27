#Excercise 4: Bubble Sort
sortingList = [];

complete = False;

while not complete:
    addItem = input('Add item? (Y/N) >>> ');
    if addItem.upper() == 'Y':
        sortingList.append(input('Item >>> '));
    else:
        complete = True;
        break;

print();

complete = False;

while not complete:
    complete = True;
    for element in range(len(sortingList)):
        if element + 1 < len(sortingList) and sortingList[element] > sortingList[element + 1]:
            complete = False;
            swap = sortingList[element];
            sortingList[element] = sortingList[element + 1];
            sortingList[element + 1] = swap;

print(str(sortingList));
