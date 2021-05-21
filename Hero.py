import pygame
class Hero:
    def __init__(this,Permainan,pos_x,pos_y):
        this.pos_x=pos_x
        this.pos_y=pos_y
        this.permainan=Permainan
        this.gbr=pygame.image.load("hero.png")
        this.health=10
        this.max_health=10
        this.firepower=1
        this.firepower_up_cost=10
        this.health_up_cost=100
        this.repair_kit=2
        this.repair_kit_cost=20
        this.forcefield_cost=400
        this.mega_bomb_cost=750
        this.forcefield=0
        this.mega_bomb=0
        #this.suara_tembakan=pygame.mixer.Sound("sound/hero_shot.wav")
    def buat_gambar(this):
        this.permainan.layar.blit(this.gbr,(this.pos_x,this.pos_y))
    def use_repair_kit(this):
        if(this.health<this.max_health) and(this.repair_kit>0):
            this.health+=1
            this.repair_kit-=1
    def upgrade_firepower(this):
        if this.permainan.skor>=this.firepower_up_cost:
            this.firepower=float(this.firepower)+0.5
            this.permainan.skor=int(this.permainan.skor)-int(this.firepower_up_cost)
            this.firepower_up_cost=int(this.firepower_up_cost)*2
    def buy_repair_kit(this):
        if(this.repair_kit<5) and (this.permainan.skor>=this.repair_kit_cost):
            this.repair_kit+=1
            this.permainan.skor=this.permainan.skor-this.repair_kit_cost
    def buy_forcefield(this):
        if(this.forcefield<1) and (this.permainan.skor>=this.forcefield_cost):
            this.forcefield+=1
            this.permainan.skor=this.permainan.skor-this.forcefield_cost
    def buy_megabomb(this):
        if(this.mega_bomb<1) and (this.permainan.skor>=this.mega_bomb_cost):
            this.mega_bomb+=1
            this.permainan.skor=this.permainan.skor-this.mega_bomb_cost
    def upgrade_health(this):
        if this.permainan.skor>=this.health_up_cost:
            this.max_health=int(this.max_health)+5
            this.permainan.skor=int(this.permainan.skor)-int(this.health_up_cost)
            this.health=this.max_health
            this.health_up_cost=int(this.health_up_cost)*2
            
            print(this.max_health)
    def repair_ship(this):
        if this.permainan.skor>=10 and this.health<this.max_health:
            this.health=int(this.health)+1
            this.permainan.skor=int(this.permainan.skor)-10
    def repair_base(this):
        if this.permainan.skor>=10:
            this.health=int(this.health)+1
            this.permainan.skor=int(this.permainan.skor)-20
    def cek_tembakan(this,Permainan):
        for tembakan in Permainan.enemy_fire:
            min_tem_x=tembakan.pos_x
            max_tem_x=tembakan.pos_x+5
            min_tem_y=tembakan.pos_y
            max_tem_y=tembakan.pos_y+5
            min_en_y=this.pos_y
            max_en_y=this.pos_y+30
            min_en_x=this.pos_x+10
            max_en_x=this.pos_x+40
            if this.health<=0:
                Permainan.game_over=True
            if (min_tem_x>=min_en_x and min_tem_x<=max_en_x) or (max_tem_x>=min_en_x and max_tem_x<=max_en_x):
                if (min_tem_y>=min_en_y and min_tem_y<=max_en_y) or (max_tem_y>=min_en_y and max_tem_y<=max_en_y):
                    this.health-=tembakan.power
                    if tembakan in Permainan.enemy_fire:
                        Permainan.enemy_fire.remove(tembakan)
