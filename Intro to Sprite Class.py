#Now we have made our code without any functions or class which is terrible as the longer the game goes, it will be harder to locate and fix bugs 
#To fix this we have a class called Sprite class- A class that contains a surface and a rectangle; and it can be drawn and updated very easily

#So in this we will create a Sprite class for dog and obstacles(cat) 
#Future me- I just found out that my code is terrible and to implement sprite class for both of them, it will require a lot of removing and adding
#So, i am just gonna only make the sprite class for dog and let you all explore on how to implement it further for the cat

#I will remove all the unnesasary part which we don't need after the sprite class 


from sys import exit
import pygame
from random import randint

class Dog(pygame.sprite.Sprite): #To declare a sprite
    def __init__(self):
        super().__init__()

        dog_surface= pygame.image.load("graphics/dog-pixel.png") 
        dog_surface_0= pygame.transform.smoothscale(dog_surface, (100, 100)).convert_alpha()
        dog_surface_1= pygame.transform.smoothscale(dog_surface, (110, 100)).convert_alpha() 

        self.dog_jump= pygame.transform.smoothscale(dog_surface, (100, 110)).convert_alpha() #We only want the jump, list, and index to access outside the __init__()
        self.dog_walk_list= [dog_surface_0, dog_surface_1] 
        self.dog_list_index= 0 

        self.image= self.dog_walk_list[self.dog_list_index] #self.image and self.rect and 100% necesarily needed to include.. We can't have a sprite class
        self.rect= self.image.get_rect(topleft = (80, 325)) #without these two
        self.dog_gravity= 0

    def player_input(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom>= 425:
            self.dog_gravity= -20

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

screen= pygame.display.set_mode((800, 500))
clock= pygame.time.Clock() 
pygame.display.set_caption("Ulta Billi, Kautval ko Mare") 

#Creating a GroupSingle for dog
dog= pygame.sprite.GroupSingle() 
dog.add(Dog()) #This is simply done to access the class Dog more easily ..

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

def collision(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.inflate(-20, -20).colliderect(obstacles_rect.inflate(-200, -200)): return False
    
    return True 

    #We could write a more simpler code if we created the Cat sprite. The code is-
    # if pygame.sprite.spritecollide(sprite= dog.sprite, group= obstacles_group, tokill= False): This return and empty list or list of objects collided with the sprite
    #   obstacle_group.empty() 
    #   return False
    # else: return True       

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
        
        # game_active= collision(dog_surface_rect, obstacle_rect_list) 
        #Instead of above code we could have,
        # game_active= collision()
    
    else:
        screen.fill("red")
        screen.blit(instruct_surface, (180, 400))
        screen.blit(text_surface, (160, 40)) 
        screen.blit(cat_surface, (300, 250))

        obstacle_rect_list.clear() 
    
    pygame.display.update() 
    clock.tick(45)