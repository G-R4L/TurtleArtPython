import turtle
import colorsys

turtle.bgcolor("black")
tt = turtle.Turtle()
tt.speed(0)
tt.width(2)
tt.hideturtle()

n = 36  # jumlah warna
hues = [x/n for x in range(n)]
colors = [colorsys.hsv_to_rgb(h, 1, 1) for h in hues]

for i in range(360):
    c = colors[i % n]
    tt.pencolor(c[0], c[1], c[2])
    tt.forward(i * 3 / n + i)
    tt.right(59)

turtle.done()
