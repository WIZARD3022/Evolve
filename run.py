import pygame
import sys
from map import Map

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