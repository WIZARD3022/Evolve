import pygame

WHITE = (255, 255, 255)

class Graph:
    def __init__(self, width, height, scale):
        self.width = width
        self.height = height
        self.scale = scale
        self.origin_x = 10
        self.origin_y = width - 10

    def draw(self, screen, Screen_x, Screen_y):
        pygame.draw.rect(screen, WHITE, (Screen_x, Screen_y, self.width, self.height))