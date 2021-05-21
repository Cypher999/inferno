import pygame
import random
class Hero_fire:
    def __init__(this,Permainan,pos_x,pos_y):
        this.pos_x=pos_x+20
        this.pos_y=pos_y
        this.permainan=Permainan
    def buat_gambar(this):
        pygame.draw.rect(this.permainan.layar,(0,255,255),pygame.Rect(this.pos_x,this.pos_y,5,5))
        this.pos_y-=10
        
