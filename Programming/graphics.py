#graphics.py
#working with turtle graphics

import turtle as t
import math

#see all turtle's methods!
print(dir(t))

#change the shape of your turtle
t.shape("turtle")

#move the turtle forward 100 units
#NOTE: turtle is by defualt at 0 degrees turn
#so now it will move positively along the x-axis
t.fd(100)

#change shape again
t.shape("triangle")

#move the turtle back 150 units
#agian, 0 degrees
t.bk(150)

#hide the turtle, it functions the same just not visible
t.hideturtle()

#turn the turtle 'left' 90 degrees
#this is positive increase in heading
t.left(90)

#move it right 100 units
t.fd(100)

#show the turtle again!
t.showturtle()

#you can also move a turtle without generating a line
#.penup() makes sure the turtle draws no line when it moves
t.penup()

#turn the turlte
t.left(-90)

#move it forward
t.fd(150)

#put the turtle back on the map
t.pendown()

#turn it and move
t.left(90)
t.fd(100)

#clear the image like this
#turtle remains where it left off
t.clear()

#if you want to clear the screen and put the turtle back at start
#you can do it manually (course, use penup/down for no line)
t.setposition(0,0)

#or use .reset(), which also put the turtle's heading back to 0
t.reset()

#change speed of turtle (0 is fastest)
t.speed(0)

#code for archimedes (equal seperation) spiral
t.color("blue")
t.down()
for i in range(200):
    n = i / 20 * math.pi
    x = (1 + 5 * n) * math.cos(n)
    y = (1 + 5 * n) * math.sin(n)
    t.goto(x, y)
t.up()
t.done()
