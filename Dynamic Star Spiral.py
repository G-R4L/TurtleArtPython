import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")

# Turtle utama
tt = turtle.Turtle()
tt.speed(0)
tt.pensize(2)
colors = ["red", "yellow", "blue", "magenta", "cyan", "lime", "white"]

# Gambar pola bintang spiral
tt.penup()
tt.goto(0, 0)
tt.pendown()

for i in range(360):
    tt.pencolor(colors[i % len(colors)])  # Ganti warna tiap langkah
    tt.forward(i * 2)                     # Gerak maju semakin jauh
    tt.left(145)                          # Putar 145 derajat (membuat pola bintang)

tt.hideturtle()
turtle.done()
