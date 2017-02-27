#Filename: decisionMakingBrendonBown.py
#Author: Brendon Bown
#Date: 9/28/2016
#Purpose: Make decisions with a FOR and a WHILE loop

#---------------------------------------------------------------------
#Activity 1: FOR loop with IF decision-making and user input
#Purpose: Make a decision with FOR and IF

#Get name from user
name1 = input('Name >>> ')
name = ['B', 'D', 'E', 'M', 'G', 'F', 'H', 'V']

#Loop to see if name starts with the letter name[i]
for i in range(0, len(name)):
    if name1[0] == name[i]:
        print('Nice to meet %s whose name starts with %s' % (name1, name[i]))
        break
else:
    print('I\'m sorry, %s, I don\'t know your name' % (name1))

#Cycle through names
cycle = int(input('Number of People >>> '))
for i in range(0, cycle):
    name1 = input('Name >>> ')
    if i == 0:
        print('Good to work with %s first thing today.' % (name1))
    elif i == 1:
        print('%s is the second person that I have worked with today.' % (name1))
    elif i == 2:
        print('I believe %s is the third individual whom I have worked with today.' % (name1))
    else:
        print('I was not planning on seeing %s today.' % (name1))

#---------------------------------------------------------------------
#Activity 1: WHILE loop with IF decision-making and user input
#Purpose: Make a decision with WHILE and IF

#Make variable 'stop'
stop = ''

#Loop to see if name starts with the letter name[i]
while stop != 'Y':
    #Get integer from user
    int1 = int(input('Integer >>> '))

    #Test for integer value
    if int1 < 10:
        print('Your number (%d) is less than 10.' % (int1))
    elif int1 < 20:
        print('Your number (%d) is between 11 and 20.' % (int1))
    elif int1 < 30:
        print('Your number (%d) is between 21 and 30.' % (int1))
    else:
        print('Your number (%d) is too high for this program.' % (int1))

    stop = input('Quit? (Y/N) >>> ')
