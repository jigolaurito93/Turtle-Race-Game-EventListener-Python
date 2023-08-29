from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange", "pink", "brown"]

screen = Screen()
# Set up the dimensions of the screen
screen.setup(500,400)

# Create a user prompt
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

print(user_bet)

y_index = -100

for turtle_index in range(0,6):
    tim = Turtle()
    tim.shape('turtle')
    tim.color(random.choice(colors))
    tim.penup()
    tim.goto(-230, y_index)
    y_index += 40


screen.listen()

# Event listener than takes in 2 arguments: key and function
# screen.onkey(key= "w", fun=)




screen.exitonclick() 