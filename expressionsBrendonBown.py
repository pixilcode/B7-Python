#file:expressions author:Brendon Bown

#Ask for the length and width
length = int(input('What is the length? >>> '))
print()
width = int(input('What is the width? >>> '))

#Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

#Print area and perimeter
print()
print('The area is ' + str(area))
print()
print('The perimeter is ' + str(perimeter))

#Notify that the program is done
print()
print('End of program')
