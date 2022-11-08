import sys
import pygame
pygame.init()

#define score variable
score_value = 0
font = pygame.font.Font('Fonts/Verdana/Verdana.ttf', 20)
font_bold = pygame.font.Font('Fonts/Verdana/verdanab.ttf', 20)
#info fonts
question_font = pygame.font.Font('Fonts/Verdana/verdanab.ttf', 32)
description_font = pygame.font.Font('Fonts/Verdana/Verdana.ttf', 22)

#Misc
def draw_text(text, font, color, surface, x, y, Window):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = x, y
    surface.blit(textobj, textrect)

#def TextRender(text, value, x, y, Window):
#    str(text) 
#    Render = font.render(text + str(value), True, (163, 163, 163))
#    Window.blit(Render, (x, y))

def TextRender(text, x, y, bold, Window):
    str(text)
    if bold == True:
        Render = font_bold.render(text, True, (163, 163, 163))
        Window.blit(Render, (x, y))
    else:
        Render = font.render(text, True, (163, 163, 163))
        Window.blit(Render, (x, y))

def CoordRender(text, value_1, value_2, x, y, Window):
    str(text)
    Render = font.render(text + str(value_1) + ", " + str(value_2), True, (163, 163, 163))
    Window.blit(Render, (x, y))

def foodRender(x, y, Window):
    food_img = pygame.image.load('Sprites/eating.png')
    food_rect = food_img.get_rect()
    food_rect.x = x
    food_rect.y = y
    Window.blit(food_img, food_rect)   

def foodAmountRender(x, y, amount, Window):
    score = font_bold.render(str(amount), True, (255, 204, 102))
    Window.blit(score, (x, y))

def ScoreRender(x, y, score_value, Window):
    score = font.render("SCORE: " + str(score_value), True, (41, 41, 41))
    Window.blit(score, (x, y))

def TopScoreRender(x, y, score_value, Window):
    score = font.render("TOP SCORE: " + str(score_value), True, (41, 41, 41))
    Window.blit(score, (x, y))

def blit_text(surface, text, pos, color=(27, 27, 27)):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = description_font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0] 
        y += word_height

def InfoRender(Window):
    description = "     Логика игры довольно простая. Необходимо поддерживать\n" \
                  "сытость Фрогги. Для этого достаточно попасть в комарика\n" \
                  "языком и во время его падения - словить, получив при этом\n" \
                  "одну единицу голода и приятный бонус в 10 дополнительных\n" \
                  "очков. Напомню, если комарик упадет на землю, вы получите\n" \
                  "всего-лишь одно очко и голод при этом не увеличится.\n\n" \
                  "    Насчет сытости. Каждые 3 секунды вы теряете 1 единицу\n" \
                  "голода. Постарайтесь прокормить вечно голодного Фрогги\n" \
                  "как можно дольше. Также стоит остерегаться воды, ведь\n" \
                  "попав в бездонный океан, вы отправитесь на корм рыбам.\n" \
                  "                                           Удачи :)"
    
    question = question_font.render('Как играть?', True, (27, 27, 27))

    blit_text(Window, description, (200, 151))
    Window.blit(question, (433, 91))

def DrawButtonsBackground(x, y, char_type, Window):
    if char_type == 'RestartBack':
        image = pygame.image.load(f'Sprites/Buttons/{char_type}/{char_type}.png')
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        Window.blit(image, rect)
    if char_type == 'MenuBack':
        background_image = pygame.image.load('Sprites/MenuBackGround.jpg')
        background_rect = background_image.get_rect()
        background_rect.x = 0
        background_rect.y = 0

        image = pygame.image.load(f'Sprites/Buttons/{char_type}/{char_type}.png')
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        Window.blit(background_image, background_rect)
        Window.blit(background_image, background_rect)
        Window.blit(image, rect)
    if char_type == 'InfoBack':
        background_image = pygame.image.load('Sprites/MenuBackGround.jpg')
        background_rect = background_image.get_rect()
        background_rect.x = 0
        background_rect.y = 0

        image = pygame.image.load(f'Sprites/Buttons/{char_type}/{char_type}.png')
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        Window.blit(background_image, background_rect)
        Window.blit(background_image, background_rect)
        Window.blit(image, rect)
