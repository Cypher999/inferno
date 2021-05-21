import pygame
import random
class Enemy_fire:
    def __init__(this,Permainan,pos_x,pos_y):
        this.pos_x=pos_x+20
        this.pos_y=pos_y
        this.permainan=Permainan
        cek_power=random.randint(0,10)
        if cek_power==5:
            this.power=5
        else:
            this.power=1
    def buat_gambar(this):
        if this.power==1:
            pygame.draw.rect(this.permainan.layar,(0,255,255),pygame.Rect(this.pos_x,this.pos_y,5,5))
        elif this.power==5:
            pygame.draw.rect(this.permainan.layar,(0,100,255),pygame.Rect(this.pos_x,this.pos_y,5,5))
        this.pos_y+=1
        
