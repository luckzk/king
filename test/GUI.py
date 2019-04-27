#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :出现图形
#Author      :Michael Jack hu
#start date  : 2019/2/12
#File        : GUI.py
#Software    : PyCharm
#finish date :
'''
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
# app.master.maxsize(1000,400)
app.master.minsize(600,400)

app.mainloop()