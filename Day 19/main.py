from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def fd():
    tim.fd(10)

def bd():
    tim.bk(10)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.reset()

screen.listen()
screen.onkey(key = "w", fun = fd)
screen.onkey(key = "s", fun = bd)
screen.onkey(key = "a", fun = left)
screen.onkey(key = "d", fun = right)
screen.onkey(key = "space", fun = clear)
screen.exitonclick()
