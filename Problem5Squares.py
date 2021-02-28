Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> def drawSquare(t, sz):
	"""Get turtle t to draw a square of sz side"""
	for i in range(4):
		t.forward(sz)
		t.left(90)

		
>>> wn = turtle.Screen()
>>> 
>>> alex = turtle.Turtle()
>>> alex.color("blue")
>>> alex.pensize(3)
>>> sz = 20
>>> x = 0
>>> y = 0
>>> for i in range(5):
	drawSquare(alex, sz)
	sz =sz+20
	x = x-10
	y = y-10
	alex.penup()
	alex.setposition(x,y)
	alex.pendown()

	
>>> wn.exitonclick()
>>> 