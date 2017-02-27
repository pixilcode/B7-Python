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
