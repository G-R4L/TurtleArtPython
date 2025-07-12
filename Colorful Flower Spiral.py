import turtle
import colorsys

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle utama
tt = turtle.Turtle()
tt.speed(0)
tt.width(2)
tt.hideturtle()

# Fungsi warna HSL ke RGB (gradasi pelangi)
def get_color(i, total):
    hue = i / total
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return (r, g, b)

# Aktifkan mode warna RGB
screen.colormode(1.0)

# Gambar bunga spiral
total = 100
for i in range(total):
    tt.color(get_color(i, total))  # Warna pelangi
    tt.circle(100)
    tt.left(360 / total)
    tt.forward(4)

turtle.done()
