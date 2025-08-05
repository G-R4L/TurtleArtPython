from turtle import *
from colorsys import *
bgcolor("black")
tracer(20)
pensize(2)
j=0
goto(-140,170)
for i in range(250):
    c=hsv_to_rgb(j,1,1)
    fillcolor(c)
    begin_fill()
    left(119)
    circle(25,180)
    circle(-25,180)
    circle(20)
    backward(350-i)
    j+=0.004
    end_fill()
done()
