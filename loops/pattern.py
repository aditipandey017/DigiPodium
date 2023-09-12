from turtle import *
speed('fastest')
bgcolor('black')
pencolor('yellow')
pensize(1)

'''for i in range(1,500,5):
    fd(i)
    lt(360/6)
    write(i)'''

for i in range(100,0,-1):
    fd(i)
    lt(360/6)
    write(i)
    circle(i)
hideturtle()
mainloop()