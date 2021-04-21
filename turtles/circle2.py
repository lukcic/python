import turtle
import math

bob = turtle.Turtle()

def polygon(name, lenght, n):
    for i in range(n):
        name.fd(lenght)
        name.lt(360/n)
    print(name)

#polygon(bob,5,360)

def circle(name, r):
    obw = 2 * math.pi * r
    n = int(obw /3 ) +1
    lenght = obw / n
    polygon(name, lenght, n)

#circle(bob, 500)

def polyline(name, lenght, n, angle):
    for i in range(n):
        name.fd(lenght)
        name.lt(angle)
    print(name)

#polyline(bob, 5, 300, 1)

def polygon2(name, lenght, angle):
    n=int(360/angle)
    polyline(name, lenght, n, angle)

#polygon2(bob, 100, 90)

def arc(name, lenght, angle):
    angle = 
    polyline(name, lenght, n, 1)
arc(bob, 10, 1)

turtle.mainloop()