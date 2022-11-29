#練習1
import tkinter as tk
root = tk.Tk()
root.title("")
root.geometry("400x600")

#練習3
def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt== "=":
         siki = entry.get() # 数式の文字列
         res = eval(siki) # 数式文字列の評価
         entry.delete(0,tk.END) # 表示文字列の削除
         entry.insert(tk.END,res)
    elif txt == "c":
        entry.delete(0, tk.END)
    elif txt == "÷":
        entry.insert(tk.END, "/")
    elif txt == "x":
        entry.insert(tk.END, "*")
    elif txt == "x²":
        entry.insert(tk.END, "**2")
    elif txt == "√":
        entry.insert(tk.END, "**0.5")
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

#練習5
operators = ["6", "7", "8", "9", "2", "3", "4", "5", "0", "1", "+","=", "-", "÷", "x", "c", "x²", "√"]
for ope in operators:
    button = tk.Button(root, text=f"{ope}", width=4, height=2, font=("", 30))
    button.grid(row=r, column=c)
    button.bind("<1>", button_click)
    c += 1
    if c%4 == 0:
        r += 1
        c = 0
    
root.mainloop()