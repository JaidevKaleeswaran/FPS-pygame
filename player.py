from settings import *
import pygame as pg
import math

class PLayer:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0,0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dy += speed_sin
            dy += speed_cos
        if keys[pg.K_s]:
            dy += -speed_sin
            dy += -speed_cos
        if keys[pg.K_a]:
            dy += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dy += -speed_sin
            dy += speed_cos

        self.x = dx
        self.y = dy

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time

        self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                    (self.X * 100 + WIDTH * math.cos(self.angle), 
                     self.Y * 100 + WIDTH * math.sin(self.angle)),2)     
        pg.draw.line(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)        

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)        