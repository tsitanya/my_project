import pygame

PLATFORM_WIDTH = 32  # Ширина прямоугольника
PLATFORM_HEIGHT = 32  # Высота
PLATFORM_COLOR = "#006262"  # Цвет прямоугольника


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH,
                                     PLATFORM_HEIGHT))
        self.image = pygame.image.load("images/platform.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH,
                                      PLATFORM_HEIGHT)



class DieBlock(Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("images/dieBlock.png")
