from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        screen2 = Screen()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.user_bet = screen2.textinput(title = "Qual a meta", prompt="Informe a meta de pontos para vencer: ")
    def write_score(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    def write_meta(self):
        self.goto(x=-0, y=-300)    
        self.write(f"Meta: {self.user_bet}", align="center", font=("Courier", 30, "normal"))
    def increase_l(self):
        self.l_score += 1
    def increase_r(self):
        self.r_score += 1