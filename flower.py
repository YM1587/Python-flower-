import turtle

def draw_flower():
    turtle.speed(2)
    turtle.bgcolor("white")
    turtle.color("red")

    # Move to starting point for flower (centered above stalk)
    turtle.penup()
    turtle.goto(0, 100)  # Center of flower
    turtle.setheading(0)
    turtle.pendown()

    # Draw flower petals
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

    # Curve back toward center for stem base
    turtle.left(180)
    turtle.circle(90,40)
    turtle.circle(-80,98)

    # Draw stem starting directly beneath flower
    turtle.penup()
    turtle.goto(0, 100)  # Re-align to center
    turtle.setheading(-90)
    turtle.pendown()
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

    # Move to position for right leaf
    turtle.setheading(-90)
    turtle.penup()
    turtle.forward(60)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(45)
    turtle.circle(50, 90)
    turtle.left(90)
    turtle.circle(50, 90)
    turtle.end_fill()

    turtle.hideturtle()
    turtle.done()

draw_flower()
