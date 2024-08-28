import turtle
import math
def hearta(k):
    return 15 * math.sin(k)**3
def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(
        3 * k) - math.cos(4 * k)
window = turtle.Screen()
window.setup(800, 600)
window.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

for i in range(6000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    pen.goto(x, y)

    r = abs(math.sin(i / 300))
    g = abs(math.sin(i / 200))
    b = abs(math.sin(i / 100))
    pen.pencolor(r, g, b)
    pen.pendown()
pen.penup()
pen.goto(0, -50)
pen.color("white")
pen.write("Je t' aime", align="center", font=("Arial", 24, "normal"))
turtle.done()
