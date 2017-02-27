def sort(array):
    complete = False;
    
    while not complete:
        complete = True;
        for element in range(len(array)):
            if element + 1 < len(array) and array[element] > array[element + 1]:
                complete = False;
                swap = array[element];
                array[element] = array[element + 1];
                array[element + 1] = swap;

def newList():
    complete = False;
    array = [];
    
    while not complete:
        addItem = input('Item >>> ');
        if not addItem == '':
            array.append(addItem);
        else:
            return array;

def addTo(array, item):
    array.append(item);

def display(array):
    print();
    print('Shopping List');
    print('-' * 13);
    for item in shoppingList:
        print(item);
    
    print(str(shoppingList));

def delete(array):
    array = [];

#Excercise 1: Shopping List
print('Welcome to ShoppingList');
shoppingList = [];

while True:
    print('\nWhat would you like to do?\n1.\tDisplay the list\n2.\tAdd to the list\n3.\tSort the list\n4.\tDelete the list\n5.\tCreate a new list

print('*' * 30);
