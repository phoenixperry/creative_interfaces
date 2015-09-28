#set up a variable for x and y position 
xpos = 0
ypos = 0

#this function runs once when your sketch launches 
def setup():
    #sets the background to black. 
    background(0)
    #sets the size 
    size(1000,1000)
    #sets a value for xpos and ypos 
    xpos = 10
    ypos = 10

#this funciton runs every frame 
def draw():
    #this sets a fill color for your shape in r,g,b color space. The values are 0-255
    fill(xpos,ypos,0)
    #this increments x each frame 
    xpos = xpos + 10
    #this increments y each frame

    #this allows this function access to the varaible xpos declared outside of it 
    global xpos
    #this allows this function access to the varaible xpos declared outside of it
    global ypos

    #adds 5 to these variables each frame 
    xpos +=5
    ypos +=5
    
    #draws a circle at the values of the variables
    #note random(50) gives you a value that's between 0 and 50 and random! It's
    #lots of fun. See the processing documentation for more details 
    ellipse(xpos,ypos, random(50),random(50))

    #this is just an alternate shape, you can uncomment it to see what it does
    #width and height are automatically known by processing as the width and
    #height of your sketch window. You set these in setup in the size function above
    ##rect(xpos, ypos, width, height)


