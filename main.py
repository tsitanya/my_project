#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
import player
import level
import camera

# Объявляем переменные
TITLE = "Омари"


def main():
    pygame.init()
    window = pygame.display.set_mode(camera.DISPLAY)
    pygame.display.set_caption(TITLE)

    bg = pygame.image.load(level.BG_FILE_3)

    lvl_1 = level.Level()
    entities = pygame.sprite.Group()

    hero = player.Player(55, 55)
    timer = pygame.time.Clock()

    main_camera = camera.Camera(lvl_1.width, lvl_1.haght)

    for pf in lvl_1.platforms:
        entities.add(pf)
    entities.add(hero)

    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(0)
            hero.move(event)

        window.blit(bg, (0, 0))
        hero.update(lvl_1.platforms)
        main_camera.apdate(hero)

        for entitie in entities:
            window.blit(entitie.image, main_camera.apply(entitie))

        pygame.display.update()


if __name__ == "__main__":
    main()
