# Snake Game !
# Created by Suryakant

# Our Game Imports
import pygame
import sys
import random
import time

# initialize pygame
# check for initializing errors

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initialising errors existing...".format(check_errors[1]))
    sys.exit(-1)  # We use sys module to get out of the program
else:
    print("(+) PyGame successfully initialized!")

# Creating a player Surface

playSurface = pygame.display.set_mode((720, 460))  # width and height of window
pygame.display.set_caption('snake game!')
# time.sleep(5)

# Colors

# Every pixel have three colors RGB and by using it we can create any color
# and it will show that color if we assign highest value to them ie, 255
# black is absence of color so we assign RGB as 000
# since white is mixture of all the three base colors RGB so assign RGB to be Highest vale
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# Creating Game Variables

# FPS Controller

fpsController = pygame.time.Clock()

# Important Variables

snakePos = [100, 50]  # this variable holds co-ordinate of the snake head
snakeBody = [[100, 50], [90, 50], [80, 50]]

# More On Variables

# food position should be change at every time so we use random module

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

# Direction Variables

direction = 'RIGHT'
changeto = direction

score = 0


# Introduction And Setup Overview

# Game Over Function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)  # First argument is for style of the text and the second one is for size
    GOsurf = myFont.render('Game over!', True, red)  # First argument is for text and second is for anti-aliasing
    # third argument is for color of the font
    GOrect = GOsurf.get_rect()  # It will give rectangular coponent of this gameover surface
    GOrect.midtop = (360, 15)  # It will specify Position of the text
    playSurface.blit(GOsurf, GOrect)  # This will show the text on player surface
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)
    # pygame.display.flip()  # This line is deleted because score card is flickering when we update score twice


# Events
# Main logic of the game

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # keydown means for when we press the key
            if event.key == pygame.K_RIGHT or event.key == ord('d'):  # ord will give ASCII value of its argument
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validation of Directions

    if changeto == 'RIGHT' and not direction == 'LEFT':  # we can't move opposite to the snake head direction directly
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # if we want the snake to move then we have to change the co-ordinates of the snake position
    # if we want the snake to move in left or right then we need to change the x co-ordinate of its position
    # if we want to move the snake in up or down then we need to change the y co- ordinate of its position

    if direction == 'RIGHT':  # one pixel have value 10 so changethe direction by 10
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # snake body mechanism

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    # Food Spawn

    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    # Background

    playSurface.fill(white)

    # Draw Snake

    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    # Bound

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()
    fpsController.tick(15)  # speed of snake

    # quick fixes
    # Improvements
    # we can add menu in this game like play, setting, quit, help, about
    # we can add some sounds, background music
    # we can add more difficulty level
    # we can add images instead of the rectangle and that's pretty interesting
    # we can convert our script into actual executable by using "pyinstaller", it can create executables of any platform
