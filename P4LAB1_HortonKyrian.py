import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create the turtle
builder = turtle.Turtle()
builder.color("green")
builder.pensize(2)
builder.speed(5)

# Draw square using a for loop
for _ in range(4):
    builder.forward(100)
    builder.left(90)

# Move to top of square for the roof
builder.fillcolor("green")
builder.begin_fill()

# Position for triangle
builder.goto(0, 100)

# Draw triangle using a while loop
sides = 0
while sides < 3:
    builder.forward(100)
    builder.left(120)
    sides += 1

builder.end_fill()

# Hide turtle
builder.hideturtle()

# Keep window open
turtle.done()
