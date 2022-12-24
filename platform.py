import pygame
import pyganim

PLATFORM_WIDTH = 32  # Ширина прямоугольника
PLATFORM_HEIGHT = 32  # Высота
PLATFORM_COLOR = "#006262"  # Цвет прямоугольника
ANIMATION_DELAY = 1
ANIMATION_TELEPORT = ('images/portal1.png',
                      'images/portal2.png')

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


class TeleportBlock(Platform):
    def __init__(self, x, y, to_x, to_y):
        super().__init__(x, y)
        self.x = to_x
        self.y = to_y
        self.image.set_colorkey(pygame.Color(PLATFORM_COLOR))
        temp = []
        for img in ANIMATION_TELEPORT:
            temp.append((img, ANIMATION_DELAY))
        self.anim = pyganim.PygAnimation(temp)
        self.anim.play()

    def update(self):
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.anim.blit(self.image, (0, 0))

