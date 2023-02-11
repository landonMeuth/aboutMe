import turtle
import random

wn=turtle.Screen()

def fourLaneInt():
    road=turtle.Turtle()
    wn=turtle.Screen()
    turtle.bgcolor("grey")
    road.color("yellow")
    road.speed(0)
    for i in range (4):
        road.forward(400)
        road.goto(0,0)
        road.right(90)
    road.color("white")

    road.penup()

    road.goto(-400,40)
    for i in range(20):
        road.pendown()
        road.forward(20)
        road.penup()
        road.forward(20)
    road.goto(-400,-40)
    for i in range(20):
        road.pendown()
        road.forward(20)
        road.penup()
        road.forward(20)
    road.right(90)
    road.goto(40,400)
    for i in range(20):
        road.pendown()
        road.forward(20)
        road.penup()
        road.forward(20)
    road.goto(-40,400)
    for i in range(20):
        road.pendown()
        road.forward(20)
        road.penup()
        road.forward(20)

    road.color("grey")
    road.begin_fill()
    road.goto(-80,-80)
    road.pendown()
    road.goto(80,-80)
    road.goto(80,80)
    road.goto(-80,80)
    road.goto(-80,-80)
    road.end_fill()

    road.color("green")

    road.begin_fill()
    road.goto(-400,-400)
    road.pendown()
    road.goto(-400,-80)
    road.goto(-80,-80)
    road.goto(-80,-400)
    road.goto(-400,-400)
    road.end_fill()

    road.begin_fill()
    road.penup()
    road.goto(400,400)
    road.pendown()
    road.goto(400,80)
    road.goto(80,80)
    road.goto(80,400)
    road.goto(400,400)
    road.end_fill()

    road.begin_fill()
    road.penup()
    road.goto(-400,400)
    road.pendown()
    road.goto(-400,80)
    road.goto(-80,80)
    road.goto(-80,400)
    road.goto(-400,400)
    road.end_fill()

    road.begin_fill()
    road.penup()
    road.goto(400,-400)
    road.pendown()
    road.goto(400,-80)
    road.goto(80,-80)
    road.goto(80,-400)
    road.goto(400,-400)
    road.end_fill()

    turtle.penup()
fourLaneInt()

car1=turtle.Turtle()
car1.penup()
car1.speed(0)
car2=turtle.Turtle()
car2.penup()
car2.speed(0)
car3=turtle.Turtle()
car3.penup()
car3.speed(0)

car1.goto(random.randrange(-600,-400),60)
car2.goto(60,random.randrange(-600,-400))
car2.left(90)
car3.goto(random.randrange(400,600),-60)
car3.left(180)
car1true=True
car2true=True
car3true=True
car1.shapesize(2)
car2.shapesize(2)
car3.shapesize(2)
while 1:
    if car1true:
        car1.fd(6)
    if car2true:
        car2.fd(5)
    if car3true:
        car3.fd(7)
    if car1.pos()[0]>400:
        car1.goto(random.randrange(-600,-400),60)
    if car2.pos()[1]>400:
        car2.goto(60,random.randrange(-600,-400))
    if car3.pos()[0]<-400:
        car3.goto(random.randrange(400,600),-60)
    if (car1true)and(car2true)and(abs(car1.pos()[0]-car2.pos()[0])<20)and(abs(car1.pos()[1]-car2.pos()[1])<20):
        car1.color("red")
        car1.stamp()
        car1.hideturtle()
        car2.color("red")
        car2.stamp()
        car2.hideturtle()
        car1true=False
        car2true=False
    if (car1true)and(car3true)and(abs(car1.pos()[0]-car3.pos()[0])<20)and(abs(car1.pos()[1]-car3.pos()[1])<20):
        car1.color("red")
        car1.stamp()
        car1.hideturtle()
        car3.color("red")
        car3.stamp()
        car3.hideturtle()
        car1true=False
        car3true=False
    if (car3true)and(car2true)and(abs(car3.pos()[0]-car2.pos()[0])<20)and(abs(car3.pos()[1]-car2.pos()[1])<20):
        car2.color("red")
        car2.stamp()
        car2.hideturtle()
        car3.color("red")
        car3.stamp()
        car3.hideturtle()
        car2true=False
        car3true=False
'''
Rev4:  When two cars collide, have the turtles stamp their location with a red color
Rev5:  When cars collide, have the turtles "disappear"
'''
#wn.mainloop()