import pygame, random
pygame.init()

width = 700
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Planet Pong')

width_planets = 25
height_planets = 25
preto = pygame.Color('grey0')
#Imagens-----------------------------------------------------------
terra_img = pygame.image.load('Terran.png').convert_alpha()
terra_img = pygame.transform.scale(terra_img, (width_planets, height_planets))
lava_img = pygame.image.load('Lava.png').convert_alpha()
lava_img = pygame.transform.scale(lava_img,(width_planets, height_planets))
Ice_img = pygame.image.load('Ice.png')
Ice_img = pygame.transform.scale(Ice_img, (width_planets, height_planets))
black_hole_img = pygame.image.load('Black_hole.png').convert_alpha()
black_hole_img = pygame.transform.scale(black_hole_img, (width_planets, height_planets))
baren_img = pygame.image.load('Baren.png')
baren_img = pygame.transform.scale(baren_img, (width_planets, height_planets))
#------------------------------------------------------------------------
player1 = pygame.Rect(width-10, height/2-40,20,80)
player2 = pygame.Rect(-10, height/2-40,20,80)
player1_speed = 0
player2_speed = 0
#Classe Planetas--------------------------------------------------
class Planetas(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (width / 2) - 12.5
        self.rect.y = (height / 2) - 12.5
        self.speedx = 2
        self.speedy = 2
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speedy *= (-1)
        if self.rect.right >= width or self.rect.left <= 0:
            self.speedx *= (-1)
#---------------------------------------------------------

#Planetas-----------------------------------------------------------
terra = Planetas(terra_img)
lava = Planetas(lava_img)
gelo = Planetas(Ice_img)
black_hole = Planetas(black_hole_img)
baren = Planetas(baren_img)
planetas_lista = [terra, lava, gelo, black_hole, baren, ]
escolhido = random.choice(planetas_lista)
#----------------------------------------------------------------------
game = True
clock = pygame.time.Clock()
FPS = 50

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 4
            if event.key == pygame.K_UP:
                player1_speed -= 4
            if event.key == pygame.K_w:
                player2_speed -= 4
            if event.key == pygame.K_s:
                player2_speed += 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 4
            if event.key == pygame.K_UP:
                player1_speed += 4
            if event.key == pygame.K_w:
                player2_speed += 4
            if event.key == pygame.K_s:
                player2_speed -= 4
            if player1.top <=0:
                player1.top =0
            if player1.bottom >= height:
                player1.bottom=height
            if player2.top <=0:
                player2.top =0
            if player2.bottom >= height:
                player2.bottom=height
    player1.y += player1_speed
    player2.y += player2_speed
    escolhido.update()
    window.fill((255,255,255))
    pygame.draw.rect(window, preto,player1)
    pygame.draw.rect(window, preto, player2)
    pygame.draw.aaline(window, preto, (width/2,0), (width/2, height))
    window.blit(escolhido.image, escolhido.rect)

    pygame.display.update()

pygame.quit()