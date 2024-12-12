import pygame
import pyganim
import time
import player

M_WIDTH = 32
M_HEIGHT = 32
MONSTER_COLOR = ('#2110FF')
ANIMATION = ("images/fire1.png",
             "images/fire2.png")
ANIMATION_DELAY = 1

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, x_vel, y_vel, max_x, max_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((M_WIDTH, M_HEIGHT))
        self.image.set_colorkey(pygame.Color(MONSTER_COLOR))
        self.rect = pygame.Rect(x, y, M_WIDTH, M_HEIGHT)
        self.start_x = x
        self.start_y = y

        self.x_vel = x_vel
        self.y_vel = y_vel

        self.max_x = max_x
        self.max_y = max_y


        temp = []
        for img in ANIMATION:
            temp.append((img, ANIMATION_DELAY))
        self.anim = pyganim.PygAnimation(temp)
        self.anim.play()

    def update(self, platforms):
        self.image.fill(pygame.Color(MONSTER_COLOR))
        self.anim.blit(self.image, (0, 0))

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        self.collide(platforms)

    


    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p) and self != p:
                self.x_vel = -self.x_vel
                self.y_vel = - self.y_vel

        start_time = time.time()
        game_over = False







