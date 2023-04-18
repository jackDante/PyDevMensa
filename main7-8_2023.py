# ___________ FILE __________________
# soluzione compito a casa:
"""
crea un file chiamato “leggimi.txt”,
apre il file in scrittura e scrive al suo interno i tuoi dati personali “nome, cognome e data nascita”
dopo aver scritto, fa una print() per stampare a video il contenuto del file
infine chiude ed elimina il file creato, quindi il file verrà cancellato dal disco.
"""
"""
import os

# With the code above, whether the file exists or the file doesn't exist in the memory,
# you can still go ahead and use that code. Just keep in mind that it will overwrite the file
# if it finds an existing file with the same name.
with open('leggimi.txt', "w", encoding="utf-8") as f:
    f.write("Giacomo, Usai e 18/07/1997")

with open('leggimi.txt', "r", encoding="utf-8") as f:
    print(f.readlines())

os.remove('leggimi.txt')
"""




"""__________________SNAKE PROJECT!________________________________________________________________________
# step 0:
Installing Pygame:
The first thing you will need to do in order to create games using Pygame is to install it on your systems.
"""
import pygame

"""
# step 1:
# Create the Screen:
To create the screen using Pygame, you will need to make use of the display.set_mode() function. 
Also, you will have to make use of the init()  and the quit() methods to initialize and 
uninitialize everything at the start and the end of the code. The update() method is used 
to update any changes made to the screen. There is another method i.e flip() that works similarly 
to the update() function. The difference is that the update() method updates only the changes 
that are made (however, if no parameters are passed, updates the complete screen) but the flip() method 
redoes the complete screen again.

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.quit()
quit()
"""

# step 2: __________________SNAKE PROJECT!______________________________
# --you will see that the screen that you saw earlier does not quit
# --Pygame provides an event called “QUIT”
"""
import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake game by Giacomo')
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()
"""

#step 3: __________________SNAKE PROJECT!______________________________
# Create the Snake:
# --definisco colori RGB=“Red Green Blue” (0 è nero, 255 è bianco)
# --To draw rectangles in Pygame, you can make use of a
# function called draw.rect() which will help yo draw the rectangle with the desired color and size.
"""
import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Snake game by YOU')

blue = (0, 0, 255)
red = (255, 0, 0)
giallopython = (236, 187, 6)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis, giallopython, [200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()

# ------------ 08/02/2023
"""

# step4: __________________SNAKE PROJECT!______________________________ ----------------------
# Moving the Snake:
# To move the snake, you will need to use the key events present in the KEYDOWN class of Pygame.
# The events that are used over here are, K_UP, K_DOWN, K_LEFT, and K_RIGHT to make the snake move up,
# down, left and right respectively. Also, the display screen is changed from the default black to white
# using the fill() method.
# I have created new variables x1_change and y1_change in order to hold the
# updating values of the x and y coordinates.
"""
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Edureka')

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()

"""
# step4: __________________SNAKE PROJECT!______________________________
# Game Over when Snake hits the boundaries:
# In this snake game, if the player hits the boundaries of the screen, then he loses.
# To specify that, I have made use of an ‘if’ statement that defines the limits for the x and y coordinates
# Of the snake to be less than or equal to that of the screen.
# Also, make a not over here that I have removed the hardcodes and used variables instead
# so that it becomes easy in case you want to make any changes to the game later on.
"""
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('Snake Game by Edureka')

game_over = False

x1 = dis_width / 2
y1 = dis_height / 2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

    pygame.display.update()

    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
"""

# step4: __________________SNAKE PROJECT!______________________________
# Adding the Food:
# Here, I will be adding some food for the snake and when the snake crosses over that food,
# I will have a message saying “Yummy!!”. Also, I will be making a small change wherein
# I will include the options to quit the game or to play again when the player loses.

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


def gameLoop():  # creating a function
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
"""
"""

# step5: __________________SNAKE PROJECT!______________________________
# Displaying the Score:
# Last but definitely not the least, you will need to display the score of the player.
# To do this, I have created a new function as “Your_score”. This function will display
# the length of the snake subtracted by 1 because that is the initial size of the snake.

# SEE FILE finale --> SNAKE.py