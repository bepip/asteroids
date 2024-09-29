import pygame
from constants import *
from player import *
import player

def fps_counter(screen, clock):
    font = pygame.font.Font(None, 30)
    FPS = f"{int(clock.get_fps())}"
    fps_surface = font.render(FPS, True, "yellow")
    fps_rect = fps_surface.get_rect(center=(20,20))
    screen.blit(fps_surface, fps_rect)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        p.draw(screen)
        dt = clock.tick(60) / 1000
        fps_counter(screen, clock)
        p.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
