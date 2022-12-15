#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
import player
import level

# Объявляем переменные
TITLE = "Омари"
WIN_WIDTH = 1300
WIN_HEIGHT = 900
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

def main():
    pygame.init()
    window = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption(TITLE)

    bg = pygame.image.load(level.BG_FILE)

    lvl_1 = level.Level()
    entities = pygame.sprite.Group()

    hero = player.Player(55,55)
    timer = pygame.time.Clock()

    for pf in lvl_1.platforms:
        entities.add(pf)
    entities.add(hero)

    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(0)
            hero.move(event)

        window.blit(bg, (0,0))
        hero.update(lvl_1.platforms)
        entities.draw(window)

        pygame.display.update()


if __name__ == "__main__":
    main()
