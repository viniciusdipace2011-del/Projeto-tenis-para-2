from turtle import Turtle
class Padle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.create_padle(x_position, y_position)
    def create_padle(self, x_position, y_position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.extrasize = 5
        self.shapesize(stretch_wid=5+self.extrasize, stretch_len=1)
        self.size = 50 + self.extrasize*10
        self.goto(x_position, y_position)
    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x= x_cor, y= y_cor+20)
    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x=x_cor, y=y_cor - 20)
    def decrease_size(self,bet):
        self.extrasize -= self.extrasize/bet
        self.shapesize(stretch_wid=5+self.extrasize, stretch_len=1) 
        size = 50 + self.extrasize*10