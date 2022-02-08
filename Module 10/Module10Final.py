# Jordan Eldridge
# 18 January 2018
# Module 10 Final Assignment

# Font Used: https://www.dafont.com/funny-cute.font?text=Start&psize=s

import pygame, random, math
pygame.init()

# Colours - - - - -

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREEN = (159, 249, 62)
GREEN = (66, 198, 45)
SELECT_GREEN = (56, 216, 61)
BLUE = (63, 72, 204)
RED = (168, 56, 52)
GREY = (193, 193, 193)
SPD_GREEN = (58, 165, 46)
SPD_RED = (211, 19, 25)
YELLOW = (247, 227, 12)

BG1 = (242, 91, 99)
BG2 = (0, 162, 232)
BG3 = (255, 127, 39)
BG4 = (163, 73, 164)
BG5 = (255, 174, 201)

START_RED = (226, 18, 29)

# Fonts - - - - - 

font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 22)

# Window - - - - -

width = 800
height = 800
size = (width, height)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Picnic Panic!")

clock = pygame.time.Clock()
done = False

# Sounds & Images - - - - - 

# Title Screen

background = pygame.image.load("Background1.png").convert()
bg_choice = ["Background1.png", "Background2.png", "Background3.png", "Background4.png", "Background5.png"]
logo = pygame.image.load("Logo.png").convert()
logo = pygame.transform.scale(logo, (600,100))
logo.set_colorkey(WHITE)
start = pygame.image.load("Start.png").convert()
start.set_colorkey(WHITE)
start_highlight = pygame.image.load("StartHighlight.png").convert()
start_highlight.set_colorkey(WHITE)
instructions = pygame.image.load("Instructions.png").convert()
instructions.set_colorkey(WHITE)
options = pygame.image.load("Options.png").convert()
options.set_colorkey(WHITE)
bg_text = pygame.image.load("BG_Text.png").convert()
bg_text.set_colorkey(WHITE)
volume_text = pygame.image.load("Volume.png").convert()
volume_text.set_colorkey(WHITE)
vol_quiet = pygame.image.load("Vol_Quiet.png").convert()
vol_quiet.set_colorkey(WHITE)
vol_med = pygame.image.load("Vol_Med.png").convert()
vol_med.set_colorkey(WHITE)
vol_loud = pygame.image.load("Vol_Loud.png").convert()
vol_loud.set_colorkey(WHITE)
vol_mute = pygame.image.load("Vol_Mute.png").convert()
vol_mute.set_colorkey(WHITE)
life_text = pygame.image.load("Lives.png").convert()
life_text.set_colorkey(WHITE)
one_life = pygame.image.load("1.png").convert()
one_life.set_colorkey(WHITE)
three_life = pygame.image.load("3.png").convert()
three_life.set_colorkey(WHITE)
five_life = pygame.image.load("5.png").convert()
five_life.set_colorkey(WHITE)
speed_text = pygame.image.load("Speed.png").convert()
speed_text.set_colorkey(WHITE)

# Game

ant = pygame.image.load("Ant.png").convert()
ant = pygame.transform.scale(ant, (20,25))
ant.set_colorkey(WHITE)
cherry = pygame.image.load("Cherry.png").convert()
cherry = pygame.transform.scale(cherry, (30,35))
cherry.set_colorkey(WHITE)
cookie = pygame.image.load("Cookie.png").convert()
cookie = pygame.transform.scale(cookie, (30,35))
cookie.set_colorkey(WHITE)
orange = pygame.image.load("Orange.png").convert()
orange = pygame.transform.scale(orange, (30,35))
orange.set_colorkey(WHITE)
choco = pygame.image.load("Chocolate.png").convert()
choco = pygame.transform.scale(choco, (30,35))
choco.set_colorkey(WHITE)
coffee = pygame.image.load("Coffee.png").convert()
coffee = pygame.transform.scale(coffee, (30,35))
coffee.set_colorkey(WHITE)
cheese = pygame.image.load("Cheese.png").convert()
cheese = pygame.transform.scale(cheese, (30,35))
cheese.set_colorkey(WHITE)

