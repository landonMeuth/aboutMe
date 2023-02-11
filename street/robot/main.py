#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(0)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(0)
robot.showturtle()

def reset(maze):
  robot.clear()
  wn.bgpic(maze)
  robot.goto(startx, starty)
  robot.setheading(90)

#---- TODO: change maze here
#MAZE !#
reset("maze1.png")

for step in range(4): # forward 3
  move()
  for i in range(3):
    turn_left()
  move()
  turn_left()

#MAZE 2# 
reset("maze2.png")

for i in range(3):
  move()
for i in range(3):
  turn_left()
for i in range(2):
  move()
  
#maze 3#
reset("maze3.png")

for step in range(4): # forward 3
  move()
  for i in range(3):
    turn_left()
  move()
  turn_left()
  
#maze 4#
def go(a,b):
  for i in range(a):
    turn_left()
  for i in range(b):
    move()


reset ("maze4.png")

movements=((3,2),(1,4),(1,1),(2,1),(3,2),(1,2),(3,2))

for i in range(len(movements)):
  go(movements[i][0],movements[i][1])

#---- end robot movement 

reset("maze2.png")
print("W=FORWARD A=LEFT D=RIGHT")
def forwards():
  robot.forward(50)
  print(robot.pos())
  robot.goto(round(robot.pos()[0], 2),round(robot.pos()[1], 2))
  if robot.pos() in {(-100.00,100.00),(-50.00,100.00),(0.00,100.00),(100.00,100.00),(-50.00,0.00),(0.00,0.00),(0.00,-50.00),(-50.00,-50.00),(100.00,-50.00),(100.00,-100.00)}:
    reset(f"maze2.png")
  if robot.pos()==(0,50) or robot.pos()==(-0,50):
    print("YOU WIN!")
    exit()
  if abs(robot.pos()[0])==150 or abs(robot.pos()[1])==150:
    reset(f"maze2.png")
def left():
  robot.left(90)
def right():
  robot.right(90)


wn.onkey(forwards,"w")
wn.onkey(left,"a")
wn.onkey(right,"d")
wn.listen()

wn.mainloop()


