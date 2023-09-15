from turtle import *
speed('fastest')
move=5
while True:
    for i in range(6):
        fd(100+5)
        for i in range(6):
            fd(50)
            rt(60)
        rt(60)
    rt(5)
    move+=5
hideturtle()
mainloop()