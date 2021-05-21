import pygame
import random
import Hero as F_Hero
import Enemy as Fe
import Mini_boss as Mb
import Hero_fire as F_Hero_fire
import Enemy_fire as Ef
import time
class Permainan:
    def enemy_parameter(this):
        this.enemy_health=10
        this.mini_boss_health=200
        this.executor_health=15
    def __init__(this,panjang,lebar):
        pygame.init()
        this.enemy_parameter()
        this.layar=pygame.display.set_mode((panjang,lebar))
        pygame.font.init()
        this.duel_enemy=Fe.Enemy_duel(this,5,9,200)
        pygame.display.set_caption("Space Shooter")
        ikon=pygame.image.load("hero.png")
        pygame.display.set_icon(ikon)
        this.selesai=False
        this.hr=F_Hero.Hero(this,3,400)
        this.musuh=[]
        this.mini_boss=[]
        this.executor=[]
        this.hero_fire=[]
        this.enemy_fire=[]
        this.waktu=pygame.time.Clock()
        this.skor=100
        this.base_health=100
        this.font_tl=pygame.font.Font("freesansbold.ttf",12)
        this.game_over=False
        this.start_game=False
        this.tombol_tekan={
            "Tombol_a":False,
            "Tombol_r":False,
            "Tombol_h":False,
            "Tombol_g":False
            }
        this.wave=1
        this.enemy_remaining=10
        while not this.selesai:            
            this.tombol=pygame.key.get_pressed()
            if not this.start_game:
                this.intermission()
            else:                
                this.layar.fill((0,0,0))
                this.run_game()
            pygame.display.flip()
    def intermission(this):
        this.layar.fill((0,0,0))
        wave_text=this.font_tl.render("Wave "+str(this.wave),True,(0,255,255))
        money_amount=this.font_tl.render("Money "+str(this.skor),True,(0,255,255))
        upgrade_health_text=this.font_tl.render("MAX HEALTH (press H to upgrade)  = "+str(this.hr.max_health)+" Upgrade Cost= "+str(this.hr.health_up_cost),True,(0,128,128))
        upgrade_firepower_text=this.font_tl.render("FIREPOWER (press A to upgrade)  = "+str(this.hr.firepower)+" Upgrade Cost= "+str(this.hr.firepower_up_cost),True,(0,128,128))
        hero_health_text=this.font_tl.render("SHIP HEALTH (press R to repair)  = "+str(this.hr.health)+" Repair Cost= 10",True,(0,128,128))
        base_health_text=this.font_tl.render("BASE HEALTH (press g to repair)  = "+str(this.base_health)+" Repair Cost= 20",True,(0,128,128))
        startgame_text=this.font_tl.render("PRESS ENTER TO START",True,(0,128,128))
        help_text=this.font_tl.render("DONT LET ENEMY GO TROUGH OR THEY WILL DAMAGE THE BASE",True,(128,128,128))
        help2_text=this.font_tl.render("BIGGER ENEMY CAN INFLICT MORE DAMAGE",True,(128,128,128))
        mission_text=this.font_tl.render("Destroy "+str(this.enemy_remaining)+" Ship",True,(0,128,128))
        this.layar.blit(money_amount,(100,20))
        this.layar.blit(startgame_text,(100,250))
        this.layar.blit(upgrade_firepower_text,(100,40))
        this.layar.blit(hero_health_text,(100,60))
        this.layar.blit(base_health_text,(100,80))
        this.layar.blit(upgrade_health_text,(100,100))
        this.layar.blit(mission_text,(100,120))
        this.layar.blit(wave_text,(100,140))
        this.layar.blit(help_text,(100,160))
        this.layar.blit(help2_text,(100,180))
        for kejadian in pygame.event.get():
            if kejadian.type==pygame.QUIT:
                this.selesai=True
            if kejadian.type==pygame.KEYDOWN:
                if (kejadian.key==pygame.K_a) and (not (this.tombol_tekan["Tombol_a"])):
                    if this.skor>=this.hr.firepower_up_cost:
                        this.hr.firepower+=0.5
                        this.skor-=this.hr.firepower_up_cost
                        this.hr.firepower_up_cost=int(this.hr.firepower_up_cost)*2
                        this.tombol_tekan["Tombol_a"]=True
                if (kejadian.key==pygame.K_r) and (not (this.tombol_tekan["Tombol_r"])):
                    if this.skor>=10 and this.hr.health<this.hr.max_health:
                        this.hr.health+=1
                        this.skor-=10
                if (kejadian.key==pygame.K_g) and (not (this.tombol_tekan["Tombol_g"])):
                    if this.skor>=20 and this.base_health<100:
                        this.base_health+=1
                        this.skor-=20
                if (kejadian.key==pygame.K_h) and (not (this.tombol_tekan["Tombol_h"])):
                    if this.skor>=this.hr.health_up_cost and this.hr.max_health<100:
                        this.hr.max_health+=5
                        this.skor-=this.hr.health_up_cost
                        this.hr.health=this.hr.max_health
                        this.hr.health_up_cost+=int(this.hr.health_up_cost)*2
            if kejadian.type==pygame.KEYUP:
                if kejadian.key==pygame.K_a and this.tombol_tekan["Tombol_a"]:                            
                    this.tombol_tekan["Tombol_a"]=False
                if kejadian.key==pygame.K_r and this.tombol_tekan["Tombol_r"]:
                    this.tombol_tekan["Tombol_r"]=False
        if this.tombol[pygame.K_RETURN]:
            this.start_game=True
    def run_game(this):
        if this.game_over:
            gameover_text=this.font_tl.render("GAME OVER",True,(0,128,128))
            this.layar.blit(gameover_text,(100,100))
            for kejadian in pygame.event.get():
                if kejadian.type==pygame.QUIT:
                    this.selesai=True
        elif not this.game_over:
            if this.base_health<=0:
                this.game_over=True
            wave_text=this.font_tl.render("Wave "+str(this.wave),True,(0,255,255))
            enemy_amount_text=this.font_tl.render("Remaining "+str(this.enemy_remaining),True,(0,255,255))
            text=this.font_tl.render(str("Score :")+str(this.skor),True,(0,255,255))
            hero_health=this.font_tl.render(str("Hp :")+str(this.hr.health),True,(0,255,255))
            base_health=this.font_tl.render(str("Base HP :")+str(this.base_health),True,(0,255,255))
            this.layar.blit(text,(10,10))
            this.layar.blit(hero_health,(10,40))
            this.layar.blit(base_health,(10,60))
            this.layar.blit(wave_text,(10,100))
            this.layar.blit(enemy_amount_text,(10,80))
            if this.enemy_remaining<=0:
                this.hr.pos_x=3
                this.hr.pos_y=400
                this.musuh=[]
                this.mini_boss=[]
                this.hero_fire=[]
                this.enemy_fire=[]
                this.wave+=1
                this.enemy_remaining=10*int(this.wave)
                this.enemy_health+=5
                this.executor_health+=5
                this.mini_boss_health+=10
                this.start_game=False
            if this.tombol[pygame.K_UP]:
                if this.hr.pos_y>10:
                    this.hr.pos_y-=1.5
            if this.tombol[pygame.K_DOWN]:
                if this.hr.pos_y<480:
                    this.hr.pos_y+=1.5
            if this.tombol[pygame.K_LEFT]:
                if this.hr.pos_x>2:
                    this.hr.pos_x-=1.5
            if this.tombol[pygame.K_RIGHT]:
                if this.hr.pos_x<680:
                    this.hr.pos_x+=1.5
            if this.tombol[pygame.K_SPACE]:
                if len(this.hero_fire)<10:
                    this.hero_fire.append(F_Hero_fire.Hero_fire(this,this.hr.pos_x,this.hr.pos_y))
            for kejadian in pygame.event.get():
                if kejadian.type==pygame.QUIT:
                    this.selesai=True
            this.hr.buat_gambar()
            this.hr.cek_tembakan(this)
            this.waktu.tick(120)
            muncul_musuh=random.randint(0,100)
            muncul_mini_boss=random.randint(0,1000)
            if muncul_musuh==20:
                pos_musuh=random.randint(5,680)
                this.musuh.append(Fe.Enemy(this,pos_musuh,0,this.enemy_health))
            if muncul_mini_boss==2:
                pos_musuh=random.randint(5,680)
                this.mini_boss.append(Mb.Mini_boss(this,pos_musuh,0,this.mini_boss_health))
            for mnb in this.mini_boss:
                mnb.buat_gambar()
                mnb.cek_tembakan(this)
                mulai_tembak=random.randint(0,100)
                if mulai_tembak==5:
                    this.enemy_fire.append(Ef.Enemy_fire(this,mnb.pos_x,mnb.pos_y+20))
                    this.enemy_fire.append(Ef.Enemy_fire(this,mnb.pos_x+20,mnb.pos_y+20))
                    this.enemy_fire.append(Ef.Enemy_fire(this,mnb.pos_x+40,mnb.pos_y+20))
                if mnb.pos_y>=500:
                    this.base_health-=5
                    if mnb in this.mini_boss:
                        this.mini_boss.remove(mnb)
            for msh in this.musuh:
                msh.buat_gambar()                
                mulai_tembak=random.randint(0,100)                
                msh.cek_tembakan(this)
                if mulai_tembak==5:
                    this.enemy_fire.append(Ef.Enemy_fire(this,msh.pos_x,msh.pos_y))
                if msh.pos_y>=500:
                    this.base_health-=1
                    if msh in this.musuh:
                        this.musuh.remove(msh)
            for en_fr in this.enemy_fire:
                en_fr.buat_gambar()
                if en_fr.pos_y>500:
                    this.enemy_fire.remove(en_fr)
            for hr_fr in this.hero_fire:
                hr_fr.buat_gambar()
                if hr_fr.pos_y<=0:
                    this.hero_fire.remove(hr_fr)
    def duel_mode(this):
        
        if this.game_over:
            gameover_text=this.font_tl.render("GAME OVER",True,(0,128,128))
            this.layar.blit(gameover_text,(100,100))
            for kejadian in pygame.event.get():
                if kejadian.type==pygame.QUIT:
                    this.selesai=True
        elif not this.game_over:            
            wave_text=this.font_tl.render("Enemy's HP "+str(this.duel_enemy.health),True,(0,255,255))
            enemy_amount_text=this.font_tl.render("Remaining "+str(this.enemy_remaining),True,(0,255,255))
            text=this.font_tl.render(str("Score :")+str(this.skor),True,(0,255,255))
            hero_health=this.font_tl.render(str("Hp :")+str(this.hr.health),True,(0,255,255))
            base_health=this.font_tl.render(str("Base HP :")+str(this.base_health),True,(0,255,255))
            this.layar.blit(text,(10,10))
            this.layar.blit(hero_health,(10,40))
            this.layar.blit(base_health,(10,60))
            this.layar.blit(wave_text,(10,100))
            this.layar.blit(enemy_amount_text,(10,80))
            if this.tombol[pygame.K_UP]:
                if this.hr.pos_y>10:
                    this.hr.pos_y-=1
            if this.tombol[pygame.K_DOWN]:
                if this.hr.pos_y<480:
                    this.hr.pos_y+=1
            if this.tombol[pygame.K_LEFT]:
                if this.hr.pos_x>2:
                    this.hr.pos_x-=1
            if this.tombol[pygame.K_RIGHT]:
                if this.hr.pos_x<680:
                    this.hr.pos_x+=1
            if this.tombol[pygame.K_SPACE]:
                if len(this.hero_fire)<10:
                    this.hero_fire.append(F_Hero_fire.Hero_fire(this,this.hr.pos_x,this.hr.pos_y))
            for kejadian in pygame.event.get():
                if kejadian.type==pygame.QUIT:
                    this.selesai=True
            this.hr.buat_gambar()
            this.hr.cek_tembakan(this)
            this.waktu.tick(120)
            this.duel_enemy.buat_gambar()                
            mulai_tembak=random.randint(0,50)                
            this.duel_enemy.cek_tembakan(this)
            if mulai_tembak==5:
                this.enemy_fire.append(Ef.Enemy_fire(this,this.duel_enemy.pos_x,this.duel_enemy.pos_y))
            if this.duel_enemy.pos_y>=500:
                this.base_health-=1
            for en_fr in this.enemy_fire:
                en_fr.buat_gambar()
                if en_fr.pos_y>500:
                    this.enemy_fire.remove(en_fr)
            for hr_fr in this.hero_fire:
                hr_fr.buat_gambar()
                if hr_fr.pos_y<=0:
                    this.hero_fire.remove(hr_fr)            

Permainan(700,500)
