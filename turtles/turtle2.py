import turtle
import math

bob = turtle.Turtle()

def polygon(name, lenght, n):
    for i in range(n):
        name.fd(lenght)
        name.lt(360/n)
    print(name)

def circle(name, r):
    obw = 2 * math.pi * r
    n = int(obw /3 ) +1
    lenght = obw / n
    polygon(name, lenght, n)

#polygon(bob,5,360)
circle(bob, 500)


turtle.mainloop()