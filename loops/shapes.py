from turtle import *
#speed('slowest')
for i in range(5):
    fd(100)
    lt(360/5)
penup()
goto(180,180)
pendown()
for i in range(6):
    fd(100)
    lt(360/6)
penup()
goto(0,-250)
pendown()
for i in range(7):
    fd(100)
    lt(360/7)
penup()
goto(-280,0)
pendown()
for i in range(8):
    fd(100)
    lt(360/8)
hideturtle() 
mainloop() 