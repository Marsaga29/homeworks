from turtle import*


# we want to paint a house

# step 1; draw a square
speed(10)
shape("turtle")
color("red")
width(8)
forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90) 

forward(300)
left(90)
# end of square


# step 2: draw a door

forward(110) 
color("black")
begin_fill()
left(90)
forward (150)
right(90)
forward(80)
right(90)
forward(150)
end_fill()

# step 3: draw a roof

penup()
goto(300,300)
pendown()

color("black")
begin_fill()
right(120)
forward(175)
left(60)
forward(175)
end_fill()

penup()
goto(40,260)
pendown()

# drawing windows
color("yellow")
begin_fill()
left(60)
forward(80)
left(90)
forward(50)
left(90)
forward(80)
left(90)
forward(50)

penup()
goto(260,260)
pendown()

right(270)
forward(80)
right(90)
forward(50)
right(90)
forward(80)
right(90)
forward(50)
end_fill()

exitonclick()
