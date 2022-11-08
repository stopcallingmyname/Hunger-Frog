import sys
import pygame
import math
import random
from Game import *
from Debug import *

pygame.init()

#Window
Width = 1080
Height = 720
WINDOW_SIZE = (Width, Height)
Half_Width = Width / 2
Half_Height = Height / 2
FPS = 140
Window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Hungry Frog")
pygame.display.set_icon(pygame.image.load('Sprites/Icon.png'))

#define game variables
Enemies = [enemy]
Ocean = [water]
enemiesAmount = 4
f = open('TopScore.txt', 'r+')
score = 0
top_score = int(f.read())
eat_amount = 6
GAME_OVER = True
Description = False

#Music
pygame.mixer.music.load('SFX/song.ogg')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#eat sound
eat_fx = pygame.mixer.Sound('SFX/am.wav')
eat_fx.set_volume(0.5)

#enemy spawn sound
spawn_fx = pygame.mixer.Sound('SFX/spawn.mp3')
spawn_fx.set_volume(0.2)

#define enemy action variables
moving_left = False
moving_right = False

def DrawWindow():
    #Sprites
    g_Skeet = pygame.image.load('Sprites/skeet.png')

    #Render
    Window.blit(g_Skeet, (0, 0))
    foodRender(18, 14, Window)
    foodAmountRender(91, 46, eat_amount, Window)
    ScoreRender(18, 105, score, Window);
    TopScoreRender(18, 130, top_score, Window);

start = pygame.time.get_ticks()
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f.seek(0)
            f.write(str(top_score))
            f.close()
            run = False
            pygame.quit()
            sys.exit()

    pygame.time.Clock().tick(FPS)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    Keys = pygame.key.get_pressed()

    if GAME_OVER == True:
        Window.fill((48, 48, 48))
        DrawButtonsBackground(333, 119, 'MenuBack', Window)
        if play.Draw(Window):
            GAME_OVER = False
            Description = False

        if info.Draw(Window):
            Description = True
        if exit.Draw(Window):
            run = False
        if Description == True:
            Window.fill((48, 48, 48))
            DrawButtonsBackground(93, 47, 'InfoBack', Window)
            InfoRender(Window)
            if info_play.Draw(Window):
                GAME_OVER = False
                Description = False

    else:
        #Without background, do not forget to change FPS back to 90
        #surf = pygame.Surface((Width, Height))
        #surf.fill((48, 48, 48))
        #Window.blit(surf, (0, 0))

        Window.fill((48, 48, 48))
        im = pygame.image.load('Sprites/clouds.jpg')
        r = im.get_rect()
        Window.blit(im, (0, 0))

        background.Draw(Window)
        world.Draw(Window)
        player.Draw(Window)

        for w in Ocean:
            w.Draw(water.rect.x, 682, Window)
            
            if len(Ocean) <= 8:
                    water.rect.x += 144
                    water = Water(water.rect.x, 682)
                    Ocean.append(water)

        if player.alive:
            now = pygame.time.get_ticks()

            scroll = player.Update()
            setScroll(scroll)

            #Logic
            for i in Enemies:

                i.ai()
                i.Update(Window)
                i.move(moving_left, moving_right)
                i.Collider(i.enemy_box, player.end, world.im_rect)

                if i.enemy_alive == False:
                    i.rect.y += 5
                    if i.enemy_box.colliderect(world.im_rect): 
                        i.rect.bottom = world.im_rect.top
                        i.rect.y = i.rect.bottom - 65
                        i.on_the_ground = True
      
                    if i.enemy_box.colliderect(player.rect): 
                        i.rect.bottom = player.rect.top
                        i.rect.y = i.rect.bottom
                        i.bonus = True
                        i.on_the_ground = True
                        eat_fx.play()

                    if i.rect.bottom > 720:
                        i.rect.y = 720 - 65
                        i.on_the_ground = True

                if i.on_the_ground == True:
                    Enemies.remove(i)
                    if i.bonus == True:
                        score += 10
                        eat_amount += 1
                    else:
                        score += 1

                if len(Enemies) <= enemiesAmount:
                    enemy = Enemy(randrange(792), randrange(360), 3)
                    Enemies.append(enemy) 
                    spawn_fx.play()

            if top_score < score:
                top_score = score

            if now - start > 3000:
                start = now
                eat_amount -= 1

            if eat_amount > 6:
                eat_amount = 6

            if eat_amount <= 0:
                eat_amount = 0
                player.alive = False
            
        else:
            DrawButtonsBackground(333, 182, 'RestartBack', Window)
            pygame.mixer.music.stop()
            scroll = 0
            setScroll(scroll)
            if restart.Draw(Window):
                pygame.mixer.music.play(-1)
                start = now
                scroll = 0
                setScroll(scroll)
                eat_amount = 6
                score = 0

                background.Reset(366, 138)
                world.Reset(145, 656)
                water.Reset(0, 682)
                player.Reset(487, 562)
                #player.Reset(487, 474) #for shadow fiend skin
                for e in Enemies:
                    e.Reset(randrange(792), randrange(360), 3)
                decoration.Reset(230, 581)
                player.alive = True

            if menu.Draw(Window):
                pygame.mixer.music.play(-1)
                GAME_OVER = True

        decoration.Draw(Window)
        DrawWindow()

    pygame.display.update()
