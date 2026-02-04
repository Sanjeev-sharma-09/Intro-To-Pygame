from sys import exit
import pygame

#Absolute necessary code which needs to written as it initiates all the important functions like rendering the images, playing
#sounds, etc.
pygame.init()

screen= pygame.display.set_mode((800, 500)) #This takes tupple as arguments .set_mode((width, height))
clock= pygame.time.Clock() #This helps us with time and controlling the framerates

pygame.display.set_caption("GAME NAME") #This sets the game title or window title

#To display components like images, text, color we can use either the display surface(main) or regular surface which we can create multiple
#and to show it, we need to connect it to the display surface(main)
test_surface= pygame.Surface((100, 100)) #Surface((width, height))
test_surface.fill("red") #Add color to a surface .fill((0, 0, 0)), it contains a rgb value of color or we could use specific name

test_surface_1= pygame.Surface((100, 100))
test_surface_1.fill("green")

test_surface_2= pygame.Surface((100, 100))
test_surface_2.fill("blue")

image_surface= pygame.image.load("graphics/dog.jpg") #To add image we use pygame.image.load("file_path")

#To add fonts we need to go through three steps -
#       1. create a font(text tyle, text size)
#       2. write text on a surface 
#       3. blit the text surface
text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 50) #.Font(font-style; if none- it uses pygame default, font-size; in pixels)
text_surface= text_font.render("Intro To PyGame", True, "white") #.render(text-to-display, AA(Anti-Aliasing); whether to smooth text edges
                                                                 #         takes boolean arguments, text-color)

#Game loop.
while True:
    
    #Checks the event/inputs the user is doing like pressing a button, keyboard, mouse clicking, etc.
    for event in pygame.event.get():
        
        if event.type== pygame.QUIT: #pygame.QUIT matches with the X button of window.
            
            pygame.quit() #This close/terminate the window and we get out of the loop.

            #This is used because above code is polar opposite of pygame.init(), so it un-initializes everthing. But the while loop is 
            #still running and pygame.display.update() code doesn't run because it needs to be initialized. Hence it gives an error
            #To fix this we use exit() method from sys module which completely stops the code. Hence. no more errors
            exit()

    #blit(Block Image Transfer) is a fancy name for putting one surface on top of eash other
    screen.blit(test_surface, (0, 0)) # display-surface(main).blit(surface-needs-to-display, (x, y) position where it needs to appear)
    screen.blit(test_surface_1, (100, 0))
    screen.blit(test_surface_2, (200, 0))

    screen.blit(image_surface, (300, 0)) #For Image

    screen.blit(text_surface, (220, 250))

    #This update all the changes happening on the window like drawing, etc to the actual window so that 
    #the user can see the changes.
    pygame.display.update() 

    #This sets the maximum framerates the game should run on. On this case, it is 60 fps
    clock.tick(60)
