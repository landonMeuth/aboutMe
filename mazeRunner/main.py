#import
import turtle as t
import random as r
import time as tm
#global var and game config
wn=t.Screen()
wallLength=15
numberOfWalls=25
pathWidth=15
time=30
play=0
#init objects
wn.setup(800,800)

pause = t.Turtle()
pause.speed(0)
pause.penup()
pause.hideturtle()
pause.goto(-60,380)
pause.write("Click screen to begin!", font=("Times",12,"bold"))

mazeDrawer = t.Turtle()
mazeDrawer.pensize(5)
mazeDrawer.pencolor("blue")
mazeDrawer.speed(0)

mazeRunner = t.Turtle()
mazeRunner.color("blue")
mazeRunner.penup()
mazeRunner.speed(0)
mazeRunner.goto(-40,40)

timekeeper = t.Turtle()
timekeeper.pensize(5)
timekeeper.pencolor("blue")
timekeeper.speed(0)
timekeeper.goto(230,270)

enemy = t.Turtle()
enemy.pensize(5)
enemy.pencolor("red")
enemy.fillcolor("red")
enemy.speed(0)
enemy.penup()

#functions

p=25

def drawDoor(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.penup()
    mazeDrawer.fd(p*2)
    mazeDrawer.pendown()

def drawBarrier(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.left(90)
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.bk(pathWidth*2)
    mazeDrawer.right(90)
#events
#main loops
def drawMaze():
    
    global wallLength
    global numberOfWalls
    global pathWidth
    
    mazeDrawer.goto(0,0)
    
    for i in range(numberOfWalls):
        wallLength+=pathWidth
        if(i>4):
            mazeDrawer.left(90)

            doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
            barrierSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))

            while abs(doorSpot-barrierSpot) < pathWidth:
                doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))

            if(doorSpot<barrierSpot):
                drawDoor(doorSpot)
                drawBarrier(barrierSpot-doorSpot-pathWidth*2)
                mazeDrawer.fd(wallLength-barrierSpot)
            else:
                drawBarrier(barrierSpot)
                drawDoor(doorSpot-barrierSpot)
                mazeDrawer.fd(wallLength-doorSpot-pathWidth*2)
    
    mazeDrawer.penup()
    mazeDrawer.goto(-300,-200)
    mazeDrawer.pendown()
    mazeDrawer.goto(-300,300)
    mazeDrawer.goto(190,300)
    mazeDrawer.goto(190,-200)
    mazeDrawer.goto(-250,-200)
    
    mazeDrawer.hideturtle()

def message(text):
    wn.clear()
    mazeDrawer.goto(-60,0)
    mazeDrawer.write(text, font=("Times",32,"bold"))
def turnLeft():
    global play
    if play:
        mazeRunner.left(90)
def turnRight():
    global play
    if play:
        mazeRunner.right(90)
def goForward():
    global play
    if play:
        mazeRunner.fd(5)
        canvas = wn.getcanvas()
        x,y=mazeRunner.pos()
        items = canvas.find_overlapping(x+5, -y+5, x-5, -y-5)

        if(len(items)>1):
            mazeRunner.goto(-40,40)
            items=[]
            pass
        if mazeRunner.pos()[0]>400 or mazeRunner.pos()[0]<-400 or mazeRunner.pos()[1]>400 or mazeRunner.pos()[1]<-400:
            wn.clear()
            message("You Win!")
            play=0
        
def updatetime():
    global time
    time-=play
    timekeeper.clear()
    if play==1:
        enemy.setheading(enemy.towards(mazeRunner.pos()[0],mazeRunner.pos()[1]))
        enemy.forward(15)
    if (abs(mazeRunner.pos()[0]-enemy.pos()[0]))<=5 or (abs(mazeRunner.pos()[0]-enemy.pos()[0]))<=5:
        time = 0
    if time<=0:
        timekeeper.write("times up!",font="Times")
        message("Game Over")
    else:
        timekeeper.write(f"time: {time}",font="Times")
        timekeeper.getscreen().ontimer(updatetime,interval)
        
def pause(x,y):
    global play
    if play==1:
        play=0
    else:
        play=1
    
#events
wn.onkeypress(turnLeft,"a")
wn.onkeypress(goForward,"w")
wn.onkeypress(turnRight,"d")
interval=1000
wn.ontimer(updatetime,interval)
wn.onscreenclick(pause)
wn.listen()

drawMaze()


wn.mainloop()


# Make sure the outer wall of the maze is a solid wall so that there is only 1 escape route