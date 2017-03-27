import turtle
import math
import time
from threading import Thread

class turtleThread:

    def __init__(self, isTurned):
        self.isTurned = isTurned;
        self.stopped = False;
        self.T = turtle();

    def start(self):
        Thread(target = self.run, args=()).start();

    def run(self):
        self.T.penup();
        self.T.home();
        self.T.mode("logo");
        self.T.degrees();

        if self.isTurned:
                T.right(180);

        self.T.speed(1000000);
        self.T.pen(5);

        cycle = 0;

        while True:

            cycle += 1;

            if(cycle % 6 == 0):
                self.T.color("red");
            elif(cycle % 6 == 1):
                self.T.color("orange");
            elif(cycle % 6 == 2):
                self.T.color("yellow");
            elif(cycle % 6 == 3):
                self.T.color("green");
            elif(cycle % 6 == 4):
                self.T.color("blue");
            elif(cycle % 6 == 5):
                self.T.color("violet");

            #Make a circle
            for i in range(5):
                self.T.circle(50);
                self.T.circle(25);
                self.T.right(1);
                self.T.forward(int(cycle / 45));
                self.T.width(int(cycle / 45) + 1);
            
            
turtleThread(True).start();
turtleThread(False).start();
