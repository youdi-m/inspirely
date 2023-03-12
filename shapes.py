import turtle

# create a turtle object
t = turtle.Turtle()

# set turtle speed
t.speed(0)

# draw a circle
t.penup()
t.goto(0, -100)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()

# draw a triangle
t.penup()
t.goto(-350, 150)
t.pendown()
t.color("green")
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()

# draw a square
t.penup()
t.goto(150, -50)
t.pendown()
t.color("blue")
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# exit on click
turtle.exitonclick()