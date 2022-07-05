from  turtle import *
import time
from random  import *
setup(800,500)
title("TurtleRace")
bgcolor("forestgreen")

penup()
goto(-100,250)
color("white")
write("TUTLE RACE",font=("Arial",20,"bold"))

goto(-350,200)
pendown()
color("chocolate")
begin_fill()
forward(700)
right(90)
forward(400)
right(90)
forward(700)
right(90)
forward(400)
right(90)
end_fill()

gap_size =20
shape("square")
penup()

color("white")
for i in range(10):
    goto(250,(170-(i*gap_size*2)))
    stamp()
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()
color("black")
for i in range(10):
    goto(250,(190-(i*gap_size*2)))
    stamp()
for i in range(10):
    goto( ((251 +gap_size),((190 - gap_size) - (i * gap_size * 2))))
    stamp()
blue_turtle=Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300,150)
blue_turtle.pendown()

pink_turtle=Turtle()
pink_turtle.color("magenta")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300,50)
pink_turtle.pendown()

yellow_turtle=Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300,-50)
yellow_turtle.pendown()

green_turtle=Turtle()
green_turtle.color("lime")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300,-150)
green_turtle.pendown()



time.sleep(1)

# move blue turtle

while blue_turtle.xcor()<=230 and pink_turtle.xcor()<=230 and yellow_turtle.xcor()<=230 and green_turtle.xcor()<=230:
    blue_turtle.fd(randint(1,10))
    pink_turtle.fd(randint(1, 10))
    yellow_turtle.fd(randint(1, 10))
    green_turtle.fd(randint(1, 10))


if blue_turtle.xcor()>pink_turtle.xcor() and blue_turtle.xcor()>yellow_turtle.xcor() and blue_turtle.xcor()>green_turtle.xcor():
     print("Blue Turtle wins!")
     for i in range(72):
         blue_turtle.right(5)
         blue_turtle.shapesize(2.5)

elif pink_turtle.xcor()>blue_turtle.xcor() and pink_turtle.xcor()>yellow_turtle.xcor() and pink_turtle.xcor()>green_turtle.xcor():
    print("Pink turtlr wins!")
    for i in range(72):
        pink_turtle.right(5)
        pink_turtle.shapesize(2.5)

elif yellow_turtle.xcor() > pink_turtle.xcor() and yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor() > green_turtle.xcor():
    print("Yellow turtle wins!")
    for i in range(72):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(2.5)

else:
    print("Green turtle wins!")
    for i in range(72):
        green_turtle.right(5)
        green_turtle.shapesize(2.5)
