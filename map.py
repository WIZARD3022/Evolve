import pygame
import random
import copy

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
        self.tiles = [210, 150]  # tile count
        self.size = [2, 2]   # tile size
        self.arr = self.new()  # Initialize the map array
        self.generate_map()

    def new(self):
        return [[0 for _ in range(self.tiles[0])] for _ in range(self.tiles[1])]

    def draw(self, screen, Screen_x=50 , Screen_y=50):
        # Placeholder for map drawing 
        for i in range(len(self.arr)):
            print(self.arr[i])
            for j in range(len(self.arr[0])):
                # Draw each tile based on its type
                if self.arr[i][j] == 0:
                    pygame.draw.rect(screen, BLUE, (j * self.size[0] + Screen_x, i * self.size[1] + Screen_y, self.size[0], self.size[1]))
                elif self.arr[i][j] == 1:
                    pygame.draw.rect(screen, GREEN, (j * self.size[0] + Screen_x, i * self.size[1] + Screen_y, self.size[0], self.size[1]))
                elif self.arr[i][j] == 2:
                    pygame.draw.rect(screen, BROWN, (j * self.size[0] + Screen_x, i * self.size[1] + Screen_y, self.size[0], self.size[1]))
                elif self.arr[i][j] == 3:
                    pygame.draw.rect(screen, WHITE, (j * self.size[0] + Screen_x, i * self.size[1] + Screen_y, self.size[0], self.size[1]))
                elif self.arr[i][j] == 4:
                    pygame.draw.rect(screen, YELLOW, (j * self.size[0] + Screen_x, i * self.size[1] + Screen_y, self.size[0], self.size[1]))
                elif self.arr[i][j] == 5:
                    pygame.draw.rect(screen, DARK_GREEN, (j * self.size[0] + Screen_x, i * self.size[1] + Screen_y, self.size[0], self.size[1]))

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
    
    def improve_map_realism(self, smooth_passes=1, start = 1, end = 2):
        """
        Smooths and improves the terrain to make it more natural.
        - smooth_passes: number of smoothing iterations
        """
        for _ in range(smooth_passes):
            new_arr = copy.deepcopy(self.arr)

            for i in range(start, end - 1):
                for j in range(start, len(self.arr[i]) - 1):
                    neighbors = [self.arr[i-1][j-1], self.arr[i-1][j], self.arr[i-1][j+1],
                                self.arr[i][j-1],               self.arr[i][j+1],
                                self.arr[i+1][j-1], self.arr[i+1][j], self.arr[i+1][j+1]]
                    
                    current = self.arr[i][j]
                    counts = {val: neighbors.count(val) for val in set(neighbors)}
                    
                    # Majority vote smoothing: pick most frequent neighbor type
                    if counts:
                        majority = max(counts, key=counts.get)
                        if counts[majority] >= 5 and majority != current:
                            new_arr[i][j] = majority

            self.arr = new_arr

        self.refine_transitions()

    def refine_transitions(self):
        """
        Refines transitions between land types (e.g., water to forest, desert to grassland)
        """
        for i in range(1, len(self.arr) - 1):
            for j in range(1, len(self.arr[0]) - 1):
                curr = self.arr[i][j]
                neighbors = [self.arr[i+dx][j+dy]
                            for dx in [-1, 0, 1]
                            for dy in [-1, 0, 1]
                            if not (dx == 0 and dy == 0)]

                # Smooth forest borders
                if curr == 5 and neighbors.count(1) >= 5:
                    self.arr[i][j] = 1

                # Desert blends into grassland
                if curr == 4 and neighbors.count(1) >= 5:
                    self.arr[i][j] = random.choice([1, 4])

                # Ice blends into water
                if curr == 3 and neighbors.count(0) >= 5:
                    self.arr[i][j] = random.choice([0, 3])

                # Mountains into grassland
                if curr == 2 and neighbors.count(1) >= 6:
                    self.arr[i][j] = random.choice([1, 2])


    def generate_map(self):
        for i in range(2, len(self.arr)-2):
            for j in range(2 , len(self.arr[0])-2):
                if i != 0 and i != len(self.arr) - 1:
                    rand_val = random.randint(0, 12)
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

        self.improve_map_realism(1, 1, len(self.arr) - 1)
        
        Random = random.randint(0, 10)
        start = random.randint(0, round((len(self.arr))/1.5))
        end = random.randint(start + Random , round((len(self.arr))/1.5) + start + Random)
        print(f"Start: {start}, End: {end}, Random: {Random}")
        if random.randint(0, 10) > 6:
            self.improve_map_realism(2, start, end)
        if random.randint(0, 10) > 6:
            self.improve_map_realism(3, start, end)





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
                    if rand_val > 6 and condition == 1:
                        for k in range(i-1, i+2):
                            for l in range(j-1, j+2):
                                self.arr[k][l] = random.choice([0, 3])
                if 0 <= i <= 6 or len(self.arr[i]) - 6 <= i <= len(self.arr[i]) - 1:
                    rand_val = random.randint(0, 12)
                    condition = self.check(i, j, 0)
                    if rand_val > 8 and condition == 1:
                        self.arr[i][j] = 3

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

