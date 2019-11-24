import shapes



#shapes.drawSquare()
ix=0
iy=0

for ix in range(4):
    shapes.drawSquare(ix,iy,1)
    for iy in range(4):
        shapes.drawSquare(ix,iy,1)
        
#turtle.done()