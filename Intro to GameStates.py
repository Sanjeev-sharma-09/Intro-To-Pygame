#In this we will implement the game over state means when the dog touches the cat, the game will be over

#Also, i am making my code more clean so there will be changes in the code from before

from sys import exit
import pygame

pygame.init()
game_active= False

screen= pygame.display.set_mode((800, 500))
clock= pygame.time.Clock() 
pygame.display.set_caption("Ulta Billi, Kautval ko Mare") 

background_surface= pygame.image.load("graphics/background.jpg")
background_surface= pygame.transform.smoothscale(background_surface, (800, 500))
floor_rect= pygame.Rect(0, 405, 800, 95)

text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 70)
text_surface= text_font.render("Intro To Pygame", True, "black")
score_font= pygame.font.SysFont("Arial", 40) #Creating a different font for score

#Instructions font
instruct_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 50)
instruct_surface= instruct_font.render("Press Space to Play", True, "black")


dog_surface= pygame.image.load("graphics/dog-pixel.png") 
dog_surface= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha() 
dog_surface_rect= dog_surface.get_rect(topleft = (80, 325)) 

dog_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
dog_text_surface= dog_text_font.render("Dogesh Bhai", True, "black")
#Creating dog gravity to make it fall downwards when jumping
dog_gravity= 0

cat_surface= pygame.image.load("graphics/cat-pixel.png")
cat_surface= pygame.transform.smoothscale(cat_surface, (240, 150)).convert_alpha() 
cat_surface_rect= cat_surface.get_rect(topleft = (1000, 272)) 

cat_text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 30)
cat_text_surface= dog_text_font.render("Billu Don", True, "black")

#Score function
def display_score():
    
    current_time= int(pygame.time.get_ticks()/ 1000)- start_time #.get_ticks() give time in milliseconds and to convert it into sec we / by 1000
    #We subtracted start_time because we don't want the time to resume from the same time it end with
    score_surface= score_font.render(f"Score: {current_time}", True, (64, 64, 64))
    score_surface_rect= score_surface.get_rect(center= (380, 100))
    screen.blit(score_surface, score_surface_rect)
    
start_time= 0

while True:
    for event in pygame.event.get():
        
        if game_active: #We check below code only if the game is active
            if event.type== pygame.QUIT:   
                pygame.quit() 
                exit()

            if event.type== pygame.KEYDOWN:  
                if event.key== pygame.K_SPACE:
                    if dog_surface_rect.bottom== 425: #Jump logic
                        dog_gravity= -20 
        else:
            if event.type== pygame.QUIT: #To quit game when RAGED UP!!!!
                pygame.quit() 
                exit()
            
            if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE: #Now when pressing space again after collision we can restart the game
                                                                           #again and make the cat come again from outside the screen
                game_active= True
                cat_surface_rect.x= 950
                start_time= int(pygame.time.get_ticks()/ 1000)

            
    if game_active: #This if statements check if the game is active or not. Now instead of exiting the game, we can restart it when the objects
                    #collide with this single variable game_active
        screen.blit(background_surface, (0, 0)) 
        screen.blit(text_surface, (120, 20))
        display_score() #Calling the display_score function

        screen.blit(dog_text_surface, (dog_surface_rect.x- 30, dog_surface_rect.y- 20))
        screen.blit(dog_surface, dog_surface_rect) 
        
        screen.blit(cat_surface, cat_surface_rect)
        screen.blit(cat_text_surface, (cat_surface_rect.x+ 85, cat_surface_rect.y- 10))


        dog_gravity+= 1
        dog_surface_rect.y+= dog_gravity
        if dog_surface_rect.bottom> 425: dog_surface_rect.bottom= 425
        
        cat_surface_rect.x -= 8
        if cat_surface_rect.right < 0: cat_surface_rect.left = 800
        
        #Collision of Dog and Cat to make Game Over
        if dog_surface_rect.inflate(-20, -20).colliderect(cat_surface_rect.inflate(-200, -200)):
            game_active= False
            # pygame.quit() 
            # exit()
        #Here we will see that the game gets over even when they are visually not colliding. This is because of transforming the images 
        #We can some transparent area which comes in the rectangle and hence when it collides the game gets over, but visually it looks like 
        #they haven't collide yet. To fix this, we can use mask to mask it around the images.. We will do this in the end product file.
        #Instead we will use .inflate(x, y) method to shrink the collision area .. It can be very usefull in complex games
    
    else:
        screen.fill("red") #If they collides the screen will be filled with red
        screen.blit(instruct_surface, (180, 400))
        
        screen.blit(text_surface, (160, 40))
        screen.blit(dog_surface, (200, 300)) 
        screen.blit(cat_surface, (300, 250))
    
    pygame.display.update() 
    clock.tick(45)