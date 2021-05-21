import pygame
import random
import Hero as F_Hero
import Enemy as Fe
import Mini_boss as Mb
import Hero_fire as F_Hero_fire
import Enemy_fire as Ef
import Key_command as Kc
import time
class Permainan:
    def reset_menu(this):
        this.intermission={
            "hangar":False,
            "preparation":True
        }
    def enemy_parameter(this):
        this.enemy_health=10
        this.mini_boss_health=200
        this.executor_health=15
    def __init__(this,panjang,lebar):
        pygame.init()
        this.intermission={}
        this.reset_menu()
        this.enemy_remaining=10
        this.pause=False
        this.enemy_parameter()
        this.panjang=panjang
        this.lebar=lebar
        this.layar=pygame.display.set_mode((this.panjang,this.lebar))
        pygame.font.init()
        this.duel_enemy=Fe.Enemy_duel(this,5,9,200)
        pygame.display.set_caption("Space Shooter")
        ikon=pygame.image.load("hero.png")
        pygame.display.set_icon(ikon)
        this.selesai=False
        this.hr=F_Hero.Hero(this,3,400)
        this.musuh=[]
        this.hitung=0
        this.mini_boss=[]
        this.executor=[]
        this.hero_fire=[]
        this.enemy_fire=[]
        this.waktu=pygame.time.Clock()
        this.skor=100
        this.base_health=100
        this.font_tl=pygame.font.SysFont("freesansbold.ttf",24)
        this.game_over=False
        this.start_game=False
        this.wave=1
        this.tombol_tekan={"Tembak":False}
        this.key_command=[]
        while not this.selesai:  
            this.layar.fill((0,0,0))          
            this.tombol=pygame.key.get_pressed()
            if not this.start_game:
                if(this.intermission["preparation"]):
                    this.preparation()
                elif(this.intermission["hangar"]):
                    this.hangar_menu()
            else:                
                this.defense_mode()
                this.reset_menu()
            pygame.display.flip()
    def hangar_menu(this):        
        this.tombol_tekan={
            "Tembak":False,
            "Repair":False,
            "Forcefield":False,
            "Megabomb":False
            }
        money_amount=this.font_tl.render("Money "+str(this.skor),True,(0,255,255))
        upgrade_health_text=this.font_tl.render("MAX HEALTH = "+str(this.hr.max_health)+" Upgrade Cost= "+str(this.hr.health_up_cost),True,(0,128,128))
        upgrade_firepower_text=this.font_tl.render("FIREPOWER = "+str(this.hr.firepower)+" Upgrade Cost= "+str(this.hr.firepower_up_cost),True,(0,128,128))
        hero_health_text=this.font_tl.render("SHIP HEALTH = "+str(this.hr.health)+" Repair Cost= 10",True,(0,128,128))
        base_health_text=this.font_tl.render("BASE HEALTH = "+str(this.base_health)+" Repair Cost= 20",True,(0,128,128))
        wave_text=this.font_tl.render("Wave "+str(this.wave),True,(0,255,255))
        
        repair_kit_text=this.font_tl.render("REPAIR KIT (allow you to repair craft in mission) = "+str(this.hr.repair_kit)+" Upgrade Cost= "+str(this.hr.repair_kit_cost),True,(0,128,128))
        
        
        this.key_command=[Kc.cmd_intermission_menu(this,50,220),Kc.Lbl_up_fpw(this,60,60),Kc.Lbl_rp_sh(this,60,100),Kc.Lbl_rp_bs(this,60,140),Kc.Lbl_up_hlth(this,60,180),Kc.Lbl_b_repair_kit(this,370,60)]
        this.layar.blit(money_amount,(50,20))
        this.layar.blit(upgrade_firepower_text,(50,40))
        this.layar.blit(hero_health_text,(50,80))
        this.layar.blit(base_health_text,(50,120))
        this.layar.blit(upgrade_health_text,(50,160))

        this.layar.blit(repair_kit_text,(360,40))
        mx,my=pygame.mouse.get_pos()
        for tbl in this.key_command:
            tbl.show_text()
        for kej in pygame.event.get():
            if kej.type==pygame.QUIT:
                this.selesai=True
            if kej.type==pygame.MOUSEBUTTONDOWN:
                if kej.button==1:
                    for tbl in this.key_command:
                        if tbl.rect.collidepoint(mx,my):
                            tbl.ter_klik()
    def preparation(this):
        this.key_command=[Kc.cmd_hangar_menu(this,50,40)]
        this.layar.fill((0,0,0))

        money_amount=this.font_tl.render("Money "+str(this.skor),True,(0,255,255))
        wave_text=this.font_tl.render("Wave "+str(this.wave),True,(0,255,255))        
        help_text=this.font_tl.render("DONT LET ENEMY GO TROUGH OR THEY WILL DAMAGE THE BASE",True,(128,128,128))
        help2_text=this.font_tl.render("BIGGER ENEMY CAN INFLICT MORE DAMAGE",True,(128,128,128))
        mission_text=this.font_tl.render("Destroy "+str(this.enemy_remaining)+" Ship",True,(0,128,128))

        

        this.layar.blit(money_amount,(50,20))
        this.layar.blit(wave_text,(50,100))
        this.layar.blit(help_text,(50,120))
        this.layar.blit(help2_text,(50,140))
        this.layar.blit(mission_text,(50,160))

        
        for tbl in this.key_command:
            tbl.show_text()
        for kejadian in pygame.event.get():
            if kejadian.type==pygame.QUIT:
                this.selesai=True
            if kejadian.type==pygame.MOUSEBUTTONDOWN:
                if kejadian.button==1:
                    mx,my=pygame.mouse.get_pos()
                    for tbl in this.key_command:
                        if tbl.rect.collidepoint(mx,my):
                            tbl.ter_klik()
        if this.tombol[pygame.K_RETURN]:
            this.start_game=True
    def defense_mode(this):
        if this.game_over:
            gameover_text=this.font_tl.render("GAME OVER",True,(0,128,128))
            this.layar.blit(gameover_text,(100,100))
            for kejadian in pygame.event.get():
                if kejadian.type==pygame.QUIT:
                    this.selesai=True
        elif not this.game_over:
            if not this.pause:
                if this.base_health<=0:
                    this.game_over=True
                wave_text=this.font_tl.render("Wave "+str(this.wave),True,(0,255,255))
                enemy_amount_text=this.font_tl.render("Remaining "+str(this.enemy_remaining),True,(0,255,255))
                text=this.font_tl.render(str("Score :")+str(this.skor),True,(0,255,255))
                hero_health=this.font_tl.render(str("Hp :")+str(this.hr.health),True,(0,255,255))
                base_health=this.font_tl.render(str("Base HP :")+str(this.base_health),True,(0,255,255))
                repair_kit=this.font_tl.render(str("Repair Kit[R] :")+str(this.hr.repair_kit),True,(0,255,255))
                kill_remain=this.font_tl.render("Destroy the Remaining Enemy ",True,(0,255,255))
                end=this.font_tl.render("Mission Complete ",True,(0,255,255))
                this.layar.blit(text,(10,10))
                this.layar.blit(hero_health,(10,40))
                this.layar.blit(base_health,(10,60))
                this.layar.blit(enemy_amount_text,(10,80))
                this.layar.blit(repair_kit,(10,120))
                this.layar.blit(wave_text,(10,250))
                if this.enemy_remaining<=0 and len(this.musuh)<=0 and len(this.mini_boss)<=0:
                    this.layar.blit(end,(10,280))
                    this.hitung+=1
                    if(this.hitung>=200):               
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
                        this.hitung=0
                this.hr.pos_x, this.hr.pos_y=pygame.mouse.get_pos()
                if(this.hr.pos_x>this.panjang):
                    this.hr.pos_x=this.panjang
                if(this.hr.pos_x<0):
                    this.hr.pos_x=0
                if(this.hr.pos_y>this.lebar):
                    this.hr.pos_y=this.lebar
                if(this.hr.pos_y<0):
                    this.hr.pos_y=0
                if this.tombol[pygame.K_SPACE] or this.tombol_tekan["Tembak"]:
                    if len(this.hero_fire)<10:
                        this.hero_fire.append(F_Hero_fire.Hero_fire(this,this.hr.pos_x,this.hr.pos_y))
                for kejadian in pygame.event.get():
                    if kejadian.type==pygame.KEYUP:
                        if kejadian.key==pygame.K_r and this.tombol_tekan["Repair"]:
                            this.tombol_tekan["Repair"]=False
                    if kejadian.type==pygame.KEYDOWN:
                        if kejadian.key==pygame.K_r and not this.tombol_tekan["Repair"]:
                            this.tombol_tekan["Repair"]=True
                            this.hr.use_repair_kit()
                        if kejadian.key==pygame.K_p:
                            if this.pause:
                                this.pause=False
                            elif not this.pause:
                                this.pause=True
                    if kejadian.type==pygame.QUIT:
                        this.selesai=True
                    if kejadian.type==pygame.MOUSEBUTTONDOWN:
                        if kejadian.button==1:
                            this.tombol_tekan["Tembak"]=True
                    if kejadian.type==pygame.MOUSEBUTTONUP:
                        if kejadian.button==1:
                            this.tombol_tekan["Tembak"]=False        
                this.hr.buat_gambar()
                this.hr.cek_tembakan(this)
                this.waktu.tick(120)
                muncul_musuh=random.randint(0,100)
                muncul_mini_boss=random.randint(0,1000)
                if muncul_musuh==20 and this.enemy_remaining>0:
                    pos_musuh=random.randint(5,this.panjang)
                    this.musuh.append(Fe.Enemy(this,pos_musuh,0,this.enemy_health))
                if muncul_mini_boss==2 and this.enemy_remaining>0:
                    pos_musuh=random.randint(5,this.panjang)
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
                if this.enemy_remaining<=0:
                    this.layar.blit(kill_remain,(10,200))
            else:
                for kejadian in pygame.event.get():
                    if kejadian.type==pygame.KEYDOWN:
                        if kejadian.key==pygame.K_p:
                            if this.pause:
                                this.pause=False
                            elif not this.pause:
                                this.pause=True
                pause_text=this.font_tl.render("Pause ",True,(0,255,255))
                this.layar.blit(pause_text,(200,200))
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

Permainan(1000,500)

