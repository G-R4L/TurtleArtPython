import turtle
import colorsys

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("black")
tt = turtle.Turtle()
tt.speed(0)
tt.width(2)
tt.hideturtle()
turtle.colormode(255)

# Fungsi warna dari merah ke ungu
def red_to_purple(i, total):
    hue = 0.95 * (i / total)  # HSV ke RGB, hue mendekati ungu
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return int(r * 255), int(g * 255), int(b * 255)

# Inisialisasi spiral
forward_dist = 0
rotate_angle = 0
steps = 220

tt.penup()
tt.goto(0, 0)
tt.pendown()

# Loop spiral bintang berduri
for i in range(steps):
    tt.pencolor(red_to_purple(i, steps))
    tt.forward(forward_dist)
    tt.right(144)  # Sudut tajam (seperti bintang 5)
    forward_dist += 3

turtle.done()
