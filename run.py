import pygame
import sys
from map import Map

def main():

    # Initialize Pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 13)

    # Clock for controlling FPS
    clock = pygame.time.Clock()
    FPS = 60

    map1 = Map(700, 500)
    map2 = Map(700, 500)
    map3 = Map(700, 500)
    map4 = Map(700, 500)
    map5 = Map(700, 500)
    map6 = Map(700, 500)
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
                    map1.arr = map1.new()
                    map1.generate_map()
                    map1.draw(screen, 50, 50)
                    text_surface = font.render(map1.dashbord, True, (0, 255, 0))  # Green text
                    text_rect = text_surface.get_rect(center=(150, 350))
                    screen.blit(text_surface, text_rect)
                    map2.arr = map2.new()
                    map2.generate_map()
                    map2.draw(screen, 500, 50)
                    map3.arr = map3.new()
                    map3.generate_map()
                    map3.draw(screen, 950, 50)
                    map4.arr = map4.new()
                    map4.generate_map()
                    map4.draw(screen, 50, 400)
                    map5.arr = map5.new()
                    map5.generate_map()
                    map5.draw(screen, 500, 400)
                    map6.arr = map6.new()
                    map6.generate_map()
                    map6.draw(screen, 950, 400)

        pygame.display.flip()




    # Quit Pygame
    pygame.quit()
    sys.exit()

main()