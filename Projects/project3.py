# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)



######################################################################
# https://en.wikipedia.org/wiki/Web_colors#Extended_colors
# Section 2 - Your code
set_background("switz")
#The colors for the rectangles
draw_rectangle("royal blue", 100, 100, 200, 200)
draw_rectangle("blue", -100, 100, 200, 200)
draw_rectangle("light blue", 100, -100, 200, 200)
draw_rectangle("navy blue", -100, -100, 200, 200)
#My sprites of things I like
s1 = create_sprite("volley", 100, 100)
s2 = create_sprite("dog", -100, -100)
s3 = create_sprite("boba",-100, 100)
s3 = create_sprite("aiglon", 100, -100)
#text yay!
message1 = create_sprite("dog",-200,200)
message1.color("pink")
message1.write("Sahasra",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("cat", -200,-250) 
message2.color("pink")
message2.write("Things that I like", font = ("Arial", 40, "normal"))
message2. hideturtle()
######################################################################


# Section 3 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()