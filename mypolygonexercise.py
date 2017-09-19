import turtle

stephanie = turtle.Turtle()

print(stephanie)

def yinyang(radius):
    stephanie.pensize(10)
    stephanie.circle(radius/2., 180)
    stephanie.circle(radius, 180)
    stephanie.left(180)
    stephanie.circle(-radius/2., 180)
    stephanie.left(90)
    stephanie.up()
    stephanie.forward(radius*0.35)
    stephanie.right(90)
    stephanie.down()
    stephanie.circle(radius*0.15)
    stephanie.left(90)
    stephanie.up()
    stephanie.backward(radius*0.35)
    stephanie.down()
    stephanie.left(90)


yinyang(200)
yinyang(200)

stephanie.mainloop()