from turtle import *
'''speed('fastest')
bgcolor('black')
pencolor('yellow')
pensize(2)
'''
from turtle import *
dis=[100,100,58,58]
ngl=[90,60,60,60]

for d, a in zip(dis,ngl):
    fd(d)
    lt(a)
fd(100)
penup()
goto(41,0)
pendown()

ngl=[90,90,90,90]
dis=[0,30,10,30]
for d, a in zip(dis,ngl):
    
    rt(a)
    fd(d)

#hideturtle()
mainloop()