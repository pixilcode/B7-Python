#Excercise 1: Shopping List
shoppingList = [];

complete = False;

while not complete:
    addItem = input('Item >>> ');
    if not addItem == '':
        shoppingList.append(addItem);
    else:
        break;

print();
print('Shopping List');
print('-' * 13);
for item in shoppingList:
    print(item);

#Bubble Sort
while not complete:
    complete = True;
    for element in range(len(shoppingList)):
        if element + 1 < len(shoppingList) and shoppingList[element] > shoppingList[element + 1]:
            complete = False;
            swap = shoppingList[element];
            shoppingList[element] = shoppingList[element + 1];
            shoppingList[element + 1] = swap;

print(str(shoppingList));

print('*' * 30);
