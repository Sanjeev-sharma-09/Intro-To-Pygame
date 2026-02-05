#In this we will learn about collision and rectangle is useful to check collision of two objects 

from sys import exit
import pygame

pygame.init()

screen= pygame.display.set_mode((800, 500))
clock= pygame.time.Clock() 

pygame.display.set_caption("Ulta Billi, Kautval ko Mare") 

background_surface= pygame.image.load("graphics/background.jpg")
background_surface= pygame.transform.smoothscale(background_surface, (800, 500))

text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 70)
text_surface= text_font.render("Intro To Collision", True, "black")

dog_x_pos= 80 #Moving it to right 

dog_surface= pygame.image.load("graphics/dog-pixel.png") 
dog_surface= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha() 
dog_surface_rect= dog_surface.get_rect(topleft = (80, 325)) #Specifying the position

dog_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
dog_text_surface= dog_text_font.render("Dogesh Bhai", True, "black")

dog_text_surface_x_pos= 55 #Matching the position of the dog

cat_x_pos= 1000 
cat_surface= pygame.image.load("graphics/cat-pixel.png")
cat_surface= pygame.transform.smoothscale(cat_surface, (240, 150)).convert_alpha() 
cat_surface_rect= cat_surface.get_rect(topleft = (1000, 265)) #Specifying the position

cat_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
cat_text_surface= dog_text_font.render("Billu Don", True, "black")
cat_text_surface_x_pos= 1085


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:   
            pygame.quit() 
            exit()

    screen.blit(background_surface, (0, 0)) 
    screen.blit(text_surface, (80, 80))

    #Here we are fixing the dog position so we could make it collide with the cat
    # dog_text_surface_x_pos-= 8 
    # if dog_text_surface_x_pos< -150: dog_text_surface_x_pos= 850
    screen.blit(dog_text_surface, (dog_text_surface_x_pos, 310))

    # dog_x_pos-= 8 
    # if dog_x_pos< -100: dog_x_pos= 900 
    screen.blit(dog_surface, dog_surface_rect) #Bliting the screen at the correct position for surface at its rectangle position
    
    #Modifying the rectangle position to work with it efficiently 
    cat_surface_rect.x -= 8
    if cat_surface_rect.right < 0: 
        cat_surface_rect.left = 800
    screen.blit(cat_text_surface, cat_surface_rect)

    cat_x_pos-= 8
    if cat_x_pos< -200: cat_x_pos= 800
    screen.blit(cat_surface, (cat_x_pos, 265))


    #To check collision we write rect1.colliderect(rect2); rect1 is whom the rect2 is colliding with..
    #This returns either 0 or 1 (0= False| 1= True)
    if dog_surface_rect.colliderect(cat_surface_rect):
        print("collision")

    #There is also a different collide code i.e., rect1.collidepoint((x, y)) as the name suggest it checks whether a point is colliding with 
    #rectangle or not 
    #This code is usefull if we are going to use our mouse in the game 
    mouse_pos= pygame.mouse.get_pos() #This will get the x and y position of mouse cursor 
    if dog_surface_rect.collidepoint(mouse_pos): #This will check if the mouse position is inside the rectangle or not.. if yes then it will print collision
        print("collision")                       #We can also do this in an event loop 

    #We can also draw shapes within the boundary of the rectangle with command
    #pygame.draw.{shape}rect(screen{what surface we want to draw on}, color, rect{where to})


    pygame.display.update() 
    clock.tick(45)