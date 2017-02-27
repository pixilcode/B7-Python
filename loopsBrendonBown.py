num = 23
run = True
while run:
    guess = int(input('Enter an integer:'))
    if guess == num:
        print('Correct')
        #Stop the loop
        run = False
    elif guess > num:
        print('Too high')
    else:
        print('Too low')

else:
    print('The loop is over')
