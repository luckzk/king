# -*- coding: utf-8 -*-
'''
#intent      :
#Author      :Michael Jack hu
#start date  : 2018/12/20
#File        : 文献生成.py
#Software    : PyCharm
#finish date :
'''

< code > < code


class ="hljs python" >  # -*- coding: utf-8 -*-
# Author:哈士奇说喵
# 文献格式生成器1.0


import string
from Tkinter import *

# 主框架部分
root = Tk()
root.title('参考文献生成器1.0(哈尔滨工程大学专版)--by 哈士奇说喵')
root.iconbitmap('C:\\Users\\MrLevo\\PycharmProjects\\test\\heru.ico')  # 左上角小图标icon
img = PhotoImage(file='heru.gif')  # 图标（大）
Label(root, image=img).pack(side=TOP)
root.geometry()
Label_root = Label(root, text='规则运算(根框架)', font=('宋体', 15))


# ------------------------------------定义规则------------------------------

def Capital2low(info):  # 首字母大写，常用
    return string.capwords(info)


def All2low(info):  # 所有字母小写
    return info.lower()


def ALL2cap(info):  # 所以字母大写
    return info.upper()


def Periodical(author, title, issn, year, vol, issn_num, frompage):
    if vol == '':
        return '%s.%s[J].%s,%s%s%s:%s.' % (author, title, issn, year, vol, issn_num, frompage)
    else:
        return '%s.%s[J].%s,%s,%s(%s):%s.' % (author, title, issn, year, vol, issn_num, frompage)


def Thesis(author, title, save_place, university, year, frompage):
    return '%s.%s[D].%s:%s,%s:%s.' % (author, title, save_place, university, year, frompage)


def Book(author, title, save_place, issn, year, frompage):
    return '%s.%s[M].%s:%s,%s:%s.' % (author, title, save_place, issn, year, frompage)


def Meeting(author, title, issn, save_place, year, frompage):
    return '%s.%s[C].%s,%s,%s:%s.' % (author, title, issn, save_place, year, frompage)


# 还可以继续增加规则函数，只要是两输入的参数都可以
# ------------------------------------触发函数---------------------------------

def Title(a):
    try:
        if spec_title.get(spec_title.curselection()).encode('utf-8') == '题目首字母大写':
            re_title = Capital2low(a)
            return re_title
        if spec_title.get(spec_title.curselection()).encode('utf-8') == '题目全部小写':
            re_title = All2low(a)
            return re_title
        if spec_title.get(spec_title.curselection()).encode('utf-8') == '题目全部大写':
            re_title = ALL2cap(a)
            return re_title
        if spec_title.get(spec_title.curselection()).encode('utf-8') == '题目不做改变':
            return a

    except:
        return a


def Answ():  # 规则函数
    try:
        if lb.get(lb.curselection()).encode('utf-8') == '期刊[J]':
            Ans.insert(END, '[]' + Periodical(Capital2low(input_author.get()), Title(var_title.get()), var_issn.get(),
                                              var_year.get(), var_vol.get(), var_issn_num.get(),
                                              var_frompage.get()))  # 注意编码问题
        if lb.get(lb.curselection()).encode('utf-8') == '学位论文[D]':
            Ans.insert(END, '[]' + Thesis(Capital2low(input_author.get()), Title(var_title.get()), var_save_place.get(),
                                          var_university.get(), var_year.get(), var_frompage.get()))
        if lb.get(lb.curselection()).encode('utf-8') == '图书[M]':
            Ans.insert(END, '[]' + Book(Capital2low(input_author.get()), Title(var_title.get()), var_save_place.get(),
                                        var_issn.get(), var_year.get(), var_frompage.get()))
        if lb.get(lb.curselection()).encode('utf-8') == '会议[C]':
            Ans.insert(END, '[]' + Meeting(Capital2low(input_author.get()), Title(var_title.get()), var_issn.get(),
                                           var_save_place.get(), var_year.get(), var_frompage.get()))
    except:

        Ans.insert(END, '[]' + Periodical(Capital2low(input_author.get()), Title(var_title.get()), var_issn.get(),
                                          var_year.get(), var_vol.get(), var_issn_num.get(), var_frompage.get()))


def Clea():  # 清空函数
    input_title.delete(0, END)  # 这里entry的delect用0
    input_author.delete(0, END)
    input_save_palce.delete(0, END)
    input_university.delete(0, END)
    input_vol.delete(0, END)
    input_issn.delete(0, END)
    input_year.delete(0, END)
    input_issn_num.delete(0, END)
    input_frompage.delete(0, END)
    Ans.delete(0, END)  # text中的用0.0


