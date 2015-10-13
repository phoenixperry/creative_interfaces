__author__ = 'phoenixperry'
def setup():
    background(0)
    size(1024,768)

def draw():
    #experiment with uncommenting this line. If you redraw the background everyframe
    # it's like shaking your etch-a-sketch. It clears it, otherwise the drawing will buildup.
    #background(0)
    #give us a random color for r, g and b!
    stroke(255, random(0,255), random(0,255))
    #let's try to draw something less regular, like a triangle. For that we will need this beginShape function
    beginShape()
    #let's not fill this shape and only use a stoke outline defined above
    noFill()

    #of course you could also fill it, just uncomment here
    #fill(250,random(0,255), random(0,255))
    #point 1 in  our shape
    vertex(mouseY, random(0,width))
    #point 2
    vertex(mouseX, random(0,width))
    #point 3
    vertex(mouseX, random(0,width))
    #end the shape!
    endShape()  