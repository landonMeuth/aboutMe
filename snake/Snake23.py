#added features
#pause button
#snake change color
#snake head faces direction
#snake sound when hit wall
#screen instructions in bottom left corner

# import

import turtle as t

from turtle import *

import time

import random as r

import winsound

winsound.PlaySound("mssound.wav", winsound.SND_ASYNC)
# game config and globals

delay = 0.1

bodyParts = []
bodyParts2 = []

pause=False

# object creation


wn = t.Screen()
wn.bgcolor("grey")
wn.setup(width=600,height=600)
wn.title("Snake!")

pauseButton=t.Turtle(shape="square")
pauseButton.speed(0)
pauseButton.penup()
pauseButton.goto(270,270)

directions=t.Turtle()
directions.hideturtle()
directions.penup()
directions.goto(-270,-270)
directions.write("Use wasd to controll player 1\n Use ijkl to controll player 2\n press the square/triange to pause/play.")

head = t.Turtle(shape="triangle")
head.speed(0)
head.penup()
head.direction = "stop"
head.goto(-40,0)

head2 = t.Turtle(shape="triangle")
head2.speed(0)
head2.penup()
head2.direction = "stop"
head2.goto(40,0)

food = t.Turtle()
food.shape("circle")
food.speed(0)
food.shapesize(.5,.5)
food.color("red")
food.penup()
food.goto(100,100)

# functions

def ups():
    # in mazerunner we used setheading
    
    if head.direction != "down":
        head.direction = "up"
        
def left():
    # in mazerunner we used setheading
    
    if head.direction != "right":
        head.direction = "left"

def right():
    # in mazerunner we used setheading
    
    if head.direction != "left":
        head.direction = "right"

def downs():
    # in mazerunner we used setheading
    
    if head.direction != "up":
        head.direction = "down"
    
def move():
    if not(pause):
        if head.direction == "up":
            head.sety(head.ycor()+20)
            head.setheading(90)
        if head.direction == "down":
            head.sety(head.ycor()-20)
            head.setheading(270)
        if head.direction == "right":
            head.setx(head.xcor()+20)
            head.setheading(0)
        if head.direction == "left":
            head.setx(head.xcor()-20)
            head.setheading(180)
def hideBodyParts():
    
    global bodyParts
    
    head.goto(-40,0)
    head.direction = "stop"
    for eachPart in bodyParts:
        eachPart.goto(1000,1000)
    bodyParts = []

# functions2

def ups2():
    # in mazerunner we used setheading
    
    if head2.direction != "down":
        head2.direction = "up"
        
def left2():
    # in mazerunner we used setheading
    
    if head2.direction != "right":
        head2.direction = "left"

def right2():
    # in mazerunner we used setheading
    
    if head2.direction != "left":
        head2.direction = "right"

def downs2():
    # in mazerunner we used setheading
    
    if head2.direction != "up":
        head2.direction = "down"
    
def move2():
    if not(pause):
        if head2.direction == "up":
            head2.sety(head2.ycor()+20)
            head2.setheading(90)
        if head2.direction == "down":
            head2.sety(head2.ycor()-20)
            head2.setheading(270)
        if head2.direction == "right":
            head2.setx(head2.xcor()+20)
            head2.setheading(0)
        if head2.direction == "left":
            head2.setx(head2.xcor()-20)
            head2.setheading(180)

def hideBodyParts2():
    
    global bodyParts2
    
    head2.goto(40,0)
    head2.direction = "stop"
    for eachPart in bodyParts2:
        eachPart.goto(1000,1000)
    bodyParts2 = []

def pausePlay(x,y):
    global pause
    if pause==False:
        pause=True
        pauseButton.shape("triangle")
    elif pause==True:
        pause=False
        pauseButton.shape("square")

# events

wn.onkeypress(ups,"w")
wn.onkeypress(left,"a")
wn.onkeypress(right,"d")
wn.onkeypress(downs,"s")

wn.onkeypress(ups2,"i")
wn.onkeypress(left2,"j")
wn.onkeypress(right2,"l")
wn.onkeypress(downs2,"k")

pauseButton.onclick(pausePlay)

wn.listen()

# mainloop

while True:
    
    wn.update()     # updates/refreshes the screen
    
    # border collision
    
    if head.xcor() == 300 or head.xcor() == -300 or head.ycor() == 300 or head.ycor() == -300:
        head.goto(0,0)
        head.direction = "stop"    
        hideBodyParts()
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    if head2.xcor() == 300 or head2.xcor() == -300 or head2.ycor() == 300 or head2.ycor() == -300:
        head2.goto(0,0)
        head2.direction = "stop"    
        hideBodyParts2()
        winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
        
    # Collide with the food
    if head.distance(food) < 20:    # returns the distance between the objects
        # food moves
        
        x = r.randint(-290,290)
        y = r.randint(-290,290)
        
        food.goto(x,y)
        
        # grow a body parts
        part = t.Turtle(shape="circle")
        part.shapesize(.5)
        part.speed(0)
        part.penup()
        bodyParts.append(part)

        #change snake color
        newcolor=r.choice(["red","green","blue","yellow","purple"])
        head.color(newcolor)
        for i in bodyParts:
            i.color(newcolor)

    if head2.distance(food) < 20:    # returns the distance between the objects
        # food moves
        
        x = r.randint(-290,290)
        y = r.randint(-290,290)
        
        food.goto(x,y)
        
        # grow a body parts
        part = t.Turtle(shape="circle")
        part.shapesize(.5)
        part.speed(0)
        part.penup()
        bodyParts2.append(part)

        #change snake color
        newcolor=r.choice(["red","green","blue","yellow","purple"])
        head2.color(newcolor)
        for i in bodyParts2:
            i.color(newcolor)
        
    
    # move the body parts
    for i in range(len(bodyParts)-1,0,-1):
        x = bodyParts[i-1].xcor()
        y = bodyParts[i-1].ycor() 
        bodyParts[i].goto(x,y)
    move()

    for i in range(len(bodyParts2)-1,0,-1):
        x = bodyParts2[i-1].xcor()
        y = bodyParts2[i-1].ycor() 
        bodyParts2[i].goto(x,y)
    move2()
    
    # move the neck to the head
    
    if len(bodyParts)>0:
        x = head.xcor()
        y = head.ycor()
        bodyParts[0].goto(x,y)
    
    if len(bodyParts2)>0:
        x = head2.xcor()
        y = head2.ycor()
        bodyParts2[0].goto(x,y)
    
    # did we hit ourselves? or did we eat our body parts
    for i in range(len(bodyParts)-1,0,-1):
        if len(bodyParts)-1>=i or not(pause):
            if bodyParts[i].pos() == head.pos():
                hideBodyParts()
                winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    
    for i in range(len(bodyParts2)-1,0,-1):
        if len(bodyParts2)-1>=i or not(pause):
            if bodyParts2[i].pos() == head.pos():
                hideBodyParts()
                winsound.PlaySound("hit.wav", winsound.SND_ASYNC)

    for i in range(len(bodyParts)-1,0,-1):
        if len(bodyParts)-1>=i or not(pause):
            if bodyParts[i].pos() == head2.pos():
                hideBodyParts2()
                winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    
    for i in range(len(bodyParts2)-1,0,-1):
        if len(bodyParts2)-1>=i or not(pause):
            if bodyParts2[i].pos() == head2.pos():
                hideBodyParts2()
                winsound.PlaySound("hit.wav", winsound.SND_ASYNC)
    
    
    
    
    time.sleep(delay)

# end of all movement

wn.mainloop()