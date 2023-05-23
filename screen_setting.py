import pygame
import colorswatch as cs

class Game_Screen:
    def __init__(self, title = "Untitled Game", sizeX = 640, sizeY = 480, bgColor = cs.cornflower_blue["pygame"]):
        self.title = title
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.screen_size = (sizeX, sizeY)
        self.bg = bgColor
        self.surface = pygame.display.set_mode(self.screen_size)
        self.CLOCK = pygame.time.Clock()
        self.FPS = 60

    def update(self):
        self.CLOCK.tick(self.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit(1)

        pygame.display.update()
        self.surface.fill(self.bg)
