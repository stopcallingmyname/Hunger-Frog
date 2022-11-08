import pygame, sys, random, time
from math import sin, cos
from random import randrange, randint, choice

#camera variables
SCROLL_THRESH = 500
scroll = 0

#jump sound
pygame.mixer.init()
jump_fx = pygame.mixer.Sound('SFX/jump.wav')
jump_fx.set_volume(0.5)
#selection sound
click_fx = pygame.mixer.Sound('SFX/click.wav')
click_fx.set_volume(0.5)

def setScroll(value):
    global scroll
    scroll = value

class World():
    def __init__(self, x, y):
        self.Reset(x, y)

    def Reset(self, x, y):
        self.img = pygame.image.load('Sprites/ground.png')
        self.im_rect = self.img.get_rect()
        self.im_rect.x = x
        self.im_rect.y = y
        self.img_3d = pygame.image.load('Sprites/ground_3d.png')

    def Draw(self, Window):
        self.im_rect.x += scroll

        Window.blit(self.img_3d, ((self.im_rect.x + 18), self.im_rect.y))
        Window.blit(self.img, self.im_rect)
        ###DRAWING ESP###
        #pygame.draw.rect(Window, (255, 255, 255), self.im_rect, 2)



class Water():
    def __init__(self, x, y):
        self.Reset(x, y)

    def Reset(self, x, y):
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(5):
            img = pygame.image.load(f'Sprites/water/{i}.png')
            self.animation_list.append(img)
		
        self.image = self.animation_list[self.frame_index]
        #self.img_3d = pygame.image.load(f'Sprites/spriteV2_3d.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_animation(self):
		#update animation
        ANIMATION_COOLDOWN = 150
		#update image depending on current frame
        self.image = self.animation_list[self.frame_index]
		#check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
		#reset animation
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def Draw(self, x, y, Window):
        self.update_animation()
        #self.rect.x += scroll

        Window.blit(self.image, self.rect)
        ###DRAWING ESP###
        #pygame.draw.rect(Window, (255, 255, 255), self.im_rect, 2)

