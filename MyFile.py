  # AddTen(n):  Adds 10 to the parameter n and returns the result
def addTen(n):
 n = n + 10
 return n
print(addTen(100))
  # DrawRectangle(Anyturtle, l, w):  Self Explanitory
import turtle
import time
po = turtle.Turtle()
def DrawRectangle(Anyturtle, l, w):
    for x in range(4):
        Anyturtle.forward(l)
        Anyturtle.right(90)
        Anyturtle.forward(w)
DrawRectangle(po, 5, 5)
  # DrawPoly(Anyturtle, n):  Will draw a regular polygon with 'n' sides of
     # * You should select the size of the polygon so that it always fits in the screen
#**15 points MAX***
