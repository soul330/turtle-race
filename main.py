from turtle import Turtle, Screen
import random

race_is_on = False
window_screen = Screen()
window_screen.setup(width=500, height=400)
user_pick_turtle = window_screen.textinput(title="Pick your turtle", prompt="Pick the color of the turtle: ")
turtle_colors = ["red", "blue", "yellow", "green", "purple", "pink"]
my_guy_position = [-70, -40, -10, 20, 50, 80]
list_of_turtles = []


for my_guy in range(0, 6):
    new_racer = Turtle(shape="turtle")
    new_racer.penup()
    new_racer.color(turtle_colors[my_guy])
    new_racer.goto(x=-230, y=my_guy_position[my_guy])
    list_of_turtles.append(new_racer)

if user_pick_turtle:
    race_is_on = True

while race_is_on:

    for turtle in list_of_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

window_screen.exitonclick()

