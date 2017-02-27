from datetime import datetime
#USING ARRAYS
#Create an array
array = [ i * (int(datetime.today().second) % 7) for i in range(10)];

#Identify the number of elements in the array
print(str(len(array)));

#Use a loop and an if statement to find items in an array
otherArray = [];
for item in array:
    if item % 5 == 3:
        otherArray.append(item);

#Use indices to assign, retrieve, and replace values in array
array.extend([ i * (int(datetime.today().microsecond) % 147098) for i in range(7)]);
for i in range(3, 5):
    array[i] = 3;

print(str(array[2:7]));
print(str(array));
