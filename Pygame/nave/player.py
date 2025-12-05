import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50),pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10

        # Dibujar el triángulo
        pygame.draw.polygon(self.image, (0,0,255),[(),(),()])

    def update(self):
        keys = pygame.key.get_pressed()

        # teclas ocupadas
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
    
        # Mantener la nave dentro de los limites de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 0:
            self.rect.right
    