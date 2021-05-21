import pygame as py_g

class Lbl_up_fpw:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        this.text=this.game.font_tl.render("Upgrade Firepower",True,(0,128,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.hr.upgrade_firepower()

class cmd_hangar_menu:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        this.text=this.game.font_tl.render("Open Hangar",True,(0,128,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.intermission["hangar"]=True
        this.game.intermission["preparation"]=False

class cmd_intermission_menu:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        this.text=this.game.font_tl.render("Back to preparation",True,(0,128,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.intermission["hangar"]=False
        this.game.intermission["preparation"]=True


class Lbl_b_repair_kit:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        if(this.game.hr.repair_kit<5):            
            this.text=this.game.font_tl.render("Buy repair kit",True,(0,128,255))
        elif(this.game.hr.repair_kit>=1):
            this.text=this.game.font_tl.render("Maxed",True,(0,255,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.hr.buy_repair_kit()

class Lbl_b_forcefield:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        if(this.game.hr.forcefield<1):
            this.text=this.game.font_tl.render("Buy Forcefield",True,(0,128,255))
        elif(this.game.hr.forcefield>=1):
            this.text=this.game.font_tl.render("Maxed",True,(0,255,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.hr.buy_forcefield()

class Lbl_b_megabomb:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        if(this.game.hr.mega_bomb<1):            
            this.text=this.game.font_tl.render("Buy Megabomb",True,(0,128,255))
        elif(this.game.hr.mega_bomb>=1):
            this.text=this.game.font_tl.render("Maxed",True,(0,255,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.hr.buy_megabomb()

        
class Lbl_up_hlth:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        this.text=this.game.font_tl.render("Upgrade Health",True,(0,128,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.hr.upgrade_health()

class Lbl_rp_sh:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        this.text=this.game.font_tl.render("Repair Ship",True,(0,128,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.hr.repair_ship()

class Lbl_rp_bs:
    def __init__(this,game,x,y):
        this.game=game
        this.x=x
        this.y=y
    def show_text(this):
        this.text=this.game.font_tl.render("Repair Base",True,(0,128,255))
        this.game.layar.blit(this.text,(this.x,this.y))
        this.panjang, this.lebar=this.text.get_size()
        this.rect=py_g.Rect(this.x,this.y,this.panjang,this.lebar)
    def ter_klik(this):
        this.game.hr.repair_base()

                
