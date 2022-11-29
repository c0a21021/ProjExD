#練習1
import tkinter as tk
import tkinter.messagebox as tkm
root = tk.Tk()
root.title("")
root.geometry("300x500")

#練習3
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt== "=":
         siki = entry.get() # 数式の文字列
         res = eval(siki) # 数式文字列の評価
         entry.delete(0,tk.END) # 表示文字列の削除
         entry.insert(tk.END,res)
    else:
        entry.insert(tk.END,txt)
    #tkm.showinfo("押すな", f"{txt}のボタンが押されました")

#練習4
entry = tk.Entry(justify = "right", width = 10, font = ("", 40))
#練習6
#entry.insert(tk.END, "")
entry.grid(row = 0, column =0, columnspan = 3)


#練習2
r, c = 1,0
for num in range(9, -1, -1):
    button = tk.Button(root, text =f"{num}", width = 4, height = 2, font=("", 30))
    button.bind("<1>", button_click)
    button.grid(row =r, column = c)
    c+=1
    if c%3 == 0:
        r += 1
        c = 0

#練習5
operators = ["+","="]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%3 == 0:
        r += 1
        c = 0
    
root.mainloop()