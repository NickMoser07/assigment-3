import turtle as t

x = int(input("where do you want your circle x (-150, 150)"))
y = int(input("where do you want your circle x (-150, 150)"))

radius = int(input("what is the diameter of your inner circle"))
radius /= 2
radius = int(radius)
finished = input("press enter to draw")

#drawing
t.speed(0)
t.penup()
t.goto(x,y)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(radius*4)
t.end_fill()
t.penup()
t.goto(x,y+radius)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(radius*3)
t.end_fill()
t.penup()
t.goto(x,y+radius*2)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(radius*2)
t.end_fill()
t.penup()
t.goto(x,y+radius*3)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(radius)
t.end_fill()
t.hideturtle()

finish = input("press enter to end")