red_ant = pygame.image.load("RedAnt.png").convert()
red_ant = pygame.transform.scale(red_ant, (20,25))
red_ant.set_colorkey(WHITE)

spray = pygame.image.load("BugSpray.png").convert()
spray = pygame.transform.scale(spray, (30,35))
spray.set_colorkey(WHITE)

# Game Over

game_over_text = pygame.image.load("GameOver.png").convert()
game_over_text.set_colorkey(WHITE)
restart = pygame.image.load("Restart.png").convert()
restart.set_colorkey(WHITE)
restart_highlight = pygame.image.load("RestartHighlight.png").convert()
restart_highlight.set_colorkey(WHITE)
high_score_title = pygame.image.load("HighScore.png").convert()
high_score_title.set_colorkey(WHITE)
new_hs = pygame.image.load("NewHighScore.png").convert()
new_hs.set_colorkey(WHITE)
your_score_title = pygame.image.load("Score.png").convert()
your_score_title.set_colorkey(WHITE)

# Sounds

click_option = pygame.mixer.Sound("ClickOption.ogg")
volume = [0.2, 0.6, 1, 0]
click_option.set_volume(volume[1])

pygame.mixer.music.load("Marimba_Boy.ogg") # Background Music
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume[1])

bite = pygame.mixer.Sound("Bite.ogg")
bite.set_volume(volume[1])

# Variables - - - - -

bg_colour = [BG1, BG2, BG3, BG4, BG5]
bg_x = [130, 185, 240, 295, 350]
bg_y = 460
bg_distance = [0] * 5
bg = "Background1.png"

vol_x = [130, 185, 240, 295]
vol_y = 550
vol_distance = [0] * 4
vol_level = 0.6

life_x = [470, 525, 580]
life_y = 460
life_distance = [0] * 3
life_choice = [1, 3, 5]

spd_x = [470, 525, 580]
spd_y = 550
spd_distance = [0] * 3
spd_choice = [2, 4, 6]
spd_colour = [SPD_RED, YELLOW, SPD_GREEN] # Option bubble colours

ant_angle = [0, 90, 180, 270] # The angles the ant can turn
for angle in range(0,4) :
    ant_angle[angle] = pygame.transform.rotate(ant, ant_angle[angle])

red_angle = [90, 270]
for r_angle in range(0,2) :
    red_angle[r_angle] = pygame.transform.rotate(red_ant, red_angle[r_angle])

red2_angle = [90, 270]
for r2_angle in range(0,2) :
    red2_angle[r2_angle] = pygame.transform.rotate(red_ant, red2_angle[r2_angle])

ant_x, ant_y = 400, 400 # Default ant position
y_speed = 2 # Ant speeds
x_speed = 2
go_x_speed = 2
go_y_speed = 2

red_x, red_y = 200, 200 # Red ant default position
red_x_speed = 3 # Red Ant speeds
red_y_speed = 0
red_x2, red_y2 = 600, 600 # Second Red Ant
red_x2_speed = 3
red_y2_speed = 0

cherry_x, cherry_y = random.randrange(70,700), random.randrange(70,700) # Random location for the cherry (first food)
cookie_x, cookie_y = random.randrange(70,700), random.randrange(70,700) # Random location for the cookie (second food)
orange_x, orange_y = random.randrange(70, 700), random.randrange(70, 700) # Random location for the orange (third food)
choco_x, choco_y = random.randrange(70, 700), random.randrange(70, 700) # Random location for the chocolate (fourth food)
coffee_x, coffee_y = random.randrange(70, 700), random.randrange(70, 700) # Random location for the coffee (fifth food)
cheese_x, cheese_y = random.randrange(70, 700), random.randrange(70, 700) # Random location for the cheese (sixth food)

spray_x, spray_y = random.randrange(70, 700), random.randrange(70, 700) # Random location for the bug spray

score = 0
life = 3
go_lives = 3

up = left = down = right = False # Allows the ant movement to be sustained
speed_up = True # Speeding up the ant
last_score = 0
game_over = False # Set to true when out of lives
high_score = [0]

# Functions - - - - - 

def draw_picture(surface, picture, x, y) : # Draw a picture to the screen
    surface.blit(picture, (x, y))

