import turtle

# --------------------------
# Doraemon
# --------------------------

def draw_doraemon():

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(0, -200)
    t.pendown()

    t.fillcolor("skyblue")
    t.begin_fill()
    t.circle(200)
    t.end_fill()

    t.penup()
    t.goto(0, -150)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()
    t.circle(150)
    t.end_fill()


# --------------------------
# Pikachu
# --------------------------

def draw_pikachu():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    for x in [-40, 40]:
        t.penup()
        t.goto(x, 120)
        t.pendown()
        t.dot(15)

    for x in [-60, 60]:
        t.penup()
        t.goto(x, 40)
        t.pendown()
        t.fillcolor("red")
        t.begin_fill()
        t.circle(15)
        t.end_fill()


# --------------------------
# Shinchan
# --------------------------

def draw_shinchan():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("peachpuff")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-40, 120)
    t.pendown()
    t.pensize(5)
    t.forward(30)

    t.penup()
    t.goto(20, 120)
    t.pendown()
    t.forward(30)


# --------------------------
# Nobita
# --------------------------

def draw_nobita():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("bisque")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-40, 120)
    t.pendown()
    t.circle(20)

    t.penup()
    t.goto(20, 120)
    t.pendown()
    t.circle(20)


# --------------------------
# Hello Kitty
# --------------------------

def draw_hello_kitty():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("white")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-20, 140)
    t.pendown()

    t.fillcolor("red")
    t.begin_fill()

    for _ in range(4):
        t.forward(40)
        t.left(90)

    t.end_fill()


# --------------------------
# Mickey Mouse
# --------------------------

def draw_mickey():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("black")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-70, 150)
    t.pendown()

    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(70, 150)
    t.pendown()

    t.begin_fill()
    t.circle(40)
    t.end_fill()


# --------------------------
# Minion
# --------------------------

def draw_minion():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("yellow")
    t.begin_fill()

    for _ in range(2):
        t.forward(120)
        t.left(90)
        t.forward(200)
        t.left(90)

    t.end_fill()


# --------------------------
# SpongeBob
# --------------------------

def draw_spongebob():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("yellow")
    t.begin_fill()

    for _ in range(4):
        t.forward(180)
        t.left(90)

    t.end_fill()


# --------------------------
# Totoro
# --------------------------

def draw_totoro():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("gray")
    t.begin_fill()
    t.circle(120)
    t.end_fill()


# --------------------------
# Smiley
# --------------------------

def draw_smiley():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    for x in [-40, 40]:
        t.penup()
        t.goto(x, 130)
        t.pendown()
        t.dot(15)

    t.penup()
    t.goto(-40, 60)
    t.pendown()
    t.setheading(-60)
    t.circle(50, 120)