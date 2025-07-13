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
        self.arr = self.new()  # Initialize the map array
        self.generate_map()

    def new(self):
        return [[0 for _ in range(self.tiles[0])] for _ in range(self.tiles[1])]

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

    def cal(self, x, y):
        val = 0
        origin_x = x - 5
        origin_y = y - 7
        for i in range(origin_x, x):
            for j in range(origin_y, y):
                if i >= 0 and j >= 0 and i < len(self.arr) and j < len(self.arr[0]):
                    if self.arr[i][j] == 1:
                        val += 1
        return val

    def generate_map(self):
        for i in range(2, len(self.arr)-2):
            for j in range(2 , len(self.arr[0])-2):
                if i != 0 and i != len(self.arr) - 1:
                    rand_val = random.randint(0, 11)
                    point = 0
                    if j >= 1 and j <= len(self.arr[0]) - 2:
                        if self.arr[i - 1][j - 1] == 1:
                            point += 1
                        if self.arr[i - 1][j] == 1:
                            point += 1
                        # if self.arr[i - 1][j + 1] == 1:
                        #     point += 1
                        if self.arr[i][j - 1] == 1:
                            point += 1
                        
                        if self.arr[i - 2][j - 2] == 1:
                            point += 1

                        if self.arr[i - 2][j - 1] == 1:
                            point += 1
                        if self.arr[i - 2][j] == 1:
                            point += 1
                        # if self.arr[i - 2][j + 1] == 1:
                        #     point += 1
                        # if self.arr[i - 2][j + 2] == 1:
                        #     point += 1

                        if self.arr[i - 1][j - 2] == 1:
                            point += 1
                        if self.arr[i - 1][j - 1] == 1:
                            point += 1
                        # if self.arr[i - 1][j + 2] == 1:
                        #     point += 1


                        if self.arr[i - 3][j - 3] == 1:
                            point += 1
                        if self.arr[i - 3][j - 2] == 1:
                            point += 1
                        if self.arr[i - 3][j - 1] == 1:
                            point += 1
                        if self.arr[i - 3][j] == 1:
                            point += 1
                        if self.arr[i - 2][j - 3] == 1:
                            point += 1
                        if self.arr[i - 1][j - 3] == 1:
                            point += 1
                        if self.arr[i][j - 3] == 1:
                            point += 1
                        # if self.arr[][] == 1:
                        #     point += 1

                        # control = 0
                        # if i >= 5 and j >= 7:
                        control = self.cal(i, j)

                        prob = 10 - point * 1.5 + control * 1.5
                        if rand_val > prob:
                            self.arr[i][j] = 1
                    else:
                        self.arr[i][j] = random.choice([0, 1])  # Fix: use random module
                else:
                    self.arr[i][j] = random.choice([0, 1])  # Optional: fill borders

        self.transform_map()

        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if i == 0 or i == len(self.arr) - 1 or j <= 1 or j >= len(self.arr[0]) - 2:
                    self.arr[i][j] = 0


    def check(self, x, y, val):

        if val == 2:
            if self.arr[x-2][y] == 2 or self.arr[x][y-2] == 2:
                return False
            return True

        if self.arr[x-1][y-1] == val and self.arr[x-1][y] == val and self.arr[x-1][y+1] == val and self.arr[x][y-1] == val and self.arr[x][y] == val and self.arr[x][y+1] == val and self.arr[x+1][y-1] == val and self.arr[x+1][y] == val and self.arr[x+1][y+1] == val:
            return True
        return False

    def transform_map(self):
        for i in range(1, len(self.arr)-1):
            for j in range(1 ,len(self.arr[0])-1):
                # Ice lands
                if 0 <= i <= 5 or len(self.arr[i]) - 5 <= i <= len(self.arr[i]) - 1:
                    rand_val = random.randint(0, 10)
                    condition = self.check(i, j, 0)
                    if rand_val > 7 and condition == 1:
                        self.arr[i][j] = random.choice([0, 3])
                if 0 <= i <= 6 or len(self.arr[i]) - 6 <= i <= len(self.arr[i]) - 1:
                    rand_val = random.randint(0, 12)
                    condition = self.check(i, j, 0)
                    if rand_val > 9 and condition == 1:
                        self.arr[i][j] = random.choice([0, 3])

        for i in range(1, len(self.arr)-1):
            for j in range(1 ,len(self.arr[0])-1):
                # Forest lands
                if len(self.arr[i])//2-5 <= i <= len(self.arr[i])//2+5:
                    rand_val = random.randint(0, 10)
                    condition = self.check(i, j, 1)
                    if rand_val > 6 and condition == 1:
                        for k in range(i-1, i+2):
                            for l in range(j-1, j+2):
                                self.arr[k][l] = random.choice([0, 1, 5])
                if len(self.arr[i])//2-10 <= i <= len(self.arr[i])//2+10:
                    rand_val = random.randint(0, 12)
                    condition = self.check(i, j, 1)
                    if rand_val > 8 and condition == 1:
                        for k in range(i-1, i+2):
                            for l in range(j-1, j+2):
                                self.arr[k][l] = random.choice([0, 1, 5])

        for i in range(1, len(self.arr)-1):
            for j in range(1 ,len(self.arr[0])-1):
                # Desert lands
                if len(self.arr[i])//4-5 <= i <= len(self.arr[i])//4+5:
                    rand_val = random.randint(0, 10)
                    condition = self.check(i, j, 0)
                    if rand_val > 6 and condition != 1:
                        for k in range(i-1, i+2):
                            for l in range(j-1, j+2):
                                self.arr[k][l] = random.choice([0, 1, 4, 5])

        for i in range(1, len(self.arr)-1):
            for j in range(1 ,len(self.arr[0])-1):
                # Mountain areas
                if len(self.arr[i])//4-30 <= i <= len(self.arr[i])//4+30:
                    rand_val = random.randint(0, 20)
                    condition = self.check(i, j, 2)
                    if rand_val > 19 and condition == 1:
                        for k in range(i-1, i+2):
                            for l in range(j-1, j+2):
                                self.arr[k][l] = random.choice([0, 1, 2])

        # for i in range(1, len(self.arr)-1):
        #     for j in range(1 ,len(self.arr[0])-1):

                        


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
    # map.draw(screen)

    # area = pygame.Rect(50, 50, 10, 10)

    # pygame.draw.rect(screen, BLUE, area)
    # Game Loop
    running = True
    while running:
        # clock.tick(FPS)  # Limit FPS
        pygame.display.set_caption(f"Map and fps :{clock.tick(FPS)}")

        # screen.fill(BLACK)  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    map.arr = map.new()
                    map.generate_map()
                    map.draw(screen)

        pygame.display.flip()




    # Quit Pygame
    pygame.quit()
    sys.exit()

main()