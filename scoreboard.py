from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "left"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("black")
        self.teleport(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()