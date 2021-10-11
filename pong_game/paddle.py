from turtle import Turtle
PADDLE_SIZE = 4
PADDLE_XCOR = 390

class Paddle:


    def __init__(self, side) -> None:
        self.paddle = []
        self.side = side
        self.create_paddle()



    def create_paddle(self) -> None:

        if self.side == "left":
            multiplier = -1
        else:
            multiplier = 1
        
        for i in range(PADDLE_SIZE):
            segment = Turtle()
            segment.color("white")
            segment.penup()
            segment.shape("square")           
            segment.goto(x = PADDLE_XCOR * multiplier, y = 60 - 20 * i)
            self.paddle.append(segment)


    def move_paddle_up(self) -> None:
        for segment in self.paddle:
            segment.sety(segment.ycor() + 20)


    def move_paddle_down(self) -> None:
        for segment in self.paddle:
            segment.sety(segment.ycor() - 20)

    
    def paddle_position_top(self) -> int:
        return self.paddle[0].ycor()


    def paddle_position_bottom(self) -> int:
        return self.paddle[len(self.paddle)-1].ycor()