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
        self.tiles = [70, 50]  # tile count
        self.size = [10, 10]   # tile size
        self.arr = [[0 for _ in range(self.tiles[0])] for _ in range(self.tiles[1])]
        self.generate_map()

    def draw(self, screen):
        # Placeholder for map drawing 
        for i in range(len(self.arr)):
            print(self.arr[i])
            for j in range(len(self.arr[0])):
                # Draw each tile based on its type
                if self.arr[i][j] == 0:
                    pygame.draw.rect(screen, BLUE, (j * self.size[0] + 50, i * self.size[1] + 50, self.size[0], self.size[1]))
                elif self.arr[i][j] == 1:
                    pygame.draw.rect(screen, GREEN, (j * self.size[0] + 50, i * self.size[1] + 50, self.size[0], self.size[1]))
                elif self.arr[i][j] == 2:
                    pygame.draw.rect(screen, BROWN, (j * self.size[0] + 50, i * self.size[1] + 50, self.size[0], self.size[1]))
                elif self.arr[i][j] == 3:
                    pygame.draw.rect(screen, WHITE, (j * self.size[0] + 50, i * self.size[1] + 50, self.size[0], self.size[1]))
                elif self.arr[i][j] == 4:
                    pygame.draw.rect(screen, YELLOW, (j * self.size[0] + 50, i * self.size[1] + 50, self.size[0], self.size[1]))
                elif self.arr[i][j] == 5:
                    pygame.draw.rect(screen, DARK_GREEN, (j * self.size[0] + 50, i * self.size[1] + 50, self.size[0], self.size[1]))

    def generate_map(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if i != 0 and i != len(self.arr) - 1:
                    rand_val = random.randint(0, 12)
                    point = 0
                    if j != 0 and j != len(self.arr[0]) - 1:
                        if self.arr[i - 1][j - 1] == 1:
                            point += 1
                        if self.arr[i - 1][j] == 1:
                            point += 1
                        if self.arr[i - 1][j + 1] == 1:
                            point += 1
                        if self.arr[i][j - 1] == 1:
                            point += 1

                        prob = 10 - point * 2.5
                        if rand_val > prob:
                            self.arr[i][j] = 1
                    else:
                        self.arr[i][j] = random.choice([0, 1])  # Fix: use random module
                else:
                    self.arr[i][j] = random.choice([0, 1])  # Optional: fill borders

        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if i == 0 or i == len(self.arr) - 1 or j <= 1 or j >= len(self.arr[0]) - 2:
                    self.arr[i][j] = 0

        # pass

    def update(self):
        # Placeholder for map update logic
        pass

def main():

    # Initialize Pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
        # clock.tick(FPS)  # Limit FPS
        pygame.display.set_caption(f"Map and fps :{clock.tick(FPS)}")

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