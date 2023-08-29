from turtle import Turtle, Screen

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()

screen = Screen()
# Set up the dimensions of the screen
screen.setup(500,400)

# Create a user prompt
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

print(user_bet)

t1.color('brown')
t2.color('blue')
t3.color('green')
t4.color('black')

t1.shape("turtle")
t1.penup()
t1.goto(-235, 0)

screen.listen()

# Event listener than takes in 2 arguments: key and function
# screen.onkey(key= "w", fun=)




screen.exitonclick() 