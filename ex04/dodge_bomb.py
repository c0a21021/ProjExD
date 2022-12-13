import pygame as pg
import sys
import random
import datetime

def check_bound(obj_rct, scr_rct):
        #第1引数:こうかとんrectまたは爆弾rect
        #第2引数:スクリーンrect
        #範囲内:+1, 範囲外:-1
        yoko, tate = +1, +1
        if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
            yoko = -1
        if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
            tate = -1
        return yoko, tate

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「逃げろ!こうかとん」と表示する
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

    #追加するボールの設定
    bomb2_sfc = pg.Surface((20,20)) #正方形の空のserface
    bomb2_sfc.set_colorkey(0, 0)
    pg.draw.circle(bomb2_sfc, (0, 0, 255), (10, 10), 10)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0,scrn_rct.width)
    bomb2_rct.centerx = random.randint(0,scrn_rct.height)

    #追加するボールの設定2
    bomb3_sfc = pg.Surface((20,20)) #正方形の空のserface
    bomb3_sfc.set_colorkey(0, 0)
    pg.draw.circle(bomb3_sfc, (255, 0, 0), (10, 10), 10)
    bomb3_rct = bomb3_sfc.get_rect()
    bomb3_rct.centerx = random.randint(0,scrn_rct.width)
    bomb3_rct.centerx = random.randint(0,scrn_rct.height)


    #練習2
    vx, vy = +1, +1
    v2x, v2y = +1, +1
    v3x, v3y = +1, +1
    flag = False #追加した爆弾に当たったか
    stime = datetime.datetime.now() #ゲーム開始時の時間を取得
    clock = pg.time.Clock()
    while True:
        etime = datetime.datetime.now() #現在時間を随時更新
        scrn_sfc.blit(pgbg_sfc, pgbg_rect) #現在の時間とゲーム開始時の時間の差分を計算
        if (etime - stime).seconds > 5: #ゲーム開始5秒経ったら青い爆弾を追加
            bomb2_rct.move_ip(v2x, v2y)
            yoko2, tate2 = check_bound(bomb2_rct, scrn_rct)
            v2x *= yoko2
            v2y *= tate2
            scrn_sfc.blit(bomb2_sfc,bomb2_rct)

        #練習4
        key_dict = pg.key.get_pressed() #辞書型
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1

        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            #どこかしらがはみ出していたら
            if key_dict[pg.K_UP]:
                tori_rct.centery += 1
            if key_dict[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dict[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dict[pg.K_RIGHT]:
                tori_rct.centerx -= 1            
        scrn_sfc.blit(tori_sfc, tori_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        
        
        #練習8
        if tori_rct.colliderect(bomb_rct):
            return
        if tori_rct.colliderect(bomb2_rct):
            flag = True
        
        if tori_rct.colliderect(bomb3_rct):
            return

        if flag == True: #青い爆弾に当たった時の処理
            bomb3_rct.move_ip(v3x, v3y)
            yoko3, tate3 = check_bound(bomb3_rct, scrn_rct)
            v3x *= yoko3
            v3y *= tate3
            scrn_sfc.blit(bomb3_sfc,bomb3_rct)

        pg.display.update()
        clock.tick(1000)

if __name__ == '__main__':
    main()
    pg.init()
    pg.quit()
    sys.exit()