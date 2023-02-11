#---import statements----
import turtle as t
import random as r
import leaderboard as lb
import math

#---game configurations--- (global variables)
wn=t.Screen()
score=0
timer=5
interval=1000
size=3
fontSetup=("Times New Roman",12,"normal")
FILENAME='Database.txt'       #constant variable, don't change it
begin=False
accuracyMeter=0
turtleMeter=0

#---intialize turtles--- (initialize objects)
bob = t.Turtle()

def setBob():
     bob.shape("turtle")
     bob.shapesize(size)
     bob.color("black")
     bob.fillcolor("purple")
     bob.speed(0)
     bob.penup()
setBob()

scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.hideturtle()
scorekeeper.goto(300,300)
scorekeeper.pendown()
scorekeeper.speed(0)

timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.goto(300,260)
timekeeper.pendown()
timekeeper.speed(0)

#---functions---
#the command to run when there is an event
#when you use onClick event, you MUST give the function the x,y
def bobClicked():
     print("bob was clicked")
     print()     #mouse's x and y
     moveBob()

def moveBob():
     #randomly moving bob
     newX=r.randint(-300,250)
     newY=r.randint(-300,250)
     bob.goto(newX,newY)

def updateScore():
     #global is to let this function know to go look at a global var
     global score
     score+=1
     scorekeeper.clear()
     #object.write("message",options)         ("font type      ",size,"style")
     scorekeeper.write(f"Score: {score}",font=fontSetup)
 
          
def do(x,y):
     global turtleMeter
     global begin
     global size
     
     turtleMeter+=1
     begin = True
     
     bob.color("red")
     bob.fillcolor("white")
     bob.stamp()
     if size==1:
          size=3
     else:
          size-=1
     setBob()
     bobClicked()
     updateScore()
     wn.bgcolor("red")
     for i in range(1000000):
          pass
     wn.bgcolor("white")

#game over function
def manageLeaderboard():
     #get the data from the txt file
     namesList=lb.getNames(FILENAME)
     scoresList=lb.getScores(FILENAME)
     
     #check to see if you made the leaderboard
     if(len(scoresList)<5 or score>=int(scoresList[-1])):
          name=input("Congrats, you're on the board \n\tName Please:")
          lb.updateLeaderboard(FILENAME, namesList, scoresList, name, score)
     else:
          lb.remove(FILENAME,namesList,scoresList)
     
     #update the leaderboard
     
     #display the leaderboard
     lb.draw_leaderboard(False, namesList, scoresList, scorekeeper, 10)
     
     
def updatetimer():
     #global is to let this function know to go look at a global var
     global timer
     timekeeper.clear()
     if timer<=0:
          timekeeper.write(f"Times Up! \n{math.trunc((turtleMeter/accuracyMeter)*100)}% accuracy",font=fontSetup)
          bob.hideturtle()
          manageLeaderboard()
     else:
          if begin == True:
               timer-=1
          timekeeper.write(f"Timer: {timer}",font=fontSetup)
          #we need to recusively run this function
          #timerkeeper gets the screen's ontimer and resets the command and interval
          timekeeper.getscreen().ontimer(updatetimer,interval)
          
def count(x,y):
     global accuracyMeter
     accuracyMeter+=1
     
     

#---events---
#object.onclick(command) -> we can reset this anytime we want
wn.onclick(count)
bob.onclick(do)
wn.ontimer(updatetimer,interval)

#---main loop --- (running code)
wn.mainloop()