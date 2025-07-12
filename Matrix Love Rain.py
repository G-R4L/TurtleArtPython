import turtle
import random
import time
import math

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("💚 Matrix Love Rain – Upgraded")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.colormode(255)  # Gunakan RGB (0-255)

# Turtle untuk menggambar karakter
rain = turtle.Turtle()
rain.hideturtle()
rain.penup()
rain.speed(0)

# Fungsi untuk mengecek apakah titik (x, y) ada dalam bentuk hati
def is_in_heart(x, y):
    x = x / 100
    y = y / 100
    return ((x**2 + y**2 - 1)**3 - x**2 * y**3) <= 0

# Karakter-karakter yang jatuh (Matrix Style)
chars = list("0 1 ♥ 1 0 1 0 ♥".split())

# Buat list titik-titik dalam bentuk hati
heart_points = []
for y in range(-250, 250, 12):  # Lebih rapat, agar padat
    for x in range(-400, 400, 12):
        if is_in_heart(x, y):
            heart_points.append((x, y))

# Loop animasi
while True:
    rain.clear()
    
    drops = random.sample(heart_points, 120)  # Tambah titik = makin rame
    for (x, y) in drops:
        # Warna hijau glow matrix
        green_shade = random.randint(180, 255)
        rain.color((0, green_shade, 0))  # Hijau menyala
        rain.goto(x, y)
        rain.write(random.choice(chars), align="center", font=("Courier", 12, "bold"))

    screen.update()
    time.sleep(0.08)
