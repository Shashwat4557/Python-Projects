import turtle

# Create a turtle object
my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

# Set the turtle's speed to fast
my_turtle.speed(1)

# Set the turtle's pen color to red
my_turtle.pencolor("red")

# Move the turtle to the starting position
my_turtle.penup()
my_turtle.goto(-150, 0)
my_turtle.pendown()

# Write the word "Happy"
my_turtle.write("HAPPY", font=("Arial", 36, "bold"))

# Move the turtle to the next position
my_turtle.penup()
my_turtle.forward(200)

# Write the word "Birthday"
my_turtle.write("BIRTHDAY", font=("Arial", 36, "bold"))

# Move the turtle to the next position
my_turtle.penup()
my_turtle.forward(300)

# Write the word "Birthday"
my_turtle.write("TANYA", font=("Arial", 36, "bold"))

# Hide the turtle when done
my_turtle.hideturtle()

# Keep the turtle window open
turtle.done()