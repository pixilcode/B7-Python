import turtle
import math
import time

def makeHexagon(isRight):
    if isRight == RIGHT:
        turtle.forward(length);
        turtle.right(60);
        turtle.forward(length);
        turtle.right(60);
        turtle.forward(length);
    elif isRight == LEFT:
        turtle.forward(length);
        turtle.left(60);
        turtle.forward(length);
        turtle.left(60);
        turtle.forward(length);

def makeHexOnHex(isRight):
    if isRight:
        makeHexagon(RIGHT);
        turtle.left(60);
        makeHexagon(LEFT);
        turtle.left(60);
        makeHexagon(RIGHT);
        turtle.right(60);
    else:
        makeHexagon(LEFT);
        turtle.right(60);
        makeHexagon(RIGHT);
        turtle.right(60);
        makeHexagon(LEFT);
        turtle.left(60);
        

turtle.penup();
turtle.home();
turtle.mode("logo");
turtle.degrees();

cycle = 0;
length = 30;
distanceFromCenter = -1 * int(15 + (15 * math.sqrt(3)));
RIGHT = True;
LEFT = False;

while True:

    #Increase the cycle number
    cycle += 1;

    #Send the turtle to the initial position
    turtle.penup();
    turtle.home();
    turtle.goto(distanceFromCenter, 0);
    turtle.degrees(360);
    turtle.pendown();

    #If the turtle is on an odd cycle, turn it to 90 degrees; if it is even, turn it to 30 degrees
    if cycle % 2 == 0:
        turtle.setheading(30);
        turn = 60;
        direction = RIGHT;
    elif cycle % 2 == 1:
        turtle.setheading(90);
        turn = -120;
        direction = LEFT;

    for i in range(int(math.pow(3, cycle - 2))):

        if math.pow(3, cycle - 2) == (1 / 3):
            makeHexagon(RIGHT);
            break;
        
        makeHexOnHex(direction);
        
    turtle.clear();    

    length *= math.sqrt(3) / 2;
    
