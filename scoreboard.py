from turtle import Turtle

FONT = ('Times New Roman', 12, 'normal')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pen()
        self.goto(x=0, y=280)
        self.pendown()
        self.color("white")
        self.write(arg="Score: 0", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.pendown()
        self.write(arg='Game Over.', move=False, align=ALIGNMENT, font=FONT)
