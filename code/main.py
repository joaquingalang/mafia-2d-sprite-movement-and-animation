import pygame
import sys
from settings import *
from tile import Tile
from player import Player

class Game:
    def __init__(self):
        # General Set Up
        pygame.init()
        pygame.display.set_caption('Soul Exorcist')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        # Initialize Sprite Groups
        self.visible_sprites = YSortCameraGroup()
        self.floor_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Initialize Map
        self.create_map()

    def create_map(self):
        # Initializes The Map
        for x_index, row in enumerate(WORLD_MAP):
            for y_index, col in enumerate(row):
                x_pos = y_index * TILESIZE
                y_pos = x_index * TILESIZE
                pos = (x_pos, y_pos)

                if col == 'X':
                    # Create Boundry Tile
                    Tile(pos, [self.obstacle_sprites], 'boundry')
                elif col == 'C':
                    # Create Column
                    Tile(pos, [self.visible_sprites, self.obstacle_sprites], 'column')
                elif col == 'P':
                    # Create Player
                    self.player = Player(pos, [self.visible_sprites])
                else:
                    print(col)

                # Build Floor For Each Tile
                Tile(pos, [self.floor_sprites], 'floor')

    def run(self):
        # Gameplay Loop
        while True:

            # Event Loop (Gets all the events while the game is running)
            for event in pygame.event.get():
                # If the event is when the user clicks the window's "X" , terminate the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Fill Screen With Black
            self.screen.fill('black')

            # Draw & Update Sprite Groups
            self.floor_sprites.custom_draw(self.player)
            self.floor_sprites.update()

            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()

            # Update Display
            pygame.display.update()

            # Manage FPS
            self.clock.tick(FPS)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # General Setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    # Draw All Elements Relative To The Player
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

if __name__ == '__main__':
    game = Game()
    game.run()