import pygame
import random
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, METEOR_FREQUENCY
from player import Player
from meteor import Meteor

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Nave Espacial vs Meteoritos")
        set.clock = pygame.time.Clock()

        set.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()

        self.player = Player()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Generar meteoritos aleatorios
                if random.randint(1, METEOR_FREQUENCY) == 1:
                    meteor = Meteor()
                    self.all_sprites(meteor)
                    self.meteors.add(meteor)

                # Actualización de todas las posiciones de los sprites
                self.all_sprites.update()

                # Logica para corroborar las colisiones
                if pygame.sprite.spritecollide(self.player, self.meteors, False):
                    print("GAME OVER!")
                    