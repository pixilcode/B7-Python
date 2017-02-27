# Filename: functionsBrendonBown.py
# Author: Brendon Bown
# Date: 10/17/2016
# Purpose: To figure out function stuff

#----------------------------------------------------------------------------------
#Activity 1
#Create a 'printMin' function
def printMin(*nums):
    '''Print the minimum of the given numbers

Numbers must be integers'''
    minimum = nums[1]
    
    for num in nums:
        if minimum > num:
            minimum = num

    print(str(minimum) + ' is the minimum value')

#Print 'printMin' documentation
print(printMin.__doc__)
print('-----------------------------------------------------------------------')
printMin(2, 3, 1, -5, 7, 9)
