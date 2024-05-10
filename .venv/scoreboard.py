from turtle import Turtle

FONT = ("Arial", 18, "normal")

class ScoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = -1
		self.color("White")
		self.hideturtle()
		self.penup()
		self.goto(0, 270)
		self.increase_score()


	def increase_score(self):
		self.score += 1
		self.clear()
		self.write(arg=f"Your score: {self.score}", move=False, align="Center", font=FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align="Center", font=FONT)