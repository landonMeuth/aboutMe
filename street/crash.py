#everything from turtle
from turtle import *# create two empty lists of turtles, adding to them later
horizontalTurts = []
verticalTurts = []# use interesting shapes and colors
turtleShapes = ["arrow", "turtle", "circle",]# "square", "triangle", "classic"]
horizColors = ["red", "blue", "green"]#, "orange", "purple", "gold"]
vertColors = ["darkred", "darkblue", "lime"]#, "salmon", "indigo", "brown"]
spacing=50
for shape in turtleShapes:
    ht = Turtle(shape=shape)
    horizontalTurts.append(ht)
    ht.penup()
    ht.fillcolor(horizColors.pop())
    ht.goto(-250,spacing)
    ht.setheading(0)    
    vt = Turtle(shape=shape)
    verticalTurts.append(vt)
    vt.penup()
    vt.fillcolor(vertColors.pop())
    vt.goto(-spacing,250)
    vt.setheading(270)
    spacing+=25#moving the turtles
distanceToMove=2
for step in range(100):
    for h in horizontalTurts:
        for v in verticalTurts:
            h.fd(distanceToMove)
            v.fd(distanceToMove)        #check for collision
        if (abs(h.xcor() - v.xcor()) < 20):
            if (abs(h.ycor()-v.ycor())<20):
                h.fillcolor("gray")
                v.fillcolor("gray")
                horizontalTurts.remove(h)       #remove from the list stop stop them moving, cant move something not in the list
                verticalTurts.remove(v) 
#wn = Screen()
#wn.mainloop()