# ----------------------------------输入选择框架------------------------------
frame_input = Frame(root)  # 分成两个框架了，好管理
# Label_input=Label(frame_input, text='(输入和选择框架)', font=('',15))
Label_author = Label(frame_input, text='作者(中间以英文逗号+空格隔开)(自动首字母大写)', font=('', 10))
Label_title = Label(frame_input, text='题目(支持大小写混输入)', font=('', 10))
Label_save_place = Label(frame_input, text='所在地--x', font=('', 10))
Label_university = Label(frame_input, text='啥大学啥论文--x', font=('', 10))
Label_issn = Label(frame_input, text='啥期刊/啥出版社/啥会议--x', font=('', 10))
Label_year = Label(frame_input, text='年份--x', font=('Times New Roman', 10))
Label_vol = Label(frame_input, text='第几卷--x', font=('Times New Roman', 10))
Label_issn_num = Label(frame_input, text='(第几期)--x', font=('Times New Roman', 10))
Label_frompage = Label(frame_input, text='起始页--x或xx-xx', font=('Times New Roman', 10))

var_author = StringVar()
var_title = StringVar()
var_vol = StringVar()
var_issn = StringVar()
var_year = StringVar()
var_issn_num = StringVar()
var_frompage = StringVar()
var_save_place = StringVar()
var_university = StringVar()
input_author = Entry(frame_input, textvariable=var_author, width=40)
input_title = Entry(frame_input, textvariable=var_title, width=80)
input_save_palce = Entry(frame_input, textvariable=var_save_place, width=20)
input_university = Entry(frame_input, textvariable=var_university, width=40)
input_vol = Entry(frame_input, textvariable=var_vol, width=10)
input_issn = Entry(frame_input, textvariable=var_issn, width=50)
input_year = Entry(frame_input, textvariable=var_year, width=10)
input_issn_num = Entry(frame_input, textvariable=var_issn_num, width=10)
input_frompage = Entry(frame_input, textvariable=var_frompage, width=10)

# ---------------------------------选择运算规则-----------------------------
# 还可以添加其他规则

lb = Listbox(frame_input, exportselection=False, height=3)
list_item = ['期刊[J]', '学位论文[D]', '图书[M]', '会议[C]']
for i in list_item:  # 需要用for循环读出列表中元素并显示插入insert
    lb.insert(END, i)  # END是指队列插入

spec_title = Listbox(frame_input, exportselection=False, height=3)  # title的选择
list_item = ['题目不做改变', '题目首字母大写', '题目全部小写', '题目全部大写']
for i in list_item:
    spec_title.insert(END, i)

# --------------------------------计算结果框架---------------------------------
frame_output = Frame(root)
# Label_output=Label(frame_output, text='(计算结果框架)', font=('',15))
Ans = Listbox(frame_output, selectmode=MULTIPLE, height=6, width=80)  # text也可以，Listbox好处在于换行
# Ans = Listbox(frame_output,selectmode=EXTENDED, height=6,width=80)#text也可以，Listbox好处在于换行

# ---------------------------------Button---------------------------------

calc = Button(frame_output, text='生成文献', command=Answ)
cle = Button(frame_output, text='清空', command=Clea)

# -----------------------------滑动Scrollbar----------------------------------------
# 注意和listbox的搭配使用
scr1 = Scrollbar(frame_input)  # 文献类型
lb.configure(yscrollcommand=scr1.set)
scr1['command'] = lb.yview

scr2 = Scrollbar(frame_output)
Ans.configure(yscrollcommand=scr2.set)
scr2['command'] = Ans.yview

scr3 = Scrollbar(frame_input)  # title改造
spec_title.configure(yscrollcommand=scr3.set)
scr3['command'] = spec_title.yview

scr4 = Scrollbar(frame_output, orient='horizontal')  # ans x
Ans.configure(xscrollcommand=scr4.set)
scr4['command'] = Ans.xview

# --------------------------------布局------------------------------------
# 布局写在一块容易排版，可能我low了吧
# Label_root.pack(side=TOP)
frame_input.pack(side=TOP)
# Label_input.pack(side=LEFT)


Label_author.pack()
input_author.pack()
Label_title.pack()
input_title.pack()
Label_save_place.pack()
input_save_palce.pack()
Label_university.pack()
input_university.pack()
Label_issn.pack()
input_issn.pack()
Label_year.pack()
input_year.pack()
Label_vol.pack()
input_vol.pack()
Label_issn_num.pack()
input_issn_num.pack()
Label_frompage.pack()
input_frompage.pack()
scr4.pack()

scr1.pack(side=LEFT, fill=Y)
lb.pack(side=LEFT)
scr3.pack(side=RIGHT, fill=Y)
spec_title.pack(side=RIGHT)

frame_output.pack(side=TOP)
# Label_output.pack(side=LEFT)
calc.pack(side=LEFT)
cle.pack(side=LEFT)
Ans.pack(side=LEFT)
scr2.pack(side=LEFT, fill=Y)

# ----------------------------root.mainloop()--------------------------

root.mainloop()