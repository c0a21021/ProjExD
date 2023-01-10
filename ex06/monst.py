import os
import pygame as pg
import random
import sys


speedFlag = False


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 

    
class Bird:
    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path) 
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio) 
        self.rct = self.sfc.get_rect()
        self.rct.center = xy 

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.blit(scr)


class Character:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, (255, 0, 0), (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 100
        self.rct.centery = 800
        self.vx, self.vy = vxy
        self.sx = -0.01
        self.sy = -0.01

       
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen, speed):
        global speedFlag
        if speed:
            self.rct.move_ip(self.vx, self.vy)
            yoko, tate = check_bound(self.rct, scr.rct)
            if abs(self.vx) >= abs(self.sx):
                self.vx += self.sx
                self.vy += self.sy
            else:
                speedFlag = False
                if self.vx > 0:
                    self.vx = 10
                elif self.vx < 0:
                    self.vx = -10
                if self.vy > 0:
                    self.vy = 10
                elif self.vy < 0:
                    self.vy = -10
            self.vx *= yoko
            self.vy *= tate
            self.sx *= yoko
            self.sy *= tate
        self.blit(scr)



main_dir = os.path.split(os.path.abspath(__file__))[0]

def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    global speedFlag
    clock =pg.time.Clock()
    #hansyaFlag = False #キャラと敵が当たった場合の判定Flag

    #練習1
    scr = Screen("引っ張りハンティング", (1600, 900), "fig/pg_bg.jpg")

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    kkt.update(scr)
    chara = Character((255, 0, 0), 10, (+1, +1), scr)

    # 練習５
    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
            if event.type == pg.MOUSEBUTTONDOWN and speedFlag == False:
                speedFlag = True
        kkt.blit(scr)
        if speedFlag:
            chara.update(scr, True)
        else:
            chara.update(scr, False) 

        #キャラとこうかとんの当たり判定
        if kkt.rct.colliderect(chara.rct):
            chara.vx *= -1
            chara.vy *= -1
            chara.sx *= -1
            chara.sy *= -1
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
