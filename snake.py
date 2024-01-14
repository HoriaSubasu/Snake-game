from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = segments

    def move_snake(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def pos(self):
        return self.segments[0].pos()

    def increase_tail(self):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        heading_tail = self.segments[len(self.segments) - 1].heading()
        position_tail = self.segments[len(self.segments) - 1].pos()
        segment.goto(position_tail)
        segment.setheading(heading_tail)
        self.segments.append(segment)


starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
