import tkinter as tk
import maze_maker as mm
import random
def key_down(event):
    global key, maze_list, cx, cy, canvas, mx, my
    key = event.keysym
    if key == "r":
         maze_list = mm.make_maze(15, 9)
         mm.show_maze(canvas, maze_list)    
         mx, my = 1, 1
         cx, cy = mx * 100 + 50, my * 100 + 50
         canvas.delete("koukaton") #こうかとんの位置を初期化するために画像を再設定するために現在の画像の再設定を行う
         canvas.create_image(cx, cy, image = koukaton, tag = "koukaton") #画像を再設定する
    else:
        pass  
        
def key_up(event):
    global key
    key = ""

def main_prock():
    global cx, cy, mx, my, canvas, mazelist
    if key == "Up": my -= 1
    elif key == "Down": my += 1
    elif key == "Right": mx += 1
    elif key == "Left": mx -= 1
        
    if maze_list[mx][my] == 1: #こうかとんの移動先が壁だったら
        if key == "Up": my += 1
        elif key == "Down": my-= 1
        elif key == "Right": mx -= 1
        elif key == "Left": mx += 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_prock)

  

if __name__ == '__main__':
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()

    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)
    koukaton = tk.PhotoImage(file = "./fig/8.png")
    mx, my = 1, 1
    cx, cy = mx * 100 + 50, my * 100 + 50
    canvas.create_image(cx, cy, image = koukaton, tag = "koukaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_prock()


    #実装できなかった部分
    ''''  
    wx, wy = random.randint(1, 5)*100, random.randint(1, 5)*100
    wwx, wwy = random.randint(1, 5)*100, random.randint(1, 5)*100
    canvas.create_rectangle(wx, wy, wx+100, wy+100, fill = "yellow")
    canvas.create_rectangle(wwx, wwy, wwx+100, wwy+100, fill = "yellow")
    '''

    root.mainloop()