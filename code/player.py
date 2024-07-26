import pygame
from settings import *

# Everything about our player is stored in the Player Sprite!
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # General Set Up
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 4)
        self.rect = self.image.get_rect(topleft = pos)

        # Movement
        self.direction = pygame.math.Vector2()

        # Status & Orientation
        self.status = 'idle'
        self.facing = 'right'

        # Animation
        self.animation_frame = 0
        self.animation_speed = 0.15

    # Collect User Input
    def input(self):
        keys = pygame.key.get_pressed()

        self.status = 'idle'

        # Vertical Movement
        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'run'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'run'
        else:
            self.direction.y = 0

        # Horizontal Movement
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'run'
            self.facing = 'left'
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'run'
            self.facing = 'right'
        else:
            self.direction.x = 0

    # Move The Player Based On Direction
    def move(self):
        speed = 6
        self.rect.x += self.direction.x * speed
        self.rect.y += self.direction.y * speed

    # Implement Animations For Current Status & Orientation
    def animations(self):
        self.animation_frame += self.animation_speed
        if self.animation_frame > 3: self.animation_frame = 0
        self.image = pygame.image.load(f'../graphics/player/{self.status}/{self.facing}/{int(self.animation_frame)}.png')
        self.image = pygame.transform.scale_by(self.image, 4)
            
    # Update Player (This method is called in every iteration of the gameplay loop)
    def update(self):
        self.input()
        self.animations()
        self.move()


