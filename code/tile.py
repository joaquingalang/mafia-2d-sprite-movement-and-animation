import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, tile_type='boundry'):
        super().__init__(groups)
        
        if tile_type == 'boundry': 
            self.image = pygame.Surface((64,64))
        else:
            self.image = pygame.image.load(f'../graphics/{tile_type}.png').convert_alpha()
            self.image = pygame.transform.scale_by(self.image, 4)

        self.rect = self.image.get_rect(topleft = pos)

        if tile_type == 'column':
            self.rect.y -= 16