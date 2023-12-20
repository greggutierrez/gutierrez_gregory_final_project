# Project Title: Video Game Design

# Project Goals:
# Create smooth running game with minimal errors
# Make the game enjoyable
# Have a Start and end scren
# Make the game creative and unique
# Make it a type of game that can have future updates even after the semester
# Works Cited: https://www.youtube.com/watch?v=Qf3-aDXG8q4

# GameDesign:
# Goals: Beat your record
# Rules: Don't let the ball hit your side
# Feedback: Title and Game over screen
# Freedom: 

# Future Goals:
# Different game modes


import pygame, sys, random

# Defining the ball, player, and opponent animations
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *=random.choice((1,-1))
    ball_speed_x *=random.choice((1,-1))
    

# Setup for the game
pygame.init()
clock = pygame.time.Clock()


# Setup for the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Game Shapes
ball = pygame.Rect(screen_width/2,screen_height/2,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
bg_color = pygame.Color('grey12')
green = (0,128,0)

# Speed of each piece of the game
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7 


# This is what happens when the game is quit
# Controls for the game (up and down key)
# How the player speed and direction are affected
while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7
                
            

    ball_animation()
    player_animation()
    opponent_ai()

# Color of each object and how each is made
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,green, player)
    pygame.draw.rect(screen,green, opponent)
    pygame.draw.ellipse(screen, green, ball)
    pygame.draw.aaline(screen, green, (screen_width/2,0), (screen_width/2,screen_height))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)

