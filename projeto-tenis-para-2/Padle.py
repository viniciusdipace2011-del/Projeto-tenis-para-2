from turtle import Turtle
class Padle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.create_padle(x_position, y_position)
    def create_padle(self, x_position, y_position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_position, y_position)
    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x= x_cor, y= y_cor+20)
    def down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        self.goto(x=x_cor, y=y_cor - 20)