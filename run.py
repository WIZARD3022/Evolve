import pygame
import sys
from map import Map
from graph import Graph

def main():

    # Initialize Pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 16)

    # Clock for controlling FPS
    clock = pygame.time.Clock()
    FPS = 60

    map1 = Map(700, 500)
    map2 = Map(700, 500)
    # map3 = Map(700, 500)
    graph1 = Graph(420, 300, 20)

    map4 = Map(700, 500)

    map5 = Map(700, 500)
    # map6 = Map(700, 500)
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
                    text_rect = text_surface.get_rect(center=(250, 370))
                    screen.blit(text_surface, text_rect)
                    map2.arr = map2.new()
                    map2.generate_map()
                    map2.draw(screen, 500, 50)
                    text_surface = font.render(map2.dashbord, True, (0, 255, 0))  # Green text
                    text_rect = text_surface.get_rect(center=(700, 370))
                    screen.blit(text_surface, text_rect)
                    # map3.arr = map3.new()
                    # map3.generate_map()
                    # map3.draw(screen, 950, 50)
                    # text_surface = font.render(map3.dashbord, True, (0, 255, 0))  # Green text
                    # text_rect = text_surface.get_rect(center=(1200, 370))

                    graph1.draw(screen, 950, 50)

                    screen.blit(text_surface, text_rect)
                    map4.arr = map4.new()
                    map4.generate_map()
                    map4.draw(screen, 50, 390)
                    text_surface = font.render(map4.dashbord, True, (0, 255, 0))  # Green text
                    text_rect = text_surface.get_rect(center=(250, 700))
                    screen.blit(text_surface, text_rect)
                    
                    map5.arr = map5.new()
                    map5.generate_map()
                    map5.draw(screen, 500, 390)
                    text_surface = font.render(map5.dashbord, True, (0, 255, 0))  # Green text
                    text_rect = text_surface.get_rect(center=(700, 700))
                    screen.blit(text_surface, text_rect)
                    # map6.arr = map6.new()
                    # map6.generate_map()
                    # map6.draw(screen, 950, 390)
                    # text_surface = font.render(map6.dashbord, True, (0, 255, 0))  # Green text
                    # text_rect = text_surface.get_rect(center=(1200, 700))
                    # screen.blit(text_surface, text_rect)

        pygame.display.flip()




    # Quit Pygame
    pygame.quit()
    sys.exit()

main()