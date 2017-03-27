import turtle
import math
import time

turtle.penup();
turtle.home();
turtle.mode("logo");
turtle.degrees();

cycle = 0;
length = 30;
distanceFromCenter = -1 * int(15 + (15 * math.sqrt(3)));
RIGHT = True;
LEFT = False;

turtle.speed(1000);
turtle.pen(5);

cycle = 0;

while True:

    cycle += 1;

    if(cycle % 6 == 0):
        turtle.color("red");
    elif(cycle % 6 == 1):
        turtle.color("orange");
    elif(cycle % 6 == 2):
        turtle.color("yellow");
    elif(cycle % 6 == 3):
        turtle.color("green");
    elif(cycle % 6 == 4):
        turtle.color("blue");
    elif(cycle % 6 == 5):
        turtle.color("violet");

    #Make a circle
    for i in range(5):
        turtle.circle(50);
        turtle.right(180);
        turtle.circle(25);
        turtle.right(180);
        turtle.right(1);
        turtle.forward(int(cycle / 45));
        turtle.width(int(cycle / 45) + 1);
    
    
    
