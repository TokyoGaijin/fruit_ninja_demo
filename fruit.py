import pygame
import os
import random

class Fruit:
    def __init__(self, surface, startX, startY, fruit_type = "apple"):
        self.surface = surface
        self.posX = startX
        self.posY = startY
        self.fruit_type = fruit_type
        self.speed = 5
        self.fruit_sprite = pygame.image.load(os.path.join("fruit_sprites", f"{self.fruit_type}.png"))
        self.fruit_rect = pygame.Rect(self.posX, self.posY, self.fruit_sprite.get_width(), self.fruit_sprite.get_height())
        self.isVisible = True

    def update(self):
        if self.isVisible:
            self.posY -= self.speed
            self.speed -= .05
            if self.posY <= random.randrange(0, 321) or self.speed <= 0:
                self.speed += .05

        self.fruit_rect.x = self.posX
        self.fruit_rect.y = self.posY

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.sprite_rect.collidepoint(event.pos):
                    self.isVisible = False

    def draw(self):
        if self.isVisible:
            self.surface.blit(self.fruit_sprite, (self.posX, self.posY))



