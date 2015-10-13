

#this function runs once when your sketch launches 
def setup(): 
    #sets the background color to grey black. 
    background(10,10,10)
    #sets the size of the sketch window  
    size(1000,1000)
    
#this funciton runs every frame         
def draw():
    #sets a fill color
    fill(mouseX, mouseY, 0)
    #uses the fill color to draw a box at the position of the user's mouse
    rect(mouseX, mouseY, mouseX*.10, mouseY*.10) 

