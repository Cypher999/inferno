import pygame
import random
class Mini_boss:
    def __init__(this,Permainan,pos_x,pos_y,health):
        this.pos_x=pos_x
        this.pos_y=pos_y
        this.fase=1
        this.fase_ledak=0
        this.health=health
        this.permainan=Permainan
        this.gbr1=pygame.image.load("Mini_Boss/1.png")
        this.gbr2=pygame.image.load("Mini_Boss/2.png")
        this.gbr3=pygame.image.load("Mini_Boss/3.png")
        this.gbr1w=pygame.image.load("Mini_Boss/1w.png")
        this.gbr2w=pygame.image.load("Mini_Boss/2w.png")
        this.gbr3w=pygame.image.load("Mini_Boss/3w.png")
        this.e=pygame.image.load("Enemy2/explode.png")
    def buat_gambar(this):
        if this.health>10:
            if this.fase==1:
                this.permainan.layar.blit(this.gbr1,(this.pos_x,this.pos_y))
            elif this.fase==2:
                this.permainan.layar.blit(this.gbr2,(this.pos_x,this.pos_y))
            elif this.fase==3:
                this.permainan.layar.blit(this.gbr3,(this.pos_x,this.pos_y))
        elif this.health<=50:
            if this.fase==1:
                this.permainan.layar.blit(this.gbr1w,(this.pos_x,this.pos_y))
            elif this.fase==2:
                this.permainan.layar.blit(this.gbr2w,(this.pos_x,this.pos_y))
            elif this.fase==3:
                this.permainan.layar.blit(this.gbr3w,(this.pos_x,this.pos_y))
        this.fase+=1
        if this.fase>3:
            this.fase=1
        ubah_posisi=random.randint(0,3)
        if ubah_posisi==1:
            if this.pos_x>2:
                this.pos_x-=5
        if ubah_posisi==2:
            if this.pos_x<300:
                this.pos_x+=5
        this.pos_y+=0.125
    def cek_tembakan(this,Permainan):
        for tembakan in Permainan.hero_fire:
            min_tem_x=tembakan.pos_x
            max_tem_x=tembakan.pos_x+5
            min_tem_y=tembakan.pos_y
            max_tem_y=tembakan.pos_y+5
            min_en_y=this.pos_y
            max_en_y=this.pos_y+100
            min_en_x=this.pos_x
            max_en_x=this.pos_x+150
            if (min_tem_x>=min_en_x and min_tem_x<=max_en_x) or (max_tem_x>=min_en_x and max_tem_x<=max_en_x):
                if (min_tem_y>=min_en_y and min_tem_y<=max_en_y) or (max_tem_y>=min_en_y and max_tem_y<=max_en_y):
                    this.health-=Permainan.hr.firepower
                    Permainan.hero_fire.pop(0)
                    if this.health<=0:                        
                            Permainan.enemy_remaining-=2
                            this.permainan.layar.blit(this.e,(this.pos_x,this.pos_y))
                            if this in Permainan.mini_boss:
                                Permainan.mini_boss.remove(this)
                            Permainan.skor+=50
        
