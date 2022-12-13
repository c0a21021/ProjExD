import pygame as pg
import sys

def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん") #タイトルバーに「初めてのPyGame」と表示する
    scrn_sfc = pg.display.set_mode((1600,900))
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")

    #練習2
    #while True:
     #   for event in pg.event.get

if __name__ == '__main__':
    main()
    pg.init()
    pg.quit()
    sys.exit()