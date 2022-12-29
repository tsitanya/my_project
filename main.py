#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
import player
import level
import camera

TITLE = "мариo"


def main():
    pygame.init()
    window = pygame.display.set_mode(camera.DISPLAY)
    pygame.display.set_caption(TITLE)

    bg = pygame.image.load(level.BG_FILE)

    lvl_1 = level.Level()
    entities = pygame.sprite.Group()
    animatet_antitis = pygame.sprite.Group()


    hero = player.Player(55, 55)
    timer = pygame.time.Clock()

    main_camera = camera.Camera(lvl_1.width, lvl_1.haght)

    for pf in lvl_1.platforms:
        entities.add(pf)
    entities.add(hero)

    tp = level.platform.TeleportBlock(1250, 470, 900, 750)
    animatet_antitis.add(tp)
    entities.add(tp)
    lvl_1.platforms.append(tp)

    tp_1 = level.platform.TeleportBlock(770, 280, 860, 240)
    animatet_antitis.add(tp_1)
    entities.add(tp_1)
    lvl_1.platforms.append(tp_1)

    tp_2 = level.platform.TeleportBlock(1700, 32, 2020, 750)
    animatet_antitis.add(tp_2)
    entities.add(tp_2)
    lvl_1.platforms.append(tp_2)

    tp_3 = level.platform.TeleportBlock(2020, 670, 2019, 530)
    animatet_antitis.add(tp_3)
    entities.add(tp_3)
    lvl_1.platforms.append(tp_3)

#    tp_h = level.platform.TeleportBlock(120, 40, 500, 750)
 #   animatet_antitis.add(tp_h)
  #  entities.add(tp_h)
   # lvl_1.platforms.append(tp_h)

    tp_h_1 = level.platform.TeleportBlock(120, 40, 50, 1100)
    animatet_antitis.add(tp_h_1)
    entities.add(tp_h_1)
    lvl_1.platforms.append(tp_h_1)

    tp_5 = level.platform.TeleportBlock(3450, 90, 3600, 750)
    animatet_antitis.add(tp_5)
    entities.add(tp_5)
    lvl_1.platforms.append(tp_5)

    tp_6 = level.platform.TeleportBlock(4192, 159, 50, 1100)
    animatet_antitis.add(tp_6)
    entities.add(tp_6)
    lvl_1.platforms.append(tp_6)

    monsters = pygame.sprite.Group()
    mn = player.monster.Monster(700, 765, 2, 2, 150, 0)
    entities.add(mn)
    monsters.add(mn)
    lvl_1.platforms.append(mn)

    monsters = pygame.sprite.Group()
    mn = player.monster.Monster(250, 1150, 2, 2, 150, 0)
    entities.add(mn)
    monsters.add(mn)
    lvl_1.platforms.append(mn)

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


        monsters.update(lvl_1.platforms)
        animatet_antitis.update()
        pygame.display.update()


if __name__ == "__main__":
    main()
