import pygame
import colorswatch as cs
import os

pygame.font.init()

class Scoreboard:
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.score = 0
        self.header = None
        self.font = pygame.font.Font(os.path.join("mike-sans-font", "MikeSansFree-MVDLP.ttf"), 20)


    def say(self, score):
        score = self.score
        header = f"Score {score}"
        showtext = self.font.render(header, 1, cs.white["pygame"])
        return showtext


    def draw(self):
        self.surface.blit(self.say(self.score), (self.posX, self.posY))