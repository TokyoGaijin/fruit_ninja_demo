import pygame
import os
import random

class Fruit:
    def __init__(self, surface, fruit_type = "apple"):
        self.surface = surface
        self.posX = 0
        self.posY = 0
        self.fruit_type = fruit_type
        self.speed = 6
        self.fruit_sprite = pygame.image.load(os.path.join("fruit_sprites", f"{self.fruit_type}.png"))
        self.fruit_rect = pygame.Rect(self.posX, self.posY, self.fruit_sprite.get_width(), self.fruit_sprite.get_height())
        self.isVisible = True

    def set_speed(self):
        self.speed = random.randrange(6, 9)

    def update(self):
        self.posY -= self.speed
        self.speed -= .05

        self.fruit_rect.x = self.posX
        self.fruit_rect.y = self.posY

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.fruit_rect.collidepoint(event.pos):
                    self.isVisible = False

    def draw(self):
        if self.isVisible:
            self.surface.blit(self.fruit_sprite, (self.posX, self.posY))



