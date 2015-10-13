
#set up s for the first time
s = "Python is great!"

#defining a funciton to show you how global works
def using_global():
    #remember that all of the tabbed in code lines are inside of this function
    #gives us access to the variable s outside the function
    global s
    #prints s
    print s
    #changes s
    s = "That's clear."
    #prints s again
    print s 

#we are now outside the function. Remember the tab is what sets lines of code to be inside a function. No more tab space? We're outside!

#call our function. this call makes all of the code inside the function definition starting on line 6 run. It runs the code through line 15.
using_global()

#print s again now we are outside and finished with the function to see that inside the
#function, because we had access to the variable outside the funciton, when we changed
#the value inside it, we changed it outside as well. :)
print s