class Decorations():
    def __init__(self, x, y):
        self.Reset(x, y)

    def Reset(self, x, y):
        self.image = pygame.image.load('Sprites/bush.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Draw(self, Window):
        self.rect.x += scroll
        Window.blit(self.image, self.rect)
        ###DRAWING ESP###
        #pygame.draw.rect(Window, (255, 255, 255), self.rect, 2)

class Background():
    def __init__(self, x, y):
        self.Reset(x, y)

    def Reset(self, x, y):
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(3):
            img = pygame.image.load(f'Sprites/Background anims/{i}.png')
            self.animation_list.append(img)
		
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update_animation(self):
		#update animation
        ANIMATION_COOLDOWN = 150
		#update image depending on current frame
        self.image = self.animation_list[self.frame_index]
		#check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
		#reset animation
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def Draw(self, Window):
        self.update_animation()
        self.rect.x += scroll

        Window.blit(self.image, self.rect)
        ###DRAWING ESP###
        #pygame.draw.rect(Window, (255, 255, 255), self.im_rect, 2)

class Player():
    def __init__(self, x, y):
        self.Reset(x, y)

    def Reset(self, x, y):
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(10):
            img = pygame.image.load(f'Sprites/froggy anims/Idle/{i}.png')
            #img = pygame.image.load(f'Sprites/pixel-sf/{i}.png') # for shadow fiend skin and set up range(6)
            self.animation_list.append(img)
		
        self.image = self.animation_list[self.frame_index]
        self.img_3d = pygame.image.load(f'Sprites/spriteV2_3d.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.Direction = 1
        self.Flip = False
        self.Speed = 8
        self.vel_y = 0
        self.jumped = False
        self.in_air = True
        self.tongue_active = False

        #Tongue variables
        self.start = [self.rect.x, self.rect.y]
        self.step = [0.0, 0.0]
        self.end = [self.rect.x, self.rect.y]

    def update_animation(self):
		#update animation
        ANIMATION_COOLDOWN = 200
		#update image depending on current frame
        self.image = self.animation_list[self.frame_index]
		#check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
		#reset animation
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def Draw(self, Window):
        #Draw Player   
        self.update_tongue()
        Window.blit(self.img_3d, ((self.rect.x + 11), self.rect.y))
        #Window.blit(pygame.transform.flip(self.image, self.Flip, False), self.rect)
        Window.blit(self.image, self.rect) #for shadow fiend skin
        if self.alive == True:
            Tongue = pygame.draw.line(Window, (255, 169, 255), self.start, self.end, 12)

            if self.tongue_active == True:
                tongue_end = pygame.image.load('Sprites/tongue_end.png')
                tongue_end_copy = pygame.image.load('Sprites/tongue_end.png')
                Window.blit(tongue_end, (self.end[0] - int(tongue_end_copy.get_width() / 2), self.end[1] - int(tongue_end_copy.get_height() / 2)))

    def update_tongue(self):
        #Get mouse pos
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #Tongue line
        if pygame.mouse.get_pressed() == (1, 0, 0):
            self.tongue_active = True
            self.start[0] = self.rect.x + 52
            self.start[1] = self.rect.y + 54
            self.end[0] = self.start[0] + self.step[0] * (mouse_x - self.start[0])
            self.end[1] = self.start[1] + self.step[1] * (mouse_y - self.start[1])
            self.step[0] += 0.1
            self.step[1] += 0.1
            self.step[0] = min(1.0, self.step[0])
            self.step[1] = min(1.0, self.step[1])
        else:
            self.tongue_active = False
            self.step[0] = 0
            self.step[1] = 0
            self.start[0] = self.rect.x + 52
            self.start[1] = self.rect.y + 54
            self.end[0] = self.rect.x + 52
            self.end[1] = self.rect.y + 54

    def Update(self):
        
        self.update_animation()
        scroll = 0
        #Delta x and Delta y
        dx = 0
        dy = 0

        #Get key pressed
        Key = pygame.key.get_pressed()

        

        #Player movement
        if Key[pygame.K_SPACE] and self.jumped == False and player.rect.bottom >= 650 and self.in_air == False:
            self.vel_y = -12
            self.jumped = True
            jump_fx.play()
        if Key[pygame.K_SPACE] == False:
            self.jumped = False

        if Key[pygame.K_a]:
            dx -= self.Speed
            self.Flip = True
            self.Direction = -1
        if Key[pygame.K_d]:
            dx += self.Speed
            self.Flip = False
            self.Direction = 1

        #add gravity
        self.vel_y += 1
        if self.vel_y > 40:
            self.vel_y = 40
        dy += self.vel_y

        #Check for collision
        self.in_air =True
        if world.im_rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
            #Check if below the ground i.e. jumping
            if self.vel_y < 0:
                dy = world.im_rect.bottom - self.rect.top
                self.vel_y = 0
            if self.vel_y >= 0:
                dy = world.im_rect.top - self.rect.bottom
                self.vel_y = 0
                self.in_air = False
                

        if self.rect.bottom > 720:
            self.rect.bottom = 720
            dy = 0
            player.rect.y = 680
            self.alive = False

        ###DRAWING ESP###
        #pygame.draw.rect(Window, (255, 255, 255), self.rect, 2)
        #pygame.draw.rect(Window, (255, 255, 255), Tongue, 2)

        #Update player coordinates
        self.rect.x += dx
        self.rect.y += dy
        
        #update scroll based on player pos
        if self.rect.right > 1080 - SCROLL_THRESH or self.rect.left < SCROLL_THRESH:
            self.rect.x -= dx
            scroll = -dx
        return scroll

class Enemy():
	def __init__(self, x, y, speed):
		self.Reset(x, y, speed)
		
	def Reset(self, x, y, speed):
		self.animation_list = []
		self.frame_index = 0
		self.update_time = pygame.time.get_ticks()
		for i in range(5):
		    img = pygame.image.load(f'Sprites/mosquite animations/flying/{i}.png')
		    self.animation_list.append(img)
        
		self.image = self.animation_list[self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.Speed = speed
		self.Direction = random.choice([-1, 1])
		self.Flip = False
		self.move_counter = 0
		self.enemy_alive = True
		self.on_the_ground = False
		self.bonus = False

	def move(self, moving_left, moving_right):
		dx = 0
		dy = 0

		if moving_left:
		    dx = -self.Speed
		    self.Flip = True
		    self.Direction = -1
		if moving_right:
		    dx = self.Speed
		    self.Flip = False
		    self.Direction = 1

		#udpate rectangle position
		self.rect.x += dx
		self.rect.y += dy

	def ai(self):
		
		if self.enemy_alive:
			if self.Direction == 1:
				ai_moving_right = True
			else:
				ai_moving_right = False
			ai_moving_left = not ai_moving_right
			self.move(ai_moving_left, ai_moving_right)
			self.move_counter += 1

			if self.move_counter > randint(100, 200):
				self.Direction *= -1
				self.move_counter *= -1

		self.rect.x += scroll

	def update_animation(self):
		#update animation
		ANIMATION_COOLDOWN = 60
		#update image depending on current frame
		self.image = self.animation_list[self.frame_index]
		#check if enough time has passed since last update
		if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		#reset animation
		if self.frame_index >= len(self.animation_list):
			self.frame_index = 0

	def Update(self, Window):
		self.update_animation()
		#Draw enemy
		self.enemy_box = Window.blit(pygame.transform.flip(self.image, self.Flip, False), self.rect)

	def Collider(self, enemy_box, end, rect):
		if enemy_box.collidepoint(end):
			self.enemy_alive = False

class Button():
    def __init__(self, char_type, x, y):
        self.char_type = char_type
        self.image = pygame.image.load(f'Sprites/Buttons/{self.char_type}/{self.char_type}_static.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def Draw(self, Window):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = pygame.image.load(f'Sprites/Buttons/{self.char_type}/{self.char_type}_clicked.png')

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.image = pygame.image.load(f'Sprites/Buttons/{self.char_type}/{self.char_type}_clicked.png')
                action = True
                time.sleep(0.2)
                self.clicked = True
                click_fx.play()

            if  pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        else:
            self.image = pygame.image.load(f'Sprites/Buttons/{self.char_type}/{self.char_type}_static.png')

        Window.blit(self.image, self.rect)
        return action
   

#Objects
background = Background(366, 138)
world = World(145, 656)
water = Water(-150, 682)
player = Player(487, 562)
#player = Player(487, 474) #for shadow fiend skin
enemy = Enemy(randrange(792), randrange(360), 3)
decoration = Decorations(230, 581)
restart = Button('Restart', 415, 245)
info = Button('Info', 415, 306)
menu = Button('Menu', 415, 367)
play = Button('Play', 415, 182)
info_play = Button('Play', 415, 530)
exit = Button('Exit', 415, 430)
