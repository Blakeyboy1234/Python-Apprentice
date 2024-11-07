"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.

RUM ME! YOu can run this program by clicking on ▶️ icon ar the top of the editor
window.

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the wind
tina = turtle.Turtle()                  # Create a turtle named tina

tina.speed(10)
tina.shape('triangle')                    # Set the shape of the turtle to a turtle
tina.speed(1)                           # Make the turtle move as fast, but not too fast.

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(150)                       # Move tina forward by the forward distance
tina.right(80)                           # Turn tina left by the left turn

tina.pencolor('blue')                    # Set the pen color to red
tina.forward(100)                       # Continuie the last two steps three more times
tina.right(90)                           # to draw a square

tina.pencolor('purple')                  # Set the pen color to green
tina.forward(100)
tina.left(90)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(100)
tina.left(90)

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Why, hello there!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

tina.goto(-50,0)
tina.pendown()
tina.color('green') 
for i in range(4):
    for y in range(5):
        tina.circle(100, steps=5)
        tina.forward(10)
    tina.right(90)
    tina.forward(3)


turtle.exitonclick()                    # Close the window when we click on it

# Now you can try writing your own programs. Open
# the next file 03_Turtle_Tricks.py

