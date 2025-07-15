import pygame
import time

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
        self.origin_x = height // 6.5
        self.origin_y = height - height // 6.5

    def text(self, screen, text, x, y):
        font = pygame.font.SysFont(None, 12)
        text_surface = font.render(text, True, (0, 255, 0))  # Green text
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw(self, screen, Screen_x, Screen_y):
        pygame.draw.rect(screen, GRAY, (Screen_x, Screen_y, self.width, self.height))
        pygame.draw.line(screen, WHITE, (Screen_x + self.origin_x, Screen_y ), (Screen_x + self.origin_x, Screen_y + self.height),1)
        pygame.draw.line(screen, WHITE, (Screen_x , Screen_y + self.origin_y), (Screen_x + self.width, Screen_y + self.origin_y),1)

        for i in range(0, self.width - int(self.origin_x), self.scale):
            pygame.draw.line(screen, WHITE, (Screen_x + i + self.origin_x, Screen_y + self.origin_y - 5), (Screen_x + i + self.origin_x, Screen_y + self.origin_y + 5), 1)
            self.text(screen, str(i*self.scale), Screen_x + i + self.origin_x, Screen_y + self.origin_y + 15)

        for i in range(0, self.height - int(self.height - self.origin_y), self.scale):
            pygame.draw.line(screen, WHITE, (Screen_x + self.origin_x - 5, Screen_y + i), (Screen_x + self.origin_x + 5, Screen_y + i), 1)
            self.text(screen, str(i*self.scale), Screen_x + self.origin_x - 15, int(self.height - self.origin_y) - ( i))