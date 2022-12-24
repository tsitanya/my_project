import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)



class Camera:
    def __init__(self, lvl_w, lvl_h):
        self.camera_config = self.configure
        self.state = pygame.Rect(0, 0, lvl_w, lvl_h)

    def apdate(self, hero):
        self.state = self.camera_config(self.state, hero.rect)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    @staticmethod
    def configure(past_state, hero_rect):
        _, _, w, h = past_state
        x, y, _, _ = hero_rect

        x = WIN_WIDTH / 2 - x
        y = WIN_HEIGHT / 2 - y


        x = min(0, x)
        x = max(-(w - WIN_WIDTH), x)

        y = min(0, y)
        y = max(-(h - WIN_HEIGHT), y)


        return pygame.Rect(x, y, w, h)