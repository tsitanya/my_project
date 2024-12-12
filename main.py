#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
import player
import level
import camera
import time 
import monster

TITLE = "ВАНЬКА"
player.Player.start_time = time.time()



def main():

    pygame.init()
    window = pygame.display.set_mode(camera.DISPLAY)
    pygame.display.set_caption(TITLE)

    bg = pygame.image.load(level.BG_FILE)


    lvl_1 = level.Level()
    entities = pygame.sprite.Group()
    animatet_antitis = pygame.sprite.Group()
    monsters = pygame.sprite.Group()

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

    pr = level.platform.prise(55, 765)
    animatet_antitis.add(pr)
    entities.add(pr)
    lvl_1.platforms.append(pr)

    # tp_1 = level.platform.TeleportBlock(770, 280, 860, 240)
    # animatet_antitis.add(tp_1)
    # entities.add(tp_1)
    # lvl_1.platforms.append(tp_1)

    mn = player.monster.Monster(200, 765, 2, 0, 700, 765)
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


main()
