#In this we will make the enemy spawn logic more sophisticated. So it fills natural that the enemies are spawing naturally


from sys import exit
import pygame
from random import randint #To randomly place enemy 

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
score_font= pygame.font.SysFont("Arial", 40) 

instruct_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 50)
instruct_surface= instruct_font.render("Press Space to Play", True, "black")

dog_surface= pygame.image.load("graphics/dog-pixel.png") 
dog_surface= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha()
dog_surface_1= pygame.transform.smoothscale(dog_surface, (110, 100)).convert_alpha() #Creating a slightly bigger surface to make the dog look like walking

dog_jump= pygame.transform.smoothscale(dog_surface, (100, 110)) #Jumping image
dog_walk_list= [dog_surface, dog_surface_1] #To combine all the images to look like walking
dog_list_index= 0 #To iterate through the walking list

dog_surface_rect= dog_surface.get_rect(topleft = (80, 325)) 
dog_gravity= 0

cat_surface= pygame.image.load("graphics/cat-pixel.png")
cat_surface= pygame.transform.smoothscale(cat_surface, (240, 150)).convert_alpha() 
cat_surface_rect= cat_surface.get_rect(topleft = (1000, 272)) 

def display_score():
    
    current_time= int(pygame.time.get_ticks()/ 1000)- start_time
    score_surface= score_font.render(f"Score: {current_time}", True, (64, 64, 64))
    score_surface_rect= score_surface.get_rect(center= (380, 100))
    screen.blit(score_surface, score_surface_rect)    

start_time= 0

#Movement logic
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-= 8

            screen.blit(cat_surface, obstacle_rect)
            

        obstacle_list= [obstacle for obstacle in obstacle_list if obstacle.x> -200] #This simply delete the enemies from the list after the went out
                                                                                    #from the screen. As we don't want the list get infinitely larger 
                                                                                    #from time ad it can affect the game performances

        return obstacle_list
    
    else: return []

#Collision logic
def collision(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.inflate(-20, -20).colliderect(obstacles_rect.inflate(-200, -200)): return False
    
    return True

obstacle_rect_list= []
obstacle_timer= pygame.USEREVENT+ 1 #We hava added +1 because some event are reserved for pygame and we don't want it to conflict with the user events
                                    #So, we add +1 to it 
pygame.time.set_timer(obstacle_timer, 1800) #The event will trigger every 1.8 seconds

def dog_animation():
    global dog_surface, dog_list_index

    if dog_surface_rect.bottom< 425:
        dog_surface= dog_jump
    
    else:
        dog_list_index+= 0.1 #Want the dog to walk slowly not instantly 
        if dog_list_index>= len(dog_walk_list): dog_list_index= 0
        dog_surface= dog_walk_list[int(dog_list_index)] #We only want the integer value

while True:
    for event in pygame.event.get():
        
        if game_active:
            if event.type== pygame.QUIT:   
                pygame.quit() 
                exit()

            if event.type== pygame.KEYDOWN:  
                if event.key== pygame.K_SPACE:
                    if dog_surface_rect.bottom== 425: 
                        dog_gravity= -20 

            if event.type== obstacle_timer: #we will only run the event if the game is active and hence written inside game.active
                obstacle_rect_list.append(cat_surface.get_rect(topleft = (randint(850, 1000), 272)))

        else:
            if event.type== pygame.QUIT:
                pygame.quit() 
                exit()
            
            if event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
                game_active= True
                start_time= int(pygame.time.get_ticks()/ 1000)

            
    if game_active:
        screen.blit(background_surface, (0, 0)) 
        screen.blit(text_surface, (120, 20))
        display_score() 


        dog_gravity+= 1
        dog_surface_rect.y+= dog_gravity
        if dog_surface_rect.bottom> 425: dog_surface_rect.bottom= 425
        dog_animation()
        screen.blit(dog_surface, dog_surface_rect) 

        #Movement
        obstacle_rect_list= obstacle_movement(obstacle_rect_list)
        
        #Collision
        game_active= collision(dog_surface_rect, obstacle_rect_list)
    
    else:
        screen.fill("red")
        screen.blit(instruct_surface, (180, 400))
        screen.blit(text_surface, (160, 40))
        screen.blit(dog_surface, (200, 300)) 
        screen.blit(cat_surface, (300, 250))

        obstacle_rect_list.clear() #To restart the list so that it begins from starting
    
    pygame.display.update() 
    clock.tick(45)