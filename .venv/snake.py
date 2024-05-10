from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180

class Snake:

	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		for pos in START_POS:
			self.add_segment(pos)

	def move_snake(self):
		for seg in range(len(self.segments) - 1, 0, -1):
			xCor = self.segments[seg - 1].xcor()
			yCor = self.segments[seg - 1].ycor()
			self.segments[seg].goto(xCor, yCor)
		self.segments[0].forward(MOVE_DIST)

	def snake_up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def snake_down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def snake_right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def snake_left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def add_segment(self, pos):
		turtle = Turtle("square")
		turtle.color("white")
		turtle.penup()
		turtle.speed(1)
		turtle.goto(pos)
		self.segments.append(turtle)

	def extend(self):
		self.add_segment(self.segments[-1].position())