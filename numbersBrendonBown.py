# Filename: numbersBrendonBown.py
# Author: Brendon Bown
# Date: 10/19/2016
# Purpose: To input two different numbers then have Python compare the numbers in a For Loop.

#----------------------------------------------------------------------------------
#Activity 1

for i in range(0,3):
    
    #Get val1 and put it in and test for an int
    val1 = float(input("Input a value >>> "))
    if val1 == int(val1):
        val1 = int(val1)
        print("Value 1: integer")
    elif val1 == float(val1):
        print("Value 1: float")

    #Get val2 and put it in and test for an int
    val2 = float(input("Input a value >>> "))
    if val2 == int(val2):
        val2 = int(val2)
        print("Value 2: integer")
    elif val2 == float(val2):
        print("Value 2: float")
    #Test the type to see if it is the same
    if type(val1) == type(val2):
        #If the value type is the same, print the value type and the sum of the two values
        print()
        print("Both types")
        print(type(val1))
        print()
        print("Sum: " + str(val1 + val2))
        print()
    else:
        #If the value type is different, print each value type and the product of the two values
        print()
        print("Value 1 type")
        print(type(val1))
        print()
        print("Value 2 type")
        print(type(val2))
        print()
        print("Product: " + str(val1 * val2))
        print()
        
