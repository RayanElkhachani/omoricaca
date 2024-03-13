import pygame
from sys import exit
from random import randint
def displayScore():
    current_time=pygame.time.get_ticks()-start_time
    score_surf = test_font.render((f'Score:{round(current_time/1000)}'),False,(64,64,64))
    score_rect = score_surf.get_rect(center = (500,50))
    screen.blit(score_surf,score_rect)

def displayGameover():
    game_over_surf = game_over_font.render("Game over",False,"pink")
    game_over_rect = game_over_surf.get_rect(center = (500,350))
    screen.blit(game_over_surf,game_over_rect)
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.y+=5
            screen.blit(caca_surf,obstacle_rect)
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.y>0]
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


pygame.init()
pygame.display.set_caption("omoriCACA")
screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
game_active = True
start_time=0
music= pygame.mixer.music.load("audio/omoricaca.mp3")


background_surf = pygame.image.load("graphics/background.png").convert()


caca_surf = pygame.image.load("graphics/caca1.png").convert_alpha()
caca_surf = pygame.transform.scale(caca_surf, (100,90))
caca_rect = caca_surf.get_rect()

obstacle_rect_list=[]

player_surf = pygame.image.load("graphics/omori.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (150,700))
player_gravity = 0

test_font=pygame.font.Font("font/Pixeltype.ttf",50)
game_over_font=pygame.font.Font("font/Pixeltype.ttf",70)
pygame.mixer.music.play(True,0,0)
obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,1500)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom ==700:
                        player_gravity =-20
                if event.key == pygame.K_d:
                        player_rect.x +=30
                if event.key == pygame.K_q:
                        player_rect.x -=30

        else:
            if event.type ==pygame.KEYDOWN and event.key == pygame.K_SPACE:
                caca_rect.bottom=0
                game_active = True
                start_time=pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(caca_surf.get_rect(bottomright= (randint(500,1100),300)))

    if game_active:
        screen.blit(background_surf,(0,0))
        displayScore()


        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 700:
            player_rect.bottom =700
        if player_rect.right < 0:
            player_rect.right = 1000
        if player_rect.left >=1000:
            player_rect.left = 0
        screen.blit(player_surf, player_rect)

        obstacle_rect_list= obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill("black")
        displayGameover()
        obstacle_rect_list.clear()
        player_gravity =0
    pygame.display.update()
    clock.tick(60)

