
#note this little trick. True will ALWAYS be true. The exit condition in this case is the break statement. It breaks you out of the loop
while True:
    #try this out to see if you have an int from the user 
    try:
        x = int(raw_input("Please enter a number: "))
        print("you entered in " + str(x))
        #break out of the loop
        break
    #this exception is really cool. if this above gives a valueError, this code runs until the user give an int. 
    except ValueError:
        print "Oops!  That was no valid number.  Try again..."
        
print "we are done now!" 