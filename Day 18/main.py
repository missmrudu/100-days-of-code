import turtle as t
from random import choice, randint

t.colormode(255)
tim = t.Turtle()
tim.speed(1)
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_color = (r,g,b)
    return random_color


#CHALLENGE 1
for i in range(4):
    tim.forward(100)
    tim.left(90)

tim.reset()

#CHALLENGE 2
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

tim.reset()


#CHALLENGE 3
tim.speed("fast")
angle = 360
number_of_sides = [3,4,5,6,7,8,9,10]
for side in number_of_sides:
    angle_of_shape = angle/side
    tim.color(random_color())
    for i in range (side):
        tim.forward(100)
        tim.right(angle_of_shape)

tim.reset()

#CHALLENGE 4
tim.speed("fast")
tim.pensize(10)
directions = [0,90,180,270]
for _ in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))

tim.reset()

#CHALLENGE 5
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5)

tim.reset()

tim.shape("turtle")
tim.forward(100) 

screen = t.Screen()
screen.exitonclick()
