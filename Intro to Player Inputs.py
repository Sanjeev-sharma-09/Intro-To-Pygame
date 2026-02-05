#In this we will implement player inputs to make the dog jump

from sys import exit
import pygame

pygame.init()

screen= pygame.display.set_mode((800, 500))
clock= pygame.time.Clock() 

pygame.display.set_caption("Ulta Billi, Kautval ko Mare") 

background_surface= pygame.image.load("graphics/background.jpg")
background_surface= pygame.transform.smoothscale(background_surface, (800, 500))

#Here i have imported the background as whole which is a problem as it poses a challenge to create a floor which could have been easier if 
#created a separate variable for it.. 
#We are creating the floor so that our dog stand on something when working with player input otherwise it will fall from the screen
floor_rect= pygame.Rect(0, 405, 800, 95)

text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 70)
text_surface= text_font.render("Intro To Pygame", True, "black")

dog_x_pos= 80 
dog_surface= pygame.image.load("graphics/dog-pixel.png") 
dog_surface= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha() 
dog_surface_rect= dog_surface.get_rect(topleft = (80, 325)) 

dog_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
dog_text_surface= dog_text_font.render("Dogesh Bhai", True, "black")
dog_text_surface_x_pos= 55 

#Creating dog gravity to make it fall downwards when jumping
dog_gravity= 0

cat_x_pos= 1000 
cat_surface= pygame.image.load("graphics/cat-pixel.png")
cat_surface= pygame.transform.smoothscale(cat_surface, (240, 150)).convert_alpha() 
cat_surface_rect= cat_surface.get_rect(topleft = (1000, 272)) 

cat_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
cat_text_surface= dog_text_font.render("Billu Don", True, "black")
cat_text_surface_x_pos= 1085


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:   
            pygame.quit() 
            exit()

        #Checking for the keyboard inputs
        if event.type== pygame.KEYDOWN: #This check if any key was pressed or not 
            if event.key== pygame.K_SPACE:
                dog_gravity= -20 #This here create a way that looks like the dog is jumping
                
        
    

    #To access the keys we use and we store it in a dictionary to access specific keys 
    # keys= pygame.key.get_pressed() #This will check which key is pressed 
    # if keys[pygame.K_SPACE]: #This is here for space
    #    print("jump")
    #This code here can be done in event loop also .. and we will have more control over the key than we have here 
    #So, i will be commenting it out .. but you can un-comment it and can run it as you like

    screen.blit(background_surface, (0, 0)) 
    screen.blit(text_surface, (120, 20))

    screen.blit(dog_text_surface, (dog_surface_rect.x- 30, dog_surface_rect.y- 20))
    screen.blit(dog_surface, dog_surface_rect) 
    
    dog_gravity+= 1
    dog_surface_rect.y+= dog_gravity
    if dog_surface_rect.bottom> 425: dog_surface_rect.bottom= 425
    
    
    
    
    
    cat_surface_rect.x -= 8
    if cat_surface_rect.right < 0: 
        cat_surface_rect.left = 800
    screen.blit(cat_surface, cat_surface_rect)
    screen.blit(cat_text_surface, (cat_surface_rect.x+ 85, cat_surface_rect.y- 10))

    


    pygame.display.update() 
    clock.tick(45)