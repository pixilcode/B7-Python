# Filename: stringsBrendonBown.py
# Author: Brendon Bown
# Date: 10/17/2016
# Purpose: To mess with strings

#----------------------------------------------------------------------------------
#Activity 1
#Take quote
quote = input("Input famous quote >>> ")

#Find length of the quote and use it to divide the quote into three parts
quotePiece1 = quote[0:int(1/3 * len(quote))]
quotePiece2 = quote[int(1/3 * len(quote)):int(2/3 * len(quote))]
quotePiece3 = quote[int(2/3 * len(quote)): len(quote)]

#Put all pieces into one array
quoteCollection = [quotePiece1, quotePiece2, quotePiece3]

#Print the quote
print("Quote: " + quote)

#Iterate through quoteCollection to print quotePieces to be more efficient
for q in quoteCollection:
    print(q)

print()


for i in range(0, len(quoteCollection)):
    print(quoteCollection[i])

print()


#Do the actual assignment which is less efficient
for i in range(0, 3):
    if i == 0:
        print(quotePiece1)
    elif i == 1:
        print(quotePiece2)
    elif i == 2:
        print(quotePiece3)

#----------------------------------------------------------------------------------
#Activity 2
#Take quote
quote = input("Input famous quote >>> ")

#Create iteration variable
i = 0

#WHILE loop doing jobs
while i < 3:
    qsplit = quote.split()
    if i == 0:
        print(qsplit)
    elif i == 1:
        print(''.join(qsplit))
    elif i == 2:
        print(' ERROR '.join(qsplit))
    i += 1
