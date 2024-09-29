import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def fps_counter(screen, clock):
    font = pygame.font.Font(None, 30)
    FPS = f"{int(clock.get_fps())}"
    fps_surface = font.render(FPS, True, "yellow")
    fps_rect = fps_surface.get_rect(center=(20,20))
    screen.blit(fps_surface, fps_rect)

def live_counter(screen, lives):
    surface, rect = draw_text(30, 40, SCREEN_HEIGHT - 20, f"lives: {lives}", "white")
    screen.blit(surface, rect)

def score_count(screen, player):
    font = pygame.font.Font(None, 30)
    score_surface = font.render(f"Score: {player.score}", True, "white")
    score_rect = score_surface.get_rect(center=((SCREEN_WIDTH - 100), 20))
    screen.blit(score_surface, score_rect)

def draw_button(screen,text, rect, color):
    button_font = pygame.font.Font(None, 50)
    pygame.draw.rect(screen, color, rect)
    text_surface = button_font.render(text, True, "white")
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def draw_text(font_size, width, height, text, color):
    font = pygame.font.Font(None, font_size)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(width, height))
    return surface, rect

def start_screen(screen, clock):
    surface, rect = draw_text(200, SCREEN_WIDTH / 2, 200, "Welcome!", "blue")
    button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 120, 200, 80)
    while True:
        screen.fill("black") 
        fps_counter(screen, clock)
        draw_button(screen, "Start", button_rect, "green")
        screen.blit(surface, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return
        pygame.display.flip()

def gameover_screen(screen, clock, score):
    surface, rect = draw_text(200, SCREEN_WIDTH / 2, 200, "Game Over", "red")
    surface1, rect1 = draw_text(150, SCREEN_WIDTH /2, 350, f"Score: {score}", "white")
    button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 + 120, 300, 80)
    while True:
        screen.fill("black") 
        fps_counter(screen, clock)
        draw_button(screen, "Back to menu", button_rect, "green")
        screen.blit(surface, rect)
        screen.blit(surface1, rect1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return
        pygame.display.flip()

def game_loop(screen, clock):
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    field = AsteroidField()
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for player in updatable:
            player.update(dt)
        for a in asteroids:
            if a.collision(p):
                a.kill()
                p.lives -= 1
                if p.lives == 0:
                    gameover_screen(screen, clock, p.score)
                    return
            for s in shots:
                if a.collision(s):
                    s.kill()
                    a.split(p)
        screen.fill("black")
        for player in drawable:
            player.draw(screen)
        score_count(screen, p)
        live_counter(screen, p.lives)
        fps_counter(screen, clock)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    while (True):
        start_screen(screen, clock)
        game_loop(screen, clock)

if __name__ == "__main__":
    main()