def draw_text(face, text, colour, surface, x, y) : # Draws text to the screen 
    name = face.render(text, True, colour)
    surface.blit(name, (x,y))

def touch_food(pic1_x, pic1_y, pic2_x, pic2_y, score, spray_x, spray_y) : # Determines if the ant touches a piece of food
    if pic2_x - 8 < pic1_x < pic2_x + 14 and pic2_y - 5 < pic1_y < pic2_y + 25 :
        pic2_x, pic2_y = random.randrange(70,700), random.randrange(70, 700) # Moves the piece of food randomly when touched
        spray_x, spray_y = random.randrange(70,700), random.randrange(70,700) # Moves the bug spray bottle
        bite.play() # Bite sound
        score += 1 # Adds a point to the score
    return pic2_x, pic2_y, score, spray_x, spray_y

def touch_enemy(pic1_x, pic1_y, pic2_x, pic2_y, life) : # Determines if the ant touches an enemy
    if pic2_x - 10 < pic1_x < pic2_x + 20 and pic2_y - 8 < pic1_y < pic2_y + 25 :
        pic2_x, pic2_y = random.randrange(70,700), random.randrange(70, 700)
        life -= 1 # Takes away a life
    return pic2_x, pic2_y, life

def touch_spray(pic1_x, pic1_y, pic2_x, pic2_y, life) : # Determines if the ant touches the bug spray
    if pic2_x - 8 < pic1_x < pic2_x + 14 and pic2_y - 5 < pic1_y < pic2_y + 25 :
        pic2_x, pic2_y = random.randrange(70,700), random.randrange(70, 700) # Moves the piece of spray randomly when touched
        '''bite.play() # Bite sound''' # FIND A NEW SOUND
        life -= 1 # Takes away one life
    return pic2_x, pic2_y, life

def draw_circle(surface, colour, x, y, radius, outline) : # Draws a circle
    pygame.draw.circle(surface, colour, (x, y), radius, outline)

def calc_distance(x1, x2, y1, y2) : # Calculates distance
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def restart_game() : # When the user chooses to restart after a game over, resets everything
    score = 0
    life = go_lives
    ant_x = 400
    ant_y = 400
    x_speed = go_x_speed
    y_speed = go_y_speed
    return(score, life, ant_x, ant_y, x_speed, y_speed)

# Welcome Loop - - - - -

