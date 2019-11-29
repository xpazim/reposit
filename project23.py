#trampo de web

import turtle
from flask import Flask

app = Flask(__name__)
 
@app.route("/")

def Jogo():
    wn = turtle.Screen()
    wn.title("Ponguinho")
    wn.bgcolor("blue")
    wn.setup(width=800,height=600)
    wn.tracer(0)

#placar

    placar_a = 0
    placar_b = 0

#raquete a

    raq_a = turtle.Turtle()
    raq_a.speed(0)
    raq_a.shape("square")
    raq_a.color("white")
    raq_a.shapesize(stretch_wid=5,stretch_len=1)
    raq_a.penup()
    raq_a.goto(-350, 0)

#raquete b

    raq_b = turtle.Turtle()
    raq_b.speed(0)
    raq_b.shape("square")
    raq_b.color("white")
    raq_b.shapesize(stretch_wid=5,stretch_len=1)
    raq_b.penup()
    raq_b.goto(350, 0)

#bola

    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2

#Menu

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Jogador 1: 0  Jogador 2: 0", align="center", font=("Courier", 24, "normal"))

    def raq_a_up():
        y = raq_a.ycor()
        y += 20
        raq_a.sety(y)

    def raq_a_down():
        y = raq_a.ycor()
        y -= 20
        raq_a.sety(y)

    def raq_b_up():
        y = raq_b.ycor()
        y += 20
        raq_b.sety(y)

    def raq_b_down():
        y = raq_b.ycor()
        y -= 20
        raq_b.sety(y)

    wn.listen()
    wn.onkeypress(raq_a_up, "w")
    wn.onkeypress(raq_a_down, "s")
    wn.onkeypress(raq_b_up, "Up")
    wn.onkeypress(raq_b_down, "Down")

    while True:
        wn.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 350:
            placar_a += 1
            pen.clear()
            pen.write("Jogador 1: {}  Jogador 2: {}".format(placar_a, placar_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            placar_b += 1
            pen.clear()
            pen.write("Jogador 1: {}  Jogador 2: {}".format(placar_a, placar_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.ycor() < raq_a.ycor() + 50 and ball.ycor() > raq_a.ycor() - 50:
            ball.dx *= -1

        elif ball.xcor() > 340 and ball.ycor() < raq_b.ycor() + 50 and ball.ycor() > raq_b.ycor() - 50:
            ball.dx *= -1

        if placar_a == 20:
            pen.write("Jogador 1 Venceu",align="center",font=("Arial",15,"normal"))
            turtle.exitonclick()

        if placar_b == 20:
            pen.write("Jogador 2 Venceu", align="center", font=("Arial", 15, "normal"))
            turtle.exitonclick()

    app.run()
