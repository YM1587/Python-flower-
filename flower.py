import turtle

def draw_flower():
    turtle.speed(2)  # Moderate speed
    turtle.bgcolor("white")
    turtle.color("red")

    # Move to starting position
    turtle.penup()
    turtle.setheading(90)
    turtle.fd(200)
    turtle.setheading(0)
    turtle.pendown()

    # Draw flower (petal)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(10,180)
    turtle.circle(25,110)
    turtle.left(50)
    turtle.circle(60,45)
    turtle.circle(20,170)
    turtle.right(24)
    turtle.fd(30)
    turtle.left(10)
    turtle.circle(30,110)
    turtle.fd(20)
    turtle.left(40)
    turtle.circle(90,70)
    turtle.circle(30,150)
    turtle.right(30)
    turtle.fd(15)
    turtle.circle(80,90)
    turtle.left(15)
    turtle.fd(45)
    turtle.right(165)
    turtle.fd(20)
    turtle.left(155)
    turtle.circle(150,80)
    turtle.left(50)
    turtle.circle(150,90)
    turtle.end_fill()

    # Second petal curve to return to stem
    turtle.left(180)
    turtle.circle(90,40)
    turtle.circle(-80,98)

    # Draw stem (straight down)
    turtle.setheading(-90)
    turtle.color("green")
    turtle.pensize(10)
    turtle.forward(200)

    # Draw left leaf
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.left(45)
    turtle.circle(-50, 90)
    turtle.right(90)
    turtle.circle(-50, 90)
    turtle.end_fill()

    # Position for right leaf
    turtle.setheading(-90)
    turtle.fd(60)
    turtle.begin_fill()
    turtle.right(45)
    turtle.circle(50, 90)
    turtle.left(90)
    turtle.circle(50, 90)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

draw_flower()
