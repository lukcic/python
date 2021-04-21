import turtle
bob = turtle.Turtle()
    
def square(name,length,angle):

    for i in range(4):
        name.fd(length)
        name.lt(angle)        
    print(name)

def polygon(name,length, n):

    for i in range(n):
        name.fd(length)
        name.lt(360/n)        
    print(name)

def circle(name, r):
    polygon(name,2,r)

def arc(name,len,angle):
    for i in range(angle):
        name.fd(len)
        name.lt(1)        
    print(name)


#square(bob,150, 90)
#polygon(bob, 50, 10)
#circle(bob,360)
arc(bob, 2, 300)

turtle.mainloop()
