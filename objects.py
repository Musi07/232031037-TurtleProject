import turtle

# --------------------------
# House
# --------------------------

def draw_house():

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(4):
        t.forward(150)
        t.left(90)

    t.goto(0, 150)
    t.goto(75, 225)
    t.goto(150, 150)


# --------------------------
# Star
# --------------------------

def draw_star():

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(5):
        t.forward(150)
        t.right(144)


# --------------------------
# Heart
# --------------------------

def draw_heart():

    t = turtle.Turtle()
    t.speed(0)

    t.color("red")
    t.begin_fill()

    t.left(140)
    t.forward(180)
    t.circle(-90, 200)

    t.left(120)
    t.circle(-90, 200)

    t.forward(180)

    t.end_fill()


# --------------------------
# Flower
# --------------------------

def draw_flower():

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(8):
        t.circle(60)
        t.left(45)


# --------------------------
# Tree
# --------------------------

def draw_tree():

    t = turtle.Turtle()
    t.speed(0)

    t.left(90)
    t.forward(120)

    t.right(90)

    t.fillcolor("green")
    t.begin_fill()
    t.circle(60)
    t.end_fill()


# --------------------------
# Rocket
# --------------------------

def draw_rocket():

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(3):
        t.forward(120)
        t.left(120)


# --------------------------
# Robot
# --------------------------

def draw_robot():

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(4):
        t.forward(120)
        t.left(90)

    t.penup()
    t.goto(30, 140)
    t.pendown()
    t.circle(5)

    t.penup()
    t.goto(90, 140)
    t.pendown()
    t.circle(5)


# --------------------------
# Car
# --------------------------

def draw_car():

    t = turtle.Turtle()
    t.speed(0)

    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(70)
        t.left(90)

    t.penup()
    t.goto(40, -20)
    t.pendown()
    t.circle(20)

    t.penup()
    t.goto(160, -20)
    t.pendown()
    t.circle(20)


# --------------------------
# Boat
# --------------------------

def draw_boat():

    t = turtle.Turtle()
    t.speed(0)

    t.forward(150)

    t.right(135)
    t.forward(70)

    t.right(90)
    t.forward(70)

    t.right(135)
    t.forward(150)

    t.penup()
    t.goto(75, 0)
    t.pendown()

    t.left(180)
    t.forward(100)

    t.right(90)
    t.forward(70)

    t.right(135)
    t.forward(100)


# --------------------------
# Ice Cream
# --------------------------

def draw_icecream():

    t = turtle.Turtle()
    t.speed(0)

    t.fillcolor("pink")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(-20, -10)
    t.pendown()

    t.fillcolor("tan")
    t.begin_fill()

    t.goto(20, -10)
    t.goto(0, -120)
    t.goto(-20, -10)

    t.end_fill()