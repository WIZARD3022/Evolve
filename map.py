import pygame
import sys
import random



# Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (165, 42, 42)
YELLOW = (255, 255, 0)
DARK_GREEN = (0, 100, 0)

# Player (rectangle) settings
# player_pos = pygame.Rect(375, 275, 50, 50)
# player_speed = 5



    # Key handling
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     player_pos.x -= player_speed
    # if keys[pygame.K_RIGHT]:
    #     player_pos.x += player_speed
    # if keys[pygame.K_UP]:
    #     player_pos.y -= player_speed
    # if keys[pygame.K_DOWN]:
    #     player_pos.y += player_speed

    # Draw player
    # pygame.draw.rect(screen, BLUE, player_pos)

    # Update display
    # pygame.display.flip()




class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [70, 50]  # This can be expanded to hold tile data
        self.arr = [[0 for _ in range(self.width//self.tiles[0])] for _ in range(self.height//self.tiles[1])]


    def draw(self, screen):
        # Placeholder for map drawing logic
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                # Draw each tile based on its type
                if self.arr[i][j] == 0:
                    pygame.draw.rect(screen, GREEN, (j * j * self.tiles[0], i * self.tiles[1], self.tiles[0], self.tiles[1]))
                elif self.arr[i][j] == 1:
                    pygame.draw.rect(screen, BROWN, (j * self.tiles[0], i * self.tiles[1], self.tiles[0], self.tiles[1]))
                # Add more tile types as needed
        pass

    def update(self):
        # Placeholder for map update logic
        pass

def main():

    # Initialize Pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Map")

    # Clock for controlling FPS
    clock = pygame.time.Clock()
    FPS = 60

    map = Map(700, 500)
    map.draw(screen)

    area = pygame.Rect(50, 50, 10, 10)

    pygame.draw.rect(screen, BLUE, area)
    pygame.display.flip()
    # Game Loop
    running = True
    while running:
        clock.tick(FPS)  # Limit FPS
        screen.fill(BLACK)  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



    # Quit Pygame
    pygame.quit()
    sys.exit()

main()
#THis is a new line me updated again