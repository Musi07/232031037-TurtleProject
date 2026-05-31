import turtle

# --------------------------
# Panda
# --------------------------

def draw_panda():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("white")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-50, 120)
    t.pendown()
    t.dot(40, "black")

    t.penup()
    t.goto(50, 120)
    t.pendown()
    t.dot(40, "black")

    t.penup()
    t.goto(-30, 70)
    t.pendown()
    t.dot(30, "black")

    t.penup()
    t.goto(30, 70)
    t.pendown()
    t.dot(30, "black")


# --------------------------
# Cat
# --------------------------

def draw_cat():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("orange")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # left ear
    t.penup()
    t.goto(-60, 140)
    t.pendown()

    t.begin_fill()
    for _ in range(3):
        t.forward(40)
        t.left(120)
    t.end_fill()

    # right ear
    t.penup()
    t.goto(60, 140)
    t.pendown()

    t.begin_fill()
    for _ in range(3):
        t.forward(40)
        t.left(120)
    t.end_fill()


# --------------------------
# Dog
# --------------------------

def draw_dog():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("brown")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-80, 120)
    t.pendown()

    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(80, 120)
    t.pendown()

    t.begin_fill()
    t.circle(30)
    t.end_fill()


# --------------------------
# Bear
# --------------------------

def draw_bear():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("saddlebrown")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-60, 140)
    t.pendown()
    t.circle(25)

    t.penup()
    t.goto(60, 140)
    t.pendown()
    t.circle(25)


# --------------------------
# Rabbit
# --------------------------

def draw_rabbit():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("white")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # left ear
    t.penup()
    t.goto(-40, 100)
    t.pendown()

    t.fillcolor("white")
    t.begin_fill()

    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(100)
        t.left(90)

    t.end_fill()

    # right ear
    t.penup()
    t.goto(20, 100)
    t.pendown()

    t.begin_fill()

    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(100)
        t.left(90)

    t.end_fill()