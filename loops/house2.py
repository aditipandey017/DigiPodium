
from turtle import *
dis=[100,100,58,58]
ngl=[90,60,60,60]

for d, a in zip(dis,ngl):
    fd(d)
    lt(a)
fd(100)
penup()
goto(42,0)
pendown()

ngl=[90,90,90,90]
dis=[0,30,10,30]
for d, a in zip(dis,ngl):
    
    rt(a)
    fd(d)

ngl=[90,0,90,60,30,90,60,30]
dis=[0,200,100,58,150,0,58,150]
for d, a in zip(dis,ngl):
    
    lt(a)
    fd(d)
penup()
goto(150,60)
pendown()
ngl=[90,90,90,90]
dis=[30,20,30,20]
for d, a in zip(dis,ngl):
    
    
    fd(d)
    lt(a)
#hideturtle()
mainloop()