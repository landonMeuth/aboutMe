#import
import turtle

#config vars
court=turtle.Turtle()
court.speed(0)

wn=turtle.Screen()
wn.setup(1000,600)

courtColor="blue" #[int(0x01),int(0xa1),int(0xd4)]
lineColor="white"
speed=10
angle=45

#defs
def line(x1,y1,x2,y2):
    court.penup()
    court.goto(x1,y1)
    court.pendown()
    court.goto(x2,y2)
    court.penup()

def drawCourt():
    wn.bgcolor(courtColor)
    court.color(lineColor)
    line(-500,220,500,220)
    line(-500,-220,500,-220)
    line(-250,-220,-250,220)
    line(250,-220,250,220)
    line(-250,0,250,0)
    court.width(3)
    line(0,-300,0,300)

#main operations
drawCourt()

wn.mainloop()