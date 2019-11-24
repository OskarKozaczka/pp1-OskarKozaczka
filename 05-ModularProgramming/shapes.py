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
        
def drawStar(x,y,r):
    pen.speed(0)
    r=r*100
    pen.penup()
    pen.setposition(x*100,y*100+r*3)
    pen.setheading(90)
    pen.pendown()
    pen.right(180-18)
    pen.forward(2*r)
    pen.left(72)
    pen.forward(2*r)
    pen.right(180-36)
    pen.forward(2*r)
    pen.left(72)
    pen.forward(2*r)
    pen.right(180-36)
    pen.forward(2*r)
    pen.left(72)
    pen.forward(2*r)
    pen.right(180-36)
    pen.forward(2*r)
    pen.left(72)
    pen.forward(2*r)
    pen.right(180-36)
    pen.forward(2*r)
    pen.left(72)
    pen.forward(2*r)

    
def drawCircle(x,y,r):
    pen.speed(0)
    pen.penup()
    pen.setposition(x,y-r)
    #pen.setheading(0)
    pen.pendown()
    pen.circle(r)
    
def drawTriangle(x,y,m):
    pen.speed(0)
    
    pen.penup()
    pen.setposition(x,y)
    pen.setheading(270+30)
    pen.pendown()
    pen.forward(m)
    pen.right(90+30)
    pen.forward(m)
    pen.right(90+30)
    pen.forward(m)

def drawBlackSquare(x,y,m):                       
    pen.speed(0)
    pen.penup()
    pen.setposition(x,y)
    pen.pendown()
    pen.fillcolor("black")
    pen.begin_fill()
    drawSquare(x,y,m)
    pen.end_fill()



    
    
def drawChees(m):
    drawSquare(0,0,m)
    drawBlackSquare(m,0,m)
    drawSquare(2*m,0,m)
    drawBlackSquare(3*m,0,m)
    
    drawBlackSquare(0,-m,m)
    drawSquare(m,-m,m)
    drawBlackSquare(m*2,-m,m)
    drawSquare(m*3,-m,m)
    
    drawSquare(0,-2*m,m)
    drawBlackSquare(m,-2*m,m)
    drawSquare(2*m,-2*m,m)
    drawBlackSquare(3*m,-2*m,m)
    
    drawBlackSquare(0,-3*m,m)
    drawSquare(m,-3*m,m)
    drawBlackSquare(m*2,-3*m,m)
    drawSquare(m*3,-3*m,m)
    
drawChees(1)