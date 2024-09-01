#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.isTouchingTop = False
        self.isTouchingBottom = False

    def move(self):
        match (self.name):
            case 'Enemy3':
                self.rect.centerx -= ENTITY_SPEED[self.name]

                if self.isTouchingBottom:
                    self.rect.centery -= ENTITY_SPEED[self.name]
                    if self.rect.centery <= 0:
                        self.isTouchingTop = True
                        self.isTouchingBottom = False

                elif self.isTouchingTop:
                    self.rect.centery += ENTITY_SPEED[self.name] * 2
                    if self.rect.centery >= WIN_HEIGHT:
                        self.isTouchingTop = False
                        self.isTouchingBottom = True
                else:
                    self.rect.centery += ENTITY_SPEED[self.name]
                    if self.rect.bottom >= WIN_HEIGHT:
                        self.isTouchingBottom = True





            case _:
                self.rect.centerx -= ENTITY_SPEED[self.name]


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
