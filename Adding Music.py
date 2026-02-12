#We will add music in this 

from sys import exit
import pygame
from random import randint

class Dog(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()

        dog_surface= pygame.image.load("graphics/dog-pixel.png") 
        dog_surface_0= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha()
        dog_surface_1= pygame.transform.smoothscale(dog_surface, (110, 100)).convert_alpha() 

        self.dog_jump= pygame.transform.smoothscale(dog_surface, (100, 110)).convert_alpha() 
        self.dog_walk_list= [dog_surface_0, dog_surface_1] 
        self.dog_list_index= 0 

        self.image= self.dog_walk_list[self.dog_list_index] 
        self.rect= self.image.get_rect(topleft = (80, 325)) 
        self.dog_gravity= 0

        self.jump_sound= pygame.mixer.Sound("music/Mario Jump.mp3") #This here is used to import sounds
        self.jump_sound.set_volume(0.01) #0-1, where 0- No sound and 1- Full volume

    def player_input(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom>= 425:
            self.dog_gravity= -20
            self.jump_sound.play() #To play the sound

    def apply_gravity(self):
        self.dog_gravity+= 1
        self.rect.y+= self.dog_gravity
        if self.rect.bottom> 425: self.rect.bottom= 425

    def animation(self):
        if self.rect.bottom< 425:
            self.image= self.dog_jump
        
        else:
            self.dog_list_index+= 0.08 
            if self.dog_list_index>= len(self.dog_walk_list): self.dog_list_index= 0
            self.image= self.dog_walk_list[int(self.dog_list_index)] 
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()

pygame.init()
game_active= False

bg_sound= pygame.mixer.Sound("music/Background Music.mp3")
bg_sound.set_volume(0.1)
bg_sound.play() # .play(loops= 2) this will loop the sounds 2 times. If we add -1 it will loop forever

screen= pygame.display.set_mode((800, 500))
clock= pygame.time.Clock() 
pygame.display.set_caption("Ulta Billi, Kautval ko Mare") 


dog= pygame.sprite.GroupSingle() 
dog.add(Dog()) 

background_surface= pygame.image.load("graphics/background.jpg")
background_surface= pygame.transform.smoothscale(background_surface, (800, 500))
floor_rect= pygame.Rect(0, 405, 800, 95)

text_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 70)
text_surface= text_font.render("Intro To Pygame", True, "black")
score_font= pygame.font.SysFont("Arial", 40) 

instruct_font= pygame.font.Font("fonts/SanjeevsFont-Regular.ttf", 50)
instruct_surface= instruct_font.render("Press Space to Play", True, "black")


cat_surface= pygame.image.load("graphics/cat-pixel.png")
cat_surface= pygame.transform.smoothscale(cat_surface, (240, 150)).convert_alpha() 
cat_surface_rect= cat_surface.get_rect(topleft = (1000, 272)) 

def display_score():
    
    current_time= int(pygame.time.get_ticks()/ 1000)- start_time
    score_surface= score_font.render(f"Score: {current_time}", True, (64, 64, 64))
    score_surface_rect= score_surface.get_rect(center= (380, 100))
    screen.blit(score_surface, score_surface_rect)    

start_time= 0

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-= 8

            screen.blit(cat_surface, obstacle_rect)
            

        obstacle_list= [obstacle for obstacle in obstacle_list if obstacle.x> -200]

        return obstacle_list
    
    else: return []
     

obstacle_rect_list= []
obstacle_timer= pygame.USEREVENT+ 1
pygame.time.set_timer(obstacle_timer, 1800) 

while True:
    for event in pygame.event.get():
        
        if game_active:
            if event.type== pygame.QUIT:   
                pygame.quit() 
                exit()

            if event.type== obstacle_timer:
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

        dog.draw(screen) 
        dog.update()

        obstacle_rect_list= obstacle_movement(obstacle_rect_list)
    
    else:
        screen.fill("red")
        screen.blit(instruct_surface, (180, 400))
        screen.blit(text_surface, (160, 40)) 
        screen.blit(cat_surface, (300, 250))

        obstacle_rect_list.clear() 
    
    pygame.display.update() 
    clock.tick(45)
