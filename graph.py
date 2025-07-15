import pygame

WHITE = (255, 255, 255)
GLASS_GREEN = (137, 173, 137)
GLASS_RED = (194, 5, 22)
GLASS_BLUE = (21, 119, 243)
GLASS_YELLOW = (254, 231, 46)
BLACK = (0, 0, 0)
GRAY = (28, 28, 28)


class Graph:
    def __init__(self, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale
        self.origin_x = 10
        self.origin_y = width - 10

    def draw(self, screen, Screen_x, Screen_y):
        pygame.draw.rect(screen, GRAY, (Screen_x, Screen_y, self.width, self.height))
        pygame.draw.line(screen, WHITE, (Screen_x + self.origin_x, Screen_y ), (Screen_x + self.origin_x, Screen_y ),1)