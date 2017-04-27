def sort(array):
    for i in range(1, len(array)):
        if array[i] < array[0]:
            temp = array[0];
            array[0] = array[i];
            array[i] = temp;
    returnArray = [array[0]];
    if len(array) > 1:
        returnArray.extend(sort(array[1:]));
        return returnArray;
    else:
        return returnArray;

print("Sorting 64 25 12 22 11...");
print(sort([64, 25, 12, 22, 11]));
print();
print("Sorting 4 7 11 4 9 5 11 7 3 5...");
print(sort([4, 7, 11, 4, 9, 5, 11, 7, 3, 5]));
print();
print("Sorting -7 6 7 5 9 0 11 10 5 8...");
print(sort([-7, 6, 7, 5, 9, 0, 11, 10, 5, 8]));
