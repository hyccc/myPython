import turtle


turtle.pensize(3)
turtle.penup()
turtle.goto(-180, 2)
turtle.pencolor('red')
turtle.fillcolor('yellow')
turtle.pendown()
turtle.begin_fill()
for _ in range(2):
    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()
turtle.mainloop()