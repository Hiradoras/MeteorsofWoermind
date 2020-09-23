import pygame
import time
import random

pygame.init()

from pygame import mixer


crash_FX = mixer.Sound("crash.wav")
pygame.mixer.Sound.set_volume(crash_FX, 20)



display_width = 600
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (180,0,0)
bright_red = (255,0,0)

green = (0,180,0)
bright_green = (0,255,0)

purple = (51,0,102)
bright_purple = (102,0,204)

blue = (0, 87, 173)
bright_blue = (64, 159, 255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Woermind")
clock = pygame.time.Clock()

playerImg = pygame.image.load('player.png')
player_x = playerImg.get_size()[0]
player_y = playerImg.get_size()[1]

pause = False

def things_dodged(count, level):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: "+str(count),True,red)
    gameDisplay.blit(text,(0,0))

    text = font.render("Level: "+str(level),True,red)
    gameDisplay.blit(text,(0,30))
#######################################
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#######################################
def player(x,y):
    gameDisplay.blit(playerImg,(x,y))
#######################################
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#######################################
def message_display(text, dodged, level):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

    time.sleep(1)

    #game_loop() #IT WILL RESTART THE GAME
    menu_screen(dodged, level)
#######################################
def menu_screen(dodged,level):
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(red)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        smallText = pygame.font.Font('freesansbold.ttf',30)
        #Score
        textScore, textScoreRect = intro_text("SCORE: "+str(dodged), smallText)
        textScoreRect.center = ((display_width/2),(display_height/2)-60)
        gameDisplay.blit(textScore,textScoreRect)

        #Level
        textLevel, textLevelRect = intro_text("LEVEL: "+str(level), smallText)
        textLevelRect.center = ((display_width/2),(display_height/2)-30)
        gameDisplay.blit(textLevel,textLevelRect)
        
        #Ask for replay
        textSurf, textRect = intro_text("Want to replay?", largeText)
        textRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(textSurf,textRect)

        button("YES", 150,400,100,50,green,bright_green,game_loop)
        button("NO", 350,400,100,50,purple,bright_purple,game_intro)
        pygame.display.update()
        clock.tick(15)
#######################################
def crash(dodged,level):
    pygame.draw.rect(gameDisplay,bright_red,[(display_width/2)-175,(display_height/2)-30,350,50])
    message_display('CRASHED',dodged,level)
    
#######################################
def quit_game():
    pygame.quit()
    quit()
#######################################
def button(msg, x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w>mouse[0]>x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
            

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = intro_text(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

#######################################
def intro_text(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
#######################################
def unpause():
    global pause
    pause = False

#######################################
def pause_text(text, font):
    textSurface = font.render(text, True, green)
    return textSurface, textSurface.get_rect()
#######################################
def paused():
    
    mixer.music.load('pygame_gameplay_music.wav')
    mixer.music.play(-1)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    unpause()
        #gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = pause_text("Paused", largeText)
        textRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(textSurf,textRect)

        textNameSurf, textNameRect = pause_text("by Ahmet Kozal", smallText)
        textNameRect.center = ((display_width/2),(display_height/1-40))
        gameDisplay.blit(textNameSurf,textNameRect)

        button("Continue", 150,350,100,50,green,bright_green,unpause)
        button("Menu", 350,350,100,50,red,bright_red,game_intro)
        #button("CREDITS", 250,450,100,50,blue,bright_blue,credits_screen)
        pygame.display.update()
        clock.tick(15)
#######################################
def game_intro():
    intro = True
    mixer.music.load('pygame_intro_music.wav')
    mixer.music.play(-1)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = intro_text("Meteors of Woermind", largeText)
        textRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(textSurf,textRect)

        textNameSurf, textNameRect = intro_text("by Ahmet Kozal", smallText)
        textNameRect.center = ((display_width/2),(display_height/1-40))
        gameDisplay.blit(textNameSurf,textNameRect)

        button("START", 150,450,100,50,green,bright_green,game_loop)
        button("QUIT", 350,450,100,50,red,bright_red,quit_game)
        button("CREDITS", 250,450,100,50,blue,bright_blue,credits_screen)
        button("HOW TO", 250,500,100,50,blue,bright_blue,how_to_screen)
        pygame.display.update()
        clock.tick(15)

#######################################
def how_to_screen():
    how_to = True
    mixer.music.load('pygame_credits_music.wav')
    mixer.music.play(-1)
    while how_to:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        smallText = pygame.font.Font('freesansbold.ttf',18)
        textSurf, textRect = intro_text("When you reach 10 score, game will be harder.", smallText)
        textRect.center = ((display_width/2),(display_height/10))
        gameDisplay.blit(textSurf,textRect)

        textSurf, textRect = intro_text("And same when you reach score 15, 2 new block will start to fall.", smallText)
        textRect.center = ((display_width/2),(display_height/10+20))
        gameDisplay.blit(textSurf,textRect)

        textSurf, textRect = intro_text("You can pause the game with pressing 'P' key.", smallText)
        textRect.center = ((display_width/2),(display_height/10+40))
        gameDisplay.blit(textSurf,textRect)

        textSurf, textRect = intro_text("Try to dodge blocks by the way!", smallText)
        textRect.center = ((display_width/2),(display_height/10+60))
        gameDisplay.blit(textSurf,textRect)

        button("Menu", 250,550,100,50,red,bright_red,game_intro)
        pygame.display.update()
        clock.tick(15)
#######################################
def credits_screen():
    credits = True
    mixer.music.load('pygame_credits_music.wav')
    mixer.music.play(-1)
    while credits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = intro_text("CREDITS", largeText)
        textRect.center = ((display_width/2),(display_height/10))
        gameDisplay.blit(textSurf,textRect)
        #Music and FX
        textMusicSurf, textMusicRect = intro_text("Musics and FX: AHMET KOZAL", smallText)
        textMusicRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(textMusicSurf,textMusicRect)

        #Models
        textMusicSurf, textMusicRect = intro_text("Models by: AHMET KOZAL", smallText)
        textMusicRect.center = ((display_width/2),(display_height/3-30))
        gameDisplay.blit(textMusicSurf,textMusicRect)

        #Game
        textMusicSurf, textMusicRect = intro_text("Game by: AHMET KOZAL", smallText)
        textMusicRect.center = ((display_width/2),(display_height/3-60))
        gameDisplay.blit(textMusicSurf,textMusicRect)

        button("MENU", 150,350,100,50,green,bright_green,game_intro)
        button("QUIT", 350,350,100,50,red,bright_red,quit_game)
        pygame.display.update()
        clock.tick(15)

#######################################
def game_loop():
    global pause 
    mixer.music.load('pygame_gameplay_music.wav')
    mixer.music.play(-1)
    x = display_width * 0.45
    y = display_height * 0.8

    x_leftchange = 0
    x_rightchange = 0

    max_up = display_height * 0.8-40
    max_down = display_height * 0.8+40

    y_upchange = 0
    y_downchange = 0 

    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0,display_width-thing_width)
    thing_starty =  -600
    thing_speed = 10
    thing_maxspeed = 15

    #Falling with random speed object
    thing2_width = 5
    thing2_height = 150
    thing2_startx = random.randrange(0,display_width-thing_width)
    thing2_starty =  -600
    thing2_speed = 20
    thing2_minspeed =15
    thing2_maxspeed = 25

    #Bouncing from the walls object
    thing3_width = 40
    thing3_height = 40
    thing3_startx = random.randrange(0,display_width-thing_width)
    thing3_starty =  -600
    thing3_yspeed = 10
    thing3_xspeed = 20

    #Bouncing from the walls object
    thing4_width = 40
    thing4_height = 40
    thing4_startx = random.randrange(0,display_width-thing_width)
    thing4_starty =  -600
    thing4_yspeed = 5
    thing4_xspeed = 25



    player_speed = 8
    player_maxspeed = 12

    dodged = 0
    level = 1
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    x_leftchange = 0
                    x_rightchange = 0
                    y_upchange = 0
                    y_downchange = 0

                if event.key == pygame.K_LEFT:
                    x_leftchange = player_speed*-1
                if event.key == pygame.K_RIGHT:
                    x_rightchange = player_speed

                if event.key == pygame.K_UP:
                    y_upchange = player_speed *-1
                if event.key == pygame.K_DOWN:
                    y_downchange = player_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_leftchange = 0
                if event.key == pygame.K_RIGHT:
                    x_rightchange = 0  
                
                if event.key == pygame.K_UP:
                    y_upchange = 0
                if event.key == pygame.K_DOWN:
                    y_downchange = 0
             
        x += x_leftchange
        x += x_rightchange

        y += y_upchange
        y += y_downchange

        if y < max_up:
            y = max_up
        if y> max_down:
            y = max_down
        
        gameDisplay.fill(white)
        
        #Next Level
        if dodged>= 10:
            level = 2
            things(thing2_startx, thing2_starty,thing2_width, thing2_height,red)
            thing2_starty += thing2_speed
            if thing2_starty > display_height:
                thing2_starty = 0 - thing2_height
                thing2_startx = random.randrange(0, display_width-thing_width)
                dodged +=1
                thing2_speed += random.randrange(-10,15)
                if thing2_speed >= thing2_maxspeed:
                    thing2_speed += random.randrange(-20,0)
                if thing2_speed <= thing2_minspeed:
                    thing2_speed += random.randrange(5,30)
        #Next Level
        if dodged>= 15:
            level = 3
            things(thing3_startx, thing3_starty,thing3_width, thing3_height,blue)
            thing3_starty += thing3_yspeed
            thing3_startx += thing3_xspeed

            if thing3_starty > display_height:
                thing3_starty = 0 - thing2_height
                thing3_startx = random.randrange(0, display_width-thing_width)
                dodged +=1
            
            if thing3_startx > display_width - thing3_width or thing3_startx < 0:
                thing3_xspeed *= -1
            
            things(thing4_startx, thing4_starty,thing4_width, thing4_height,blue)
            thing4_starty += thing4_yspeed
            thing4_startx += thing4_xspeed

            if thing4_starty > display_height:
                thing4_starty = 0 - thing4_height
                thing4_startx = random.randrange(0, display_width-thing_width)
                dodged +=1
            
            if thing4_startx > display_width - thing4_width or thing4_startx < 0:
                thing4_xspeed *= -1            

        things(thing_startx, thing_starty,thing_width, thing_height,black)
        thing_starty += thing_speed
        player(x,y)
        things_dodged(dodged, level)
        #LOGICS##################################################
        #!!! Canceled make player dead when he touch the edges !!!
        if x > display_width - player_x:
            x = display_width - player_x
            #crash_FX.play()       
            # crash(dodged, level)
        if x < 0:
            x = 0
        ##########################################
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width-thing_width)
            dodged +=1
            if thing_speed <= thing_maxspeed:
                thing_speed +=1
            if player_speed <= player_maxspeed:
                player_speed +=0.2
            
            
        if y < (thing_starty+thing_height) and y> thing_starty :
            if (x+player_x >= thing_startx and x <= thing_width+thing_startx): 
                crash_FX.play()                
                crash(dodged,level)
        if y < (thing2_starty+thing2_height) and y> thing2_starty :
            if (x+player_x >= thing2_startx and x <= thing2_width+thing2_startx): 
                crash_FX.play()                
                crash(dodged, level)
        if y < (thing3_starty+thing3_height) and y> thing3_starty :
            if (x+player_x >= thing3_startx and x <= thing3_width+thing3_startx): 
                crash_FX.play()                
                crash(dodged,level)
        if y < (thing4_starty+thing4_height) and y> thing4_starty :
            if (x+player_x >= thing4_startx and x <= thing4_width+thing4_startx): 
                crash_FX.play()                
                crash(dodged,level)


        
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
