from turtle import *
pld=Turtle()
wn=Screen()

pld.shape("square")
pld.penup()
pld.shapesize(1)

def switch():
    if pld.fillcolor()=="red":
        pld.fillcolor("black")
    else:
        pld.fillcolor("red")

for i in range(6):
    for i in range(2):
        for i in range(3):
            pld.forward(40)
            pld.stamp()
        pld.backward(100)
        switch()
    pld.right(90)
    pld.forward(20)
    pld.left(90)
    pld.backward(40)
    switch()

wn.mainloop()