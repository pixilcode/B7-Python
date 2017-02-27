# Filename : P03_Looping.py
# Author : Brendon Bown
# Date : 9/19/2016
# Purpose : This project practices for loops

#Print numbers 1-10
for i in range(1,11):
    print(i)
else:
    print('-' * 20)

#Print multiples of 3 up to 30
for i in range(1,11):
    print(i * 3)
else:
    print('-' * 20)

#Print a pyramid of '|ERROR|' using a While loop
i = 1
while i < 11:
    print('|ERROR|' * i)
    i += 1
else:
    print('-' * 20)
