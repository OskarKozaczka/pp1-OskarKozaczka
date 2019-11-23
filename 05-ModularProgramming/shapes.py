import turtle

pen = turtle.Turtle()

def drawSquare(x,y,n):
    
    pen.speed(0)
    pen.penup()
    pen.setposition(x*100,y*100)
    pen.pendown()
    for i in range(4):
        pen.forward(100*n)
        pen.right(90)     # Rotate clockwise by 90 degrees