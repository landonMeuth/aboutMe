import turtle

class car:
    def __init__(self,color,lane,shape):
        self.color=color
        self.lane=lane
        self.shape=shape
        turtle.shape()
        turtle.color(self.color)
        
    def drive(self):
        turtle.forward(10)