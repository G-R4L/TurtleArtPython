import turtle
import math
import colorsys

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Mouse-Controlled Spiral Art")
screen.tracer(0)  # Nonaktifkan animasi agar lebih halus

# Konfigurasi turtle
tt = turtle.Turtle()
tt.hideturtle()
tt.speed(0)
tt.pensize(2)
screen.colormode(1.0)

# Fungsi untuk membuat warna pelangi (HSV ke RGB)
def rainbow(i, total):
    hue = i / total
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

# Fungsi menggambar spiral dari titik mouse
def draw_spiral(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

    angle = 0
    radius = 0
    total = 100  # Jumlah langkah spiral

    for i in range(total):
        angle += 12
        radius += 2
        color = rainbow(i, total)
        tt.pencolor(color)

        new_x = x + math.cos(math.radians(angle)) * radius
        new_y = y + math.sin(math.radians(angle)) * radius
        tt.goto(new_x, new_y)

    screen.update()

# Event: klik mouse untuk menggambar spiral
screen.onclick(draw_spiral)

screen.listen()
turtle.done()