while not done :

    click = False

    # Input - - - - -
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN :
            click = True

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    
    mouse_but = pygame.mouse.get_pressed()
    left_click = mouse_but[0]
    cent_click = mouse_but[1]
    right_click = mouse_but[2]

    colour = window.get_at(mouse_pos)

    # Process - - - - -

    draw_picture(window, background, 0, 0) # Draws the background

    # Start Button

    if left_click and colour == GREEN or colour == LIGHT_GREEN and click : # If the user hits the start button (shape)
        click_option.play()
        break
    if left_click and colour == BLUE or colour == START_RED and click : # If the user hits the start button (text)
        click_option.play()
        break

    # Options

    # Background

    for i in range(5) : # Outline of blanket colour bubbles
        draw_circle(window, BLACK, bg_x[i], bg_y, 25, 0)
    
    for i in range(5) : # Adjust the colour of the blanket
        bg_distance[i] = calc_distance(mouse_x, bg_x[i], mouse_y, bg_y)
        if bg_distance[i] <= 25 :
            draw_circle(window, RED, bg_x[i], bg_y, 25, 0)
        if left_click and bg_distance[i] <= 25 and click :
            background = pygame.image.load(bg_choice[i]).convert()
            bg = bg_choice[i] # For the circle (below)
            click_option.play()
            
        if bg == "Background1.png" :
            draw_circle(window, SELECT_GREEN, bg_x[0], bg_y, 25, 0)
        elif bg == "Background2.png" :
            draw_circle(window, SELECT_GREEN, bg_x[1], bg_y, 25, 0)
        elif bg == "Background3.png" :
            draw_circle(window, SELECT_GREEN, bg_x[2], bg_y, 25, 0)
        elif bg == "Background4.png" :
            draw_circle(window, SELECT_GREEN, bg_x[3], bg_y, 25, 0)
        elif bg == "Background5.png" :
            draw_circle(window, SELECT_GREEN, bg_x[4], bg_y, 25, 0)

    # Volume

    for i in range(4) :
        draw_circle(window, BLACK, vol_x[i], vol_y, 25, 0)
        
    for i in range(4) : # Adjust the volume
        vol_distance[i] = calc_distance(mouse_x, vol_x[i], mouse_y, vol_y)
        if vol_distance[i] <= 25 :
            draw_circle(window, RED, vol_x[i], vol_y, 25, 0)           
        if left_click and vol_distance[i] <= 25 and click :
            pygame.mixer.music.set_volume(volume[i]) # Sets the music volume
            click_option.set_volume(volume[i]) # Sets the sound effect volume
            bite.set_volume(volume[i]) # Sets the bite volume
            vol_level = volume[i] # For the select circle (below)
            click_option.play()
            
    if vol_level == 0.2 :
        draw_circle(window, SELECT_GREEN, vol_x[0], vol_y, 25, 0)
    elif vol_level == 0.6 :
        draw_circle(window, SELECT_GREEN, vol_x[1], vol_y, 25, 0)
    elif vol_level == 1 :
        draw_circle(window, SELECT_GREEN, vol_x[2], vol_y, 25, 0)
    elif vol_level == 0 :
        draw_circle(window, SELECT_GREEN, vol_x[3], vol_y, 25, 0)

    # Lives

    for i in range(3) :
        draw_circle(window, BLACK, life_x[i], life_y, 25, 0)

    for i in range(3) :
        life_distance[i] = calc_distance(mouse_x, life_x[i], mouse_y, life_y)
        if life_distance[i] <= 25 :
            draw_circle(window, RED, life_x[i], life_y, 25, 0)
        if left_click and life_distance[i] <= 25 and click :
            life = life_choice[i]
            go_lives = life_choice[i] # For game over, sets lives back to selected if restart
            click_option.play()

        if life == 1 :
            draw_circle(window, SELECT_GREEN, life_x[0], life_y, 25, 0)
        elif life == 3 :
            draw_circle(window, SELECT_GREEN, life_x[1], life_y, 25, 0)
        elif life == 5 :
            draw_circle(window, SELECT_GREEN, life_x[2], life_y, 25, 0)

    # Speed

    for i in range(3) :
        draw_circle(window, BLACK, spd_x[i], spd_y, 25, 0)

    for i in range(3) :
        spd_distance[i] = calc_distance(mouse_x, spd_x[i], mouse_y, spd_y)
        if spd_distance[i] <= 25 :
            draw_circle(window, RED, spd_x[i], spd_y, 25, 0)
        if left_click and spd_distance[i] <= 25 and click :
            x_speed, y_speed = spd_choice[i], spd_choice[i]
            go_x_speed, go_y_speed = spd_choice[i], spd_choice[i] # Game over selection, reset
            click_option.play()

        if x_speed == 2 :
            draw_circle(window, SELECT_GREEN, spd_x[0], spd_y, 25, 0)
        elif x_speed == 4 :
            draw_circle(window, SELECT_GREEN, spd_x[1], spd_y, 25, 0)
        elif x_speed == 6 :
            draw_circle(window, SELECT_GREEN, spd_x[2], spd_y, 25, 0)

    # Drawing - - - - -

    # Title & Instructions

    draw_picture(window, logo, 105, 100)
    draw_picture(window, instructions, 105, 220)
    instruct_1 = draw_text(font2, "Welcome to 'Picnic Panic!' The goal of this game is to", BLACK, window, 105, 275)
    instruct_2 = draw_text(font2, "collect as much food as possible. Run around the blanket", BLACK, window, 105, 295)
    instruct_3 = draw_text(font2, "with the arrow or WASD keys. Don't run off the edge or you'll ", BLACK, window, 105, 315)
    instruct_4 = draw_text(font2, "lose lives! Be careful, watch for hazards (       &       ), and have fun!", BLACK, window, 105, 335)

    draw_picture(window, options, 105, 360)
    draw_picture(window, bg_text, 105, 405)
    draw_picture(window, volume_text, 105, 495)
    draw_picture(window, life_text, 450, 405)
    draw_picture(window, speed_text, 450, 495)

    draw_picture(window, red_ant, 427, 330) # Red Ant hazard warning
    draw_picture(window, spray, 460, 325) # Spray bottle hazard warning

    # Background Options

    for i in range(5) : # Background bubbles
        draw_circle(window, bg_colour[i], bg_x[i], bg_y, 20, 0)

    # Volume Options

    for i in range(4) :
        draw_circle(window, GREY, vol_x[i], vol_y, 20, 0)
        
    draw_picture(window, vol_quiet, vol_x[0]-14, vol_y-16)
    draw_picture(window, vol_med, vol_x[1]-16, vol_y-16)
    draw_picture(window, vol_loud, vol_x[2]-18, vol_y-16)
    draw_picture(window, vol_mute, vol_x[3]-18, vol_y-16)

    # Life Options

    for i in range(3) :
        draw_circle(window, GREY, life_x[i], life_y, 20, 0)

    draw_picture(window, one_life, life_x[0]-8, life_y-11)
    draw_picture(window, three_life, life_x[1]-10, life_y-11)
    draw_picture(window, five_life, life_x[2]-10, life_y-11)

    # Speed Options

    for i in range(3) :
        draw_circle(window, spd_colour[i], spd_x[i], spd_y, 20, 0)

    # Start Button

    draw_picture(window, start, 320, 610)
    
    if colour == GREEN or colour == LIGHT_GREEN or colour == BLUE or colour == START_RED : # Button Highlight
        draw_picture(window, start_highlight, 320, 610)

    pygame.display.flip()
    clock.tick(60)

