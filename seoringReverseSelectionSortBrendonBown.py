def sort(array):
    for i in range(0, len(array) - 1):
        minIndex = i;
        for j in range(i + 1, len(array)):
            if array[j] > array[minIndex]:
                minIndex = j;
        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i];
    return array;

print("Sorting 64 25 12 22 11...");
print(sort([64, 25, 12, 22, 11]));
print();
print("Sorting 4 7 11 4 9 5 11 7 3 5...");
print(sort([4, 7, 11, 4, 9, 5, 11, 7, 3, 5]));
print();
print("Sorting -7 6 7 5 9 0 11 10 5 8...");
print(sort([-7, 6, 7, 5, 9, 0, 11, 10, 5, 8]));
