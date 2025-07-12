import turtle
import random
import time
import math

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("💚 Matrix Love Rain")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.colormode(255)

# Turtle untuk menggambar karakter
rain = turtle.Turtle()
rain.hideturtle()
rain.penup()
rain.speed(0)

# Fungsi untuk mengecek apakah titik (x, y) ada dalam bentuk hati
def is_in_heart(x, y):
    x = x / 100
    y = y / 100
    equation = (x**2 + y**2 - 1)**3 - x**2 * y**3
    return equation <= 0

# Karakter-karakter yang akan jatuh seperti Matrix
chars = list("01♥")

# Buat list titik-titik dalam bentuk hati
heart_points = []
for y in range(-250, 250, 15):
    for x in range(-400, 400, 15):
        if is_in_heart(x, y):
            heart_points.append((x, y))

# Loop animasi Matrix Love Rain
while True:
    rain.clear()
    drops = random.sample(heart_points, 80)  # 80 titik acak dalam bentuk hati
    for (x, y) in drops:
        rain.goto(x, y)
        rain.color(0, random.randint(150, 255), 0)  # Hijau matrix
        rain.write(random.choice(chars), align="center", font=("Courier", 14, "bold"))

    screen.update()
    time.sleep(0.1)
