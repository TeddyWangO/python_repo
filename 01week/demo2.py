import turtle
import math
x, y, x1, y1, x2, y2, x3, y3 = 100, 100, 100, -100, -100, -100, -100, 100
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.goto(x1, y1)
turtle.goto(x2, y2)
turtle.goto(x3, y3)

distance = math.sqrt((x-x3)*(y-y1))
turtle.write(distance)
turtle.done()
