#This here covers for the animation part in pygame... the file "Intro to Pygame" contains the basic structure of pygame how you can make
#images, text display on the screen... It also covers the basic functionality to the structure of how the game is made
#This file is different from the "Intro to Pygame" as of images only.. the structure remains same...
#Any changes made is started with a comment, same as with new changes.. if not, it is either covered before or the changes is not worth while

from sys import exit
import pygame

pygame.init()

screen= pygame.display.set_mode((800, 500))
clock= pygame.time.Clock() 

pygame.display.set_caption("Ulta Billi, Kautval ko Mare") #Title is based on idiom but a little touch from myself

background_surface= pygame.image.load("graphics/background.jpg")
background_surface= pygame.transform.smoothscale(background_surface, (800, 500))

#To work with animation we need to change the position of a surface, so it appears moving.. and to do that we need to create a variable
#for position of surface we need to animate 
dog_x_pos= 800
dog_surface= pygame.image.load("graphics/dog-pixel.png") #Dog image
dog_surface= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha() #This transform the size of a surface; .smoothscale-> smooths the image
                                                                                   #whereas, .scale does the same but with less smooth images
                                                                                   #it takes tupple as argument for new scale (width, height)

cat_x_pos= 1000 
cat_surface= pygame.image.load("graphics/cat-pixel.png") #Cat image
cat_surface= pygame.transform.smoothscale(cat_surface, (240, 150)).convert_alpha() #We use .convert() method to convert our png/jpg file into a more
                                                                                   #flexible way that pygame can use very easily..
                                                                                   #.convert_alpha() is used to remove the black and white part of the image
                                                                                   #We can ignore it, if not a lot is happening on the screen
                                                                                   #But it is good practise to convert an image so pygame can work more easily

text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 70)
text_surface= text_font.render("Intro To Animation", True, "black")

#Dog Name
dog_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
dog_text_surface= dog_text_font.render("Dogesh Bhai", True, "black")
dog_text_surface_x_pos= 765
#Cat Name
cat_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
cat_text_surface= dog_text_font.render("Billu Don", True, "black")
cat_text_surface_x_pos= 1085


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:   
            pygame.quit() 
            exit()

    screen.blit(background_surface, (0, 0)) #If we remove this line.. the dog and cat surfaces will leave a trail behind every frame
                                            #To fix this, we blit a screen every frame or iteration at the very start.. so that we don't see the trail
    screen.blit(text_surface, (80, 80))

    #Dog Name Movement
    dog_text_surface_x_pos-= 8 
    if dog_text_surface_x_pos< -150: dog_text_surface_x_pos= 850
    screen.blit(dog_text_surface, (dog_text_surface_x_pos, 310))
    #Dog Movement
    dog_x_pos-= 8 #This determines how much a object should move in every frame
    if dog_x_pos< -100: dog_x_pos= 900 #This resets the position when the object goes outside the screen, otherwise it will keep going infinitely
    screen.blit(dog_surface, (dog_x_pos, 325)) #Instead of a contant value in x position, we pass a variable which we can change
                                             #So, it appears to be moving
    
    #Cat Name Movement
    cat_text_surface_x_pos-= 8 
    if cat_text_surface_x_pos< -200: cat_text_surface_x_pos= 800
    screen.blit(cat_text_surface, (cat_text_surface_x_pos, 255))
    #Cat Movement
    cat_x_pos-= 8
    if cat_x_pos< -200: cat_x_pos= 800
    screen.blit(cat_surface, (cat_x_pos, 265))
    

    pygame.display.update() 

    clock.tick(45)