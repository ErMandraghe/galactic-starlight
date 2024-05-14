import turtle
# simple star but william had fun modifying the original code
bob = turtle.Turtle()
bob.color("green", "cyan")
bob.begin_fill()
bob.speed(100)
def pen():
	bob.penup()
	bob.forward(100)
	bob.pendown()
def mov():
	bob.color("red")
	bob.forward(300)
	bob.right(175)
def movements():
	bob.forward(250)
	bob.left(178)
def forcycle():
	for x in range(92):
 		movements()
 		pen()
 		# movements()
def cycle():
	for x in range(92):
 		mov()
 		pen()
forcycle()
cycle()

bob.end_fill
turtle.done()