# Main Loop - - - - -

while not done :

    click = False

    # Input - - - - -
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN :
            click = True

    key = pygame.key.get_pressed()

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    
    mouse_but = pygame.mouse.get_pressed()
    left_click = mouse_but[0]
    cent_click = mouse_but[1]
    right_click = mouse_but[2]

    colour = window.get_at(mouse_pos)

    # Process - - - - -

    draw_picture(window, background, 0, 0) # Background

    # Ant Movement

    if key[pygame.K_w] or key[pygame.K_UP] : # Move up
        up = True
        left = down = right = False
    elif key[pygame.K_a] or key[pygame.K_LEFT] : # Move left
        left = True
        up = down = right = False
    elif key[pygame.K_s] or key[pygame.K_DOWN] : # Move down
        down = True
        up = left = right = False
    elif key[pygame.K_d] or key[pygame.K_RIGHT] : # Move right
        right = True
        up = down = left = False
        
    if up == True : # Allows the movement to be sustained
        angle = 0
        ant_y -= y_speed
    elif left == True :
        angle = 1
        ant_x -= x_speed
    elif down == True :
        angle = 2
        ant_y += y_speed
    elif right == True :
        angle = 3
        ant_x += x_speed

    if ant_x > 736 : # If the ant touches the edge of the blanket
        ant_x = 400
        any_y = 400
        life -= 1
    elif ant_x < 38 :
        ant_x = 400
        ant_y = 400
        life -= 1
    elif ant_y > 740 :
        ant_x = 400
        ant_y = 400
        life -= 1
    elif ant_y < 35 :
        ant_x = 400
        ant_y = 400
        life -= 1

    # Food

    cherry_x, cherry_y, score, spray_x, spray_y = touch_food(ant_x, ant_y, cherry_x, cherry_y, score, spray_x, spray_y) # Finds a new location for the cherry if it's touched
    if score >= 5 :
        cookie_x, cookie_y, score, spray_x, spray_y = touch_food(ant_x, ant_y, cookie_x, cookie_y, score, spray_x, spray_y)
    if score >= 8 :
        orange_x, orange_y, score, spray_x, spray_y = touch_food(ant_x, ant_y, orange_x, orange_y, score, spray_x, spray_y)
    if score >= 12 :
        choco_x, choco_y, score, spray_x, spray_y = touch_food(ant_x, ant_y, choco_x, choco_y, score, spray_x, spray_y)
    if score >= 15 :
        coffee_x, coffee_y, score, spray_x, spray_y = touch_food(ant_x, ant_y, coffee_x, coffee_y, score, spray_x, spray_y)
    if score >= 18 :
        cheese_x, cheese_y, score, spray_x, spray_y = touch_food(ant_x, ant_y, cheese_x, cheese_y, score, spray_x, spray_y)

    # Bug Spray

    if score >= 12 :
        spray_x, spray_y, life = touch_spray(ant_x, ant_y, spray_x, spray_y, life)

    # Speed Up

    if score % 5 == 0 and score != 0 : # The ant speeds up every five points
        if last_score >= 21 : # Allows the ant to only speed up 4 times
            last_score = 999
        if score > last_score : # Prevents the ant from continuously speeding up
            speed_up = True
        if speed_up :
            x_speed += 2
            y_speed += 2
            speed_up = False
        last_score = score

    # Enemy Ants

    # Ant 1

    red_x += red_x_speed
    red_y += red_y_speed

    if red_x > 736 :
        r_angle = 0
        red_x_speed *= -1
    elif red_x < 38 :
        r_angle = 1
        red_x_speed *= -1

    red_x, red_y, life = touch_enemy(ant_x, ant_y, red_x, red_y, life)

    # Ant 2

    red_x2 += red_x2_speed
    red_y2 += red_y2_speed

    if red_x2 > 736 :
        r2_angle = 0
        red_x2_speed *= -1
    elif red_x2 < 38 :
        r2_angle = 1
        red_x2_speed *= -1

    red_x2, red_y2, life = touch_enemy(ant_x, ant_y, red_x2, red_y2, life)

    # Drawing - - - - -

    draw_picture(window, ant_angle[angle], ant_x, ant_y) # Drawing the ant
    draw_picture(window, cherry, cherry_x, cherry_y) # Drawing the cherry
    if score >= 5 : # Puts a cookie on the screen if the score >= 5
        draw_picture(window, cookie, cookie_x, cookie_y) # Drawing the cookie
    if score >= 8 :
        draw_picture(window, orange, orange_x, orange_y) # Drawing the orange
    if score >= 12 :
        draw_picture(window, choco, choco_x, choco_y) # Drawing the chocolate
    if score >= 15 :
        draw_picture(window, coffee, coffee_x, coffee_y) # Drawing the coffee
    if score >= 18 :
        draw_picture(window, cheese, cheese_x, cheese_y) # Drawing the cheese

    draw_picture(window, red_angle[r_angle], red_x, red_y) # Red Ant
    draw_picture(window, red2_angle[r2_angle], red_x2, red_y2)

    if score >= 12 :
        draw_picture(window, spray, spray_x, spray_y)

    # Score & Life

    score_text = draw_text(font, "Score: %s" %(score), BLACK, window, 50, 50)
    life_counter = draw_text(font, "Lives: %s" %(life), BLACK, window, 50, 75)

    # Game Over - - - - -

    if life == 0 :
        game_over = True

    if game_over :
        draw_picture(window, background, 0, 0)
        draw_picture(window, game_over_text, 70, 100)

        # High Score

        draw_picture(window, high_score_title, 295, 290)
        high_score.append(score)
        high_score_text = draw_text(font, str(max(high_score)), BLACK, window, 395, 350)

        # Your Score

        draw_picture(window, your_score_title, 290, 400)
        your_score_text = draw_text(font, str(score), BLACK, window, 395, 460)

        # Restart

        draw_picture(window, restart, 320, 550)

        if colour == GREEN or colour == LIGHT_GREEN or colour == BLUE or colour == START_RED : # Button Highlight
            draw_picture(window, restart_highlight, 320, 550)

        if left_click and colour == GREEN or colour == LIGHT_GREEN and click : # If the user hits the start button (shape)
            click_option.play()
            score, life, ant_x, ant_y, x_speed, y_speed = restart_game()
            game_over = False
        if left_click and colour == BLUE or colour == START_RED and click : # If the user hits the start button (text)
            click_option.play()
            score, life, ant_x, ant_y, x_speed, y_speed = restart_game()
            game_over = False

    #pygame.draw.rect(window, BLACK, (38,35,720,718), 10) # Blanket Outline (REMOVE)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
