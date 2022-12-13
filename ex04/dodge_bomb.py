import pygame as pg
import sys

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「初めてのPyGame」と表示する
    scrn_sfc = pg.display.set_mode((1600,900))
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rect = pgbg_sfc.get_rect()

    #練習3
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct  = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) #scrn_sfcにtori_rctに従って、tori_sfcを貼り付ける


    #練習2
    while True:
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
        pg.display.update()

if __name__ == '__main__':
    main()
    pg.init()
    pg.quit()
    sys.exit()