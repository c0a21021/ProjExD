import pygame as pg
import sys
import random

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「初めてのPyGame」と表示する
    scrn_sfc = pg.display.set_mode((1600,900))
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    scrn_rct = scrn_sfc.get_rect()
    pgbg_rect = pgbg_sfc.get_rect()

    #練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct  = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) #scrn_sfcにtori_rctに従って、tori_sfcを貼り付ける

    #練習5
    bomb_sfc = pg.Surface((20,20)) #正方形の空のserface
    bomb_sfc.set_colorkey(0, 0)

    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_rct.centerx = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(bomb_sfc,bomb_rct)
    




    #練習2
    while True:
        clock = pg.time.Clock()
        scrn_sfc.blit(pgbg_sfc, pgbg_rect)

        #練習4
        key_dict = pg.key.get_pressed() #辞書型
        if key_dict[pg.K_UP] == True:
            tori_rct.centery -= 1
        elif key_dict[pg.K_DOWN] == True:
            tori_rct.centery += 1
        elif key_dict[pg.K_LEFT] == True:
            tori_rct.centerx -= 1
        elif key_dict[pg.K_RIGHT] == True:
            tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        
        vx, vy = +1, +1
        bomb_rct.move_ip(vx, vy)
        pg.display.update()
        clock.tick(1000)

if __name__ == '__main__':
    main()
    pg.init()
    pg.quit()
    sys.exit()