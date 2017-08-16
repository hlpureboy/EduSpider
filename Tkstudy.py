# -*- coding: utf-8 -*-
import tkinter as tk
def insert_point():
    var=e.get()
    t.insert('insert',var)
root=tk.Tk()
root.title('welcome tkinter')
root.geometry('200x100')
e=tk.Entry(root,show=None,)
e.pack()
b=tk.Button(root,text='insert point',command=insert_point)
b.pack()
t=tk.Text(root,height=2)
t.pack()
root.mainloop()