import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption('Flappy Bird')
running = True

GREEN = (0,200,0)
BLUE = (0,0,255)

clock = pygame.time.Clock()

TUBE_WIDTH = 50
TUBE_VELOCITY = 3
TUBE_DISTANCE = 550

tube1_x = 0
tube2_x = 200
tube3_x = 400

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

while running:
    clock.tick(60)
    screen.fill(GREEN)

    pygame.draw.rect(screen, BLUE, (tube1_x, 0, TUBE_WIDTH, tube1_height))
    pygame.draw.rect(screen, BLUE, (tube2_x, 0, TUBE_WIDTH, tube2_height))
    pygame.draw.rect(screen, BLUE, (tube3_x, 0, TUBE_WIDTH, tube3_height))

    tube1_x = tube1_x - 3
    tube2_x = tube2_x - 3
    tube3_x = tube3_x - 3

    if tube1_x < -TUBE_WIDTH:
        tube1_x = 550
    if tube2_x < -TUBE_WIDTH:
        tube2_x = 550
    if tube3_x < -TUBE_WIDTH:
        tube3_x = 550

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()


