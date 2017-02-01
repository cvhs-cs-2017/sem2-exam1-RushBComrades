"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
import time
def Cube():
    qy = turtle.Turtle()
    def Square():
        for i in range(4):
            qy.forward(20)
            qy.right(90)
    Square()
    qy.up()
    qy.goto(25,25)
    qy.down()
    Square()
    qy.up()
    qy.goto(0,0)
    qy.down()
    qy.goto(25,25)
    qy.up()
    qy.goto(20,0)
    qy.down()
    qy.goto(45,25)
    qy.up()
    qy.goto(20,-20)
    qy.down()
    qy.goto(45,5)
    qy.up()
    qy.goto(0,-20)
    qy.down()
    qy.goto(25,5)
    qy.up()
    qy.goto(100,100)
    time.sleep(5)
Cube()


"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
