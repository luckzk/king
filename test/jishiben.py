#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2019/2/23
#File        : jishiben.py
#Software    : PyCharm
#finish date :
'''

import tkinter as tk
from tkinter import messagebox,filedialog
import os


root = tk.Tk()
root.title('ben')

root.geometry('600x400+600+200')

#statusbar
status = tk.Label(root,text = 'Ln20',bd = 1,relief = tk.SUNKEN,anchor = 'w')
status.pack(side = tk.BOTTOM,fill = tk.X)

#-------菜单--------
me = tk.Menu(root)

root.config(menu=me)


#文件菜单
filemenu = tk.Menu(me)
filemenu.add_command(label='new',accelerator='Ctrl + N')
filemenu.add_command(label='open',accelerator='Ctrl + O')
filemenu.add_command(label='save',accelerator='Ctrl + S')
filemenu.add_command(label='save as',accelerator='Ctrl + A')
me.add_cascade(label = '文件',menu = filemenu)

#新建
def new():
    root.title('未命名文件')
    filename = None
    textpad.delete(1.0,tk.END)
#打开
def openfile():
    global filename
    filename = filedialog.askopenfilename(defaultextension = '.txt')
    if filename == '':
        filename = None
    else:
        root.title('FileName:'+os.path.basename(filename))
        textpad.delete(1.0,tk.END)
        f = open(filename,'r')
        textpad.insert(1.0,f.read())
        f.close()

#保存
def save():
    global filename
    try:
        f = open(filename,'w')
        msg = textpad.get(1.0,tk.END)
        f.write(msg)
        f.close()
    except:
        saveas()
#另存为
def saveas():
    f = filedialog.asksaveasfilename(initialfile= '未命名.txt', defaultextension='.txt')
    global filename
    filename = f
    fh = open(f,'w')
    msg = textpad.get(1.0,tk.END)
    fh.write(msg)
    fh.close()
    root.title('FileName:'+os.path.basename(f))


def cut():
    textpad.event_generate('<<Cut>>')

def copy():
    textpad.event_generate('<<Copy>>')

def paste():
    textpad.event_generate('<<Paste>>')

def redo():
    textpad.event_generate('<<Redo>>')

def undo():
    textpad.event_generate('<<Undo>>')

def selectAll():
    textpad.tag_add('sel','1.0',tk.END)

def search():
    topsearch = tk.Toplevel(root)
    topsearch.geometry('300x30+200+250')
    label1 = tk.Label(topsearch,text='Find')
    label1.grid(row=0, column=0,padx=5)
    entry1 = tk.Entry(topsearch,width=20)
    entry1.grid(row=0, column=1,padx=5)
    button1 = tk.Button(topsearch,text='查找')
    button1.grid(row=0, column=2)


#编辑
editmenu = tk.Menu(me)
editmenu.add_command(label = '撤销',accelerator = 'ctrl + z')
editmenu.add_command(label = '重做',accelerator = 'ctrl + y')
editmenu.add_command(label = '复制',accelerator = 'ctrl + c')
editmenu.add_command(label = '剪切',accelerator = 'ctrl + x')
editmenu.add_command(label = '粘贴',accelerator = 'ctrl + v')
editmenu.add_command(label = '查找',accelerator = 'ctrl + F')
editmenu.add_command(label = '全选',accelerator = 'ctrl + A')
me.add_cascade(label = '编辑',menu = editmenu)

#关于
def author():
    messagebox.showinfo('作者信息','本软件由qssjx完成')
def about():
    messagebox.showinfo('版权信息.copyright','版权属于qssjx')

aboutmenu = tk.Menu(me)
aboutmenu.add_command(label = '作者',command = author)
aboutmenu.add_command(label = '版权',command = about)
me.add_cascade(label = '关于',menu = aboutmenu)

#toolbar
toolbar = tk.Frame(root,height = 15,bg = 'SkyBlue')
shortButton = tk.Button(toolbar,text = '新建',command = open)
shortButton.pack(side = tk.LEFT)
shortButton = tk.Button(toolbar,text = '打开',command = 123)
shortButton.pack(side = tk.LEFT,padx = 5,pady = 5)
shortButton = tk.Button(toolbar,text = '保存',command = 1233)
shortButton.pack(side = tk.RIGHT)
shortButton = tk.Button(toolbar,text = '撤销',command = 1231232)
shortButton.pack(side = tk.RIGHT,padx = 5,pady = 5)
toolbar.pack(expand = tk.NO,fill = tk.X)

#正文编辑区域
lnlabel = tk.Label(root,width = 2,bg = 'antique white')
lnlabel.pack(side = tk.LEFT,fill = tk.Y)

textpad = tk.Text(root,undo = True)
textpad.pack(expand = tk.YES,fill = tk.BOTH)

scroll = tk.Scrollbar(textpad)
textpad.config(yscrollcommand = scroll.set)
scroll.config(command = textpad.yview)
scroll.pack(side = tk.RIGHT,fill = tk.Y)


root.mainloop()
