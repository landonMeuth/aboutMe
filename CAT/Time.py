import turtle as t

wn=t.Screen()
time=10
fontSetup=("Times New Roman",15,"normal")

timekeeper=t.Turtle()
timekeeper.penup()
timekeeper.goto(250,200)
timekeeper.pendown()
timekeeper.speed()

#function
def endGame():
    global time
    if time<=0:
        return True
    
def updatetime():
    global time
    time-=1
    timekeeper.clear()
    if time<=0:
        timekeeper.write("times up!",font=fontSetup)
    else:
        timekeeper.write(f"time: {time}",font=fontSetup)
        timekeeper.getscreen().ontimer(updatetime,interval)
    endGame()

#events
interval=1000
wn.ontimer(updatetime,interval)

#wn.mainloop()