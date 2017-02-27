# Filename: calculationsBrendonBown.py
# Author: Brendon Bown
# Date: 9/13/2016
# Purpose: To practice calculating

#variables
a = 7
b = 12
c = 23
d = 34
e = 45

fiveStar = '*****'
fiveStarOffset = ' *****'
outerEdge = '*   *'
inOne = ' * * '
inTwo = '  *  '

pi = 3.14159265
radius = 1.2
area = pi * radius * radius
circumference = pi * radius * 2

#operations

    #print designs
print(fiveStar, fiveStarOffset, fiveStar, fiveStarOffset, fiveStar, sep = '\n')
print()
print(fiveStar, outerEdge, outerEdge, outerEdge, fiveStar, sep = '\n')
print()
print(fiveStar, outerEdge, inOne, inTwo, sep = '\n')

    #add 'a', 'b', 'c', 'd', and 'e'
summation = a + b + c + d + e
print('The sum is ' + str(summation))

    #multiply 'a', 'b', 'c', 'd', and 'e'
product = a * b * c * d * e
print('The product is ' + str(product))

    #show circle calculations
print('The radius is ' + str(radius))
print('The area is ' + str(area))
print('The circumference is ' + str(circumference))
