#In this we will learn about rectangle's in pygame.. We can use and interact with surfaces in two ways- 1)We can use the original main 
#variable we declared it.. 2)We can store them again in a rectangle
#Storing a rectangle have its benefits- 1)We can use its any point(topleft, topright, bottom, etc) to adjust it to the game environment
#instead of using only top left(default for surface), which can be beneficial in certain ways
#2)We can use the rectangle to check for collisions which is very important further in this series
#So, here we will only learn about rectangles and how to implement it 

#We can simplify rectangle and surface via their roles- surface--contains actual info| rectangle--used for placements and other modification

#To draw a rectangle we can use pygame.Rect(left, top, width, heigth). But we want to create the rectangle as the same size as the surface
#To do that we need to further go down to where it is declared 

from sys import exit
import pygame

pygame.init()

screen= pygame.display.set_mode((800, 500))
clock= pygame.time.Clock() 

pygame.display.set_caption("Ulta Billi, Kautval ko Mare") 

background_surface= pygame.image.load("graphics/background.jpg")
background_surface= pygame.transform.smoothscale(background_surface, (800, 500))

dog_x_pos= 800
dog_surface= pygame.image.load("graphics/dog-pixel.png") #Dog image
dog_surface= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha() 
dog_surface_rect= dog_surface.get_rect() #This draws a rectangle around the same size as the surface.. We can also specify where certain position
                                         #should be like, .get_rect(topleft= (100, 100)) this here means that the topleft corner of the rectangle
                                         #is placed at the coordinates (100, 100)..

cat_x_pos= 1000 
cat_surface= pygame.image.load("graphics/cat-pixel.png") #Cat image
cat_surface= pygame.transform.smoothscale(cat_surface, (240, 150)).convert_alpha() 
cat_surface_rect= cat_surface.get_rect() #We can specify its where it should be placed.. but for me, already have made all the adjustment from
                                         #hard coding..

text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 70)
text_surface= text_font.render("Intro To Animation", True, "black")

dog_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
dog_text_surface= dog_text_font.render("Dogesh Bhai", True, "black")
dog_text_surface_x_pos= 765

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


    dog_text_surface_x_pos-= 8 
    if dog_text_surface_x_pos< -150: dog_text_surface_x_pos= 850
    screen.blit(dog_text_surface, (dog_text_surface_x_pos, 310)) #When we specify the position of the rectangles, we pass it instead of passing 
                                                                 #numeric coordinates

    #We moved the dog by defining it x position.. But working with rectangle we don't touch the actual surface
    #We move objects by moving the rectangle position itself
    #We write it as-
    # dog_surface_rect.-= 8
    # if dog_surface_rect.left< -100: dog_surface_rect.left= 900
    
    #It will only work when you have specified the rectangle's position, which i didn't hence it will not work for my code

    dog_x_pos-= 8 
    if dog_x_pos< -100: dog_x_pos= 900 
    screen.blit(dog_surface, (dog_x_pos, 325)) 
    
    cat_text_surface_x_pos-= 8 
    if cat_text_surface_x_pos< -200: cat_text_surface_x_pos= 800
    screen.blit(cat_text_surface, (cat_text_surface_x_pos, 255))

    cat_x_pos-= 8
    if cat_x_pos< -200: cat_x_pos= 800
    screen.blit(cat_surface, (cat_x_pos, 265))
    

    pygame.display.update() 
    clock.tick(45)