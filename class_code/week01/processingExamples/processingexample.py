
#this function runs once when your sketch launches 
def setup():
     #sets the size of the sketch window  
    size(1000,1000) 

#this funciton runs every frame     
def draw():
    #sets the background to a rgb value. mouseX and mouseY are values that
    #processing gives you for the position of the user's mouse. If you use
    #them here they will make the background change color as the user moves around
    background(mouseY, mouseX, mouseY) 
    #fill the ellipse. Again this is r,g,b, color space. 
    fill(mouseX, mouseY, 0)
    #draw a circle at 1/2 the width and height. Just like mouseX and mouseY, processing
    #gives you width and height as variables it sets up you can use. It's just the
    #width and height of the window 
    ellipse (width/2,height/2,mouseX,mouseX)

