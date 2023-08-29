from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange", "pink", "brown"]
all_turtles= []

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
    tim.color(colors[turtle_index])
    tim.penup()
    # Y_INDEX = [-100, -60, -20, 20, 40]
    tim.goto(-230, y_index)
    y_index += 40
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle wins!")
            else:
                print(f"You lost! The {winner} turtle wins")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
  



screen.listen()

# Event listener than takes in 2 arguments: key and function
# screen.onkey(key= "w", fun=)




screen.exitonclick() 