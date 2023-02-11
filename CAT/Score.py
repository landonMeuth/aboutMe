import turtle as t

wn=t.Screen()
score=0
fontSetup=("Times New Roman",15,"normal")

scorekeeper=t.Turtle()
scorekeeper.penup()
scorekeeper.goto(250,250)
scorekeeper.pendown()
scorekeeper.speed()

#function
def updateScore():
    global score
    score+=1
    scorekeeper.clear()
    scorekeeper.write(f"score: {score}",font=fontSetup)

#events
#wn.onscreenclick(updateScore)
#wn.mainloop()