import pygame
import random
import Enemy_fire as Ef
class Enemy2:
    def __init__(this,Permainan,pos_x,pos_y):
        this.pos_x=pos_x
        this.pos_y=pos_y
        this.fase=1
        this.fase_ledak=0
        this.health=20
        this.permainan=Permainan
        this.gbr1=pygame.image.load("Enemy2/1.png")
        this.gbr2=pygame.image.load("Enemy2/2.png")
        this.gbr1w=pygame.image.load("Enemy2/1w.png")
        this.gbr2w=pygame.image.load("Enemy2/2w.png")
        this.e=pygame.image.load("Enemy2/explode.png")
    def buat_gambar(this):
        if this.health>10:
            if this.fase==1:
                this.permainan.layar.blit(this.gbr1,(this.pos_x,this.pos_y))
            elif this.fase==2:
                this.permainan.layar.blit(this.gbr2,(this.pos_x,this.pos_y))
        elif this.health<=10:
            if this.fase==1:
                this.permainan.layar.blit(this.gbr1w,(this.pos_x,this.pos_y))
            elif this.fase==2:
                this.permainan.layar.blit(this.gbr2w,(this.pos_x,this.pos_y))
        this.fase+=1
        if this.fase>2:
            this.fase=1
        ubah_posisi=random.randint(0,3)
        if ubah_posisi==1:
            if this.pos_x>2:
                this.pos_x-=1
        if ubah_posisi==2:
            if this.pos_x<480:
                this.pos_x+=1    
        this.pos_y+=0.25
    def cek_tembakan(this,Permainan):
        for tembakan in Permainan.hero_fire:
            min_tem_x=tembakan.pos_x
            max_tem_x=tembakan.pos_x+5
            min_tem_y=tembakan.pos_y
            max_tem_y=tembakan.pos_y+5
            min_en_y=this.pos_y
            max_en_y=this.pos_y+30
            min_en_x=this.pos_x+10
            max_en_x=this.pos_x+40
            if (min_tem_x>=min_en_x and min_tem_x<=max_en_x) or (max_tem_x>=min_en_x and max_tem_x<=max_en_x):
                if (min_tem_y>=min_en_y and min_tem_y<=max_en_y) or (max_tem_y>=min_en_y and max_tem_y<=max_en_y):
                    Permainan.hero_fire.pop(0)
                    this.health-=1
                    if this.health==0:
                        if this in Permainan.musuh:
                            if this.fase_ledak==0:
                                this.fase_ledak=1
                            if this.fase_ledak==1:
                                this.permainan.layar.blit(this.e,(this.pos_x,this.pos_y))
                                Permainan.musuh.remove(this)
        
