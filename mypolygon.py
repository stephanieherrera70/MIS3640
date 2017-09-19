import turtle

Stephanie = turtle.Turtle()

print(Stephanie)
Stephanie.fd(100)
Stephanie.lt(90)
Stephanie.fd(100)
Stephanie.lt(90)
Stephanie.fd(100)
Stephanie.lt(90)
Stephanie.fd(100)


for i in range (4):
    print('Hello!')


for i in range (4):
    Stephanie.fd(100)
    Stephanie.lt(90)




def square(t):
    for i in range (4):
        t.fd(100)
        t.lt(90)

square(Stephanie)

def square(t, length):
    for i in range (4):
        t.fd(length)
        t.lt(90)
square(Stephanie, 50)



def polygon(t, length, n):
    for i in range (n):
        t.fd(length)
        t.lt(360/n)

polygon(Stephanie, 50, 8)

import math 
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n 
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

circle(Stephanie, 80)

# circle(Stephanie, 80)

#arc(Stephanie, 100, 180)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

#polygon(alex, 4, 100)
polyline(alex, 4, 100, 90)

turtle.mainloop()

 