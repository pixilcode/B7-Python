def numSort(array):
    even = list();
    odd = list();

    for i in array:
        if i % 2 == 0:
            even.append(i);
        else:
            odd.append(i);

    odd.sort();
    even.sort();

    array = list();
    array.extend(even);
    array.extend(odd);

    return array;

array = [5, 3, 8, 6, 0, 12, 4, 23]
print("Original array: " + str(array));
array = numSort(array);
print("Sorted array: " + str(array));
