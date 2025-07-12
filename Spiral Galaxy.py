# Import Turtle
import turtle
import colorsys

# Setup layar
turtle.bgcolor("black")
tt = turtle.Turtle()
tt.speed(0)
tt.width(2)
tt.penup()
tt.goto(0, 0)
tt.pendown()
turtle.colormode(255)
tt.hideturtle()

# Inisialisasi
forward_dist = 0
rotate_angle = 0
steps = 210

# Warna pelangi
def get_color(i, total):
    hue = i / total
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return int(r * 255), int(g * 255), int(b * 255)

# Loop spiral galaksi
for i in range(steps):
    tt.pencolor(get_color(i, steps))     # Ganti warna tiap langkah
    tt.forward(forward_dist)
    tt.left(rotate_angle)                # Berbeda: ke kiri
    forward_dist += 2.5
    rotate_angle += 1.5

turtle.done()
