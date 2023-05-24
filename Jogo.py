import pygame
pygame.init()

width = 600
height = 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Planet Pong')

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.fill((255,255,255))
    pygame.display.update

pygame.quit()