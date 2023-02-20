import tkinter as tk

calculation = ""

def add(symbol):
    global calculation
    calculation += str(symbol)
    text_res.delete(1.0, "end")
    text_res.insert(1.0, calculation)


def evalute():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_res.delete(1.0, "end")
        text_res.insert(1.0, calculation)
    except:
        clear()
        text_res.inesrt(1.0, "Error")

def clear():
    global calculation
    calculation = ""
    text_res.delete(1.0, "end")


root = tk.Tk()
root.geometry("275x280")

text_res = tk.Text(root, height=2, width=14, font=("Arial", 24))
text_res.grid(columnspan=5)

BTN1 = tk.Button(root,text="1",command=lambda : add(1),width=4, font=("Arial",14))
BTN1.grid(row=2,column=1)
BTN2 = tk.Button(root,text="2",command=lambda : add(2),width=4, font=("Arial",14))
BTN2.grid(row=2,column=2)
BTN3 = tk.Button(root,text="3",command=lambda : add(3),width=4, font=("Arial",14))
BTN3.grid(row=2,column=3)
BTN4 = tk.Button(root,text="4",command=lambda : add(4),width=4, font=("Arial",14))
BTN4.grid(row=3,column=1)
BTN5 = tk.Button(root,text="5",command=lambda : add(5),width=4, font=("Arial",14))
BTN5.grid(row=3,column=2)
BTN6 = tk.Button(root,text="6",command=lambda : add(6),width=4, font=("Arial",14))
BTN6.grid(row=3,column=3)
BTN7 = tk.Button(root,text="7",command=lambda : add(7),width=4, font=("Arial",14))
BTN7.grid(row=4,column=1)
BTN8 = tk.Button(root,text="8",command=lambda : add(8),width=4, font=("Arial",14))
BTN8.grid(row=4,column=2)
BTN9 = tk.Button(root,text="9",command=lambda : add(9),width=4, font=("Arial",14))
BTN9.grid(row=4,column=3)
BTN10 = tk.Button(root,text="0",command=lambda : add(0),width=4, font=("Arial",14))
BTN10.grid(row=5,column=2)
BTN11 = tk.Button(root,text="(",command=lambda : add("("),width=4, font=("Arial",14))
BTN11.grid(row=5,column=1)
BTN12 = tk.Button(root,text=")",command=lambda : add(")"),width=4, font=("Arial",14))
BTN12.grid(row=5,column=3)
BTN13 = tk.Button(root,text="+",command=lambda : add("+"),width=4, font=("Arial",14))
BTN13.grid(row=2,column=4)
BTN14 = tk.Button(root,text="-",command=lambda : add("-"),width=4, font=("Arial",14))
BTN14.grid(row=3,column=4)
BTN15 = tk.Button(root,text="*",command=lambda : add("*"),width=4, font=("Arial",14))
BTN15.grid(row=4,column=4)
BTN16 = tk.Button(root,text="/",command=lambda : add("/"),width=4, font=("Arial",14))
BTN16.grid(row=5,column=4)
BTN17 = tk.Button(root,text="C",command=clear, font=("Arial",14))
BTN17.grid(row=1,column=1)
BTN18 = tk.Button(root,text="=",command=evalute,width=4, font=("Arial",14))
BTN18.grid(row=1,column=4)

root.mainloop()