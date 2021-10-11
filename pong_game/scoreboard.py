from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, position:str) -> None:
        super().__init__()
        self.score = 0
        self.position = position
        self.penup()
        self.hideturtle()
        self.color("white")
        
        self.current_score()


    def win(self):
        self.score += 1
        self.clear()
        self.current_score()


    def current_score(self):
        if self.position == "right":
            self.goto(x = 50, y = 220)
        elif self.position == "left":
            self.goto(x = -50, y = 220)
        
        self.write(self.score, align = self.position, font = ("Arial", 40, "normal") )