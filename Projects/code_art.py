import turtle

t = turtle.Turtle()
t. speed(100)

turtle.Screen() .bgcolor("black")

t.goto(100, 0)
colors =["royal blue","white","red"]
#changed one of the colors from sky blue to white.
for i in range(500):
    t.color( colors[ i % 3 ] )
    t.forward(90 + i)
    t.left(100 +1)
    t.forward(60 + i)
    t.left(50 +1)
    t.forward(30 + i)
    t.left(100 +1)
    t.forward(120 + i)
    t.left(50 +1)
#changed the shape because i didn't like it.
#closed the whole
turtle.exitonclick()