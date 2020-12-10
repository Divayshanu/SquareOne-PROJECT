import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Message, Text
from cv2 import cv2
import datetime as dt
import os
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.font as font
from tkinter import messagebox
from subprocess import Popen
import sys
import sqlite3
import login
from tkinter import simpledialog

class Marquee(Canvas):
    def __init__(self, parent, text, margin=3, borderwidth=2, relief='flat', bg="red", fps=100):
        Canvas.__init__(self, parent, borderwidth=borderwidth,
                        relief=relief, bg="red")
        self.fps = fps
        text = self.create_text(0, -1000, text=text,
                                anchor="w", tags=("text",), fill="white", font=('freemono', 10, 'bold'))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2 * margin) + (2 * borderwidth)
        height = (y1 - y0) + (2 * margin) + (2 * borderwidth)
        self.configure(width=width, height=height)

        self.animate()

    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            x0 = self.winfo_width()
            y0 = int(self.winfo_height() / 2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)
        self.after_id = self.after(int(1000 / self.fps), self.animate)



def Information():
    root.destroy()
    my_info = tk.Tk()
    my_info.title("MY INFORMATION")
    my_info.geometry("405x150")
    my_info.minsize(405, 150)
    my_info.maxsize(405, 150)
    my_info.configure(background='aquamarine', bd=1, relief=SUNKEN,)

    top_frame_info = Frame(my_info,bg='aquamarine', relief=SUNKEN)
    top_frame_info.grid(row=0, sticky="nsew")

    headingLabel = tk.Label(top_frame_info, text="Name",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=0,sticky='nsew')
    headingLabel = tk.Label(top_frame_info, text="Square No Id",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=1,sticky='nsew')
    
    Bottom_frame_info = Frame(my_info,bg='aquamarine', relief=SUNKEN)
    Bottom_frame_info.grid(row=1,column=0, sticky="nsew")

    Blank_frame_info = Frame(my_info,bg='aquamarine', relief=SUNKEN)
    Blank_frame_info.grid(row=2,column=0, sticky="nsew")

    Button_frame_info = Frame(my_info,bg='red', relief=SUNKEN)
    Button_frame_info.grid(row=3,column=0, sticky="nsew")

    my_conn = sqlite3.connect('SquareOne.db')
    my_id = my_conn.execute('''SELECT id from IdName ''')
    x = ""
    for id in my_id:
        x = id
    r_set=my_conn.execute("SELECT Fullname, CardNo from Student WHERE CardNo = ? ",x)
    i=0
    for student in r_set: 
        for j in range(len(student)):
            e = Entry(Bottom_frame_info, width=21,fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
            e.configure(state = "readonly", background='peach puff')
        i=i+1

    back_button = Button(Button_frame_info, text="OUIT",command =lambda:[Popen([sys.executable, "./gui.py"]), my_info.destroy()], highlightbackground='orchid1',
                      font="times 25 bold", relief=SUNKEN, bd=3)
    back_button.grid(row=0, column=2, sticky='nsew', pady=(30, 30), padx=(160, 50))
    my_info.mainloop()
    

def Bal():
    root.destroy()
    my_bal = tk.Tk()
    my_bal.title("Balance Information")
    my_bal.geometry("405x150")
    my_bal.minsize(405, 150)
    my_bal.maxsize(405, 150)
    my_bal.configure(background='aquamarine', bd=1, relief=SUNKEN,)

    top_frame_bal = Frame(my_bal,bg='aquamarine', relief=SUNKEN)
    top_frame_bal.grid(row=0, sticky="nsew")

    headingLabel = tk.Label(top_frame_bal, text="Name",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=0,sticky='nsew')
    headingLabel = tk.Label(top_frame_bal, text="Account Balance",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=1,sticky='nsew')

    Bottom_frame_bal = Frame(my_bal,bg='aquamarine', relief=SUNKEN)
    Bottom_frame_bal.grid(row=1, sticky="nsew")

    Blank_frame_bal = Frame(my_bal,bg='aquamarine', relief=SUNKEN)
    Blank_frame_bal.grid(row=2,column=0, sticky="nsew")

    Button_frame_bal = Frame(my_bal,bg='red', relief=SUNKEN)
    Button_frame_bal.grid(row=3,column=0, sticky="nsew")


    my_conn = sqlite3.connect('SquareOne.db')
    my_id = my_conn.execute('''SELECT id from IdName ''')
    x = ""
    for id in my_id:
        x = id
    r_set=my_conn.execute("SELECT Fullname, AccountBal from Student WHERE CardNo = ? ",x)
    i=0
    for student in r_set: 
        for j in range(len(student)):
            e = Entry(Bottom_frame_bal, width=21,fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
            e.configure(state = "readonly", background='peach puff')
        i=i+1
    back_button = Button(Button_frame_bal, text="OUIT",command =lambda:[Popen([sys.executable, "./gui.py"]), my_bal.destroy()], highlightbackground='orchid1',
                      font="times 25 bold", relief=SUNKEN, bd=3,)
    back_button.grid(row=0, column=2, sticky='nsew', pady=(30, 30), padx=(160, 50))

    my_bal.mainloop()


def Acc_recharge():
    root.destroy()
    upd_bal = tk.Tk()
    upd_bal.title("Balance Information")
    upd_bal.geometry("405x150")
    upd_bal.minsize(405, 150)
    upd_bal.maxsize(405, 150)
    upd_bal.configure(background='aquamarine', bd=1, relief=SUNKEN,)

    top_frame_upd = Frame(upd_bal,bg='aquamarine', relief=SUNKEN)
    top_frame_upd.grid(row=0, sticky="nsew")

    headingLabel = tk.Label(top_frame_upd, text="Name",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=0,sticky='nsew')
    headingLabel = tk.Label(top_frame_upd, text="New Balance",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=1,sticky='nsew')

    Bottom_frame_upd = Frame(upd_bal,bg='aquamarine', relief=SUNKEN)
    Bottom_frame_upd.grid(row=1, sticky="nsew")

    Blank_frame_upd = Frame(upd_bal,bg='aquamarine', relief=SUNKEN)
    Blank_frame_upd.grid(row=2,column=0, sticky="nsew")

    Button_frame_upd = Frame(upd_bal,bg='red', relief=SUNKEN)
    Button_frame_upd.grid(row=3,column=0, sticky="nsew")

    new_bal = simpledialog.askstring(title="Recharge",
                                  prompt="How much Amount you want to add?:")
    
    upd_conn = sqlite3.connect('SquareOne.db')
    upd_curr = upd_conn.cursor()
    upd_id = upd_conn.execute('''SELECT id from IdName ''')
    x = ""
    for id in upd_id:
        x = id
    pre_bal = upd_conn.execute("SELECT AccountBal from Student WHERE CardNo = ? ",x)

    for i in pre_bal:
        curr_bal = i
    cur_bal = curr_bal[0]
    
    upd_conn.execute("UPDATE AccountHistory SET pre_trans = ? WHERE CardNo = ? ",(new_bal,x[0]))
    new_bal = (int(new_bal) + int(cur_bal))
    stwt = 'UPDATE Student SET AccountBal = ? WHERE CardNo = ?'
    upd_curr.execute(stwt,(new_bal,x[0]))
    upd_conn.commit()
    r_set=upd_conn.execute("SELECT Fullname, AccountBal from Student WHERE CardNo = ? ",x)
    i=0
    for student in r_set: 
        for j in range(len(student)):
            e = Entry(Bottom_frame_upd, width=21,fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
            e.configure(state = "readonly", background='peach puff')
        i=i+1
    back_button = Button(Button_frame_upd, text="OUIT",command =lambda:[Popen([sys.executable, "./gui.py"]), upd_bal.destroy()], highlightbackground='orchid1',
                      font="times 25 bold", relief=SUNKEN, bd=3,)
    back_button.grid(row=0, column=2, sticky='nsew', pady=(30, 30), padx=(160, 50))

    upd_bal.mainloop()

def about():
    root.destroy()
    abt = tk.Tk()
    abt.title("Balance Information")
    abt.geometry("405x220")
    abt.minsize(405, 220)
    abt.maxsize(405, 220)
    abt.configure(background='wheat1', bd=1, relief=SUNKEN)

    top_frame_upd = Frame(abt,bg='wheat1', relief=SUNKEN)
    top_frame_upd.grid(row=0, sticky="nsew")

    Button_frame_abt = Frame(abt,bg='SlateBlue1', relief=SUNKEN)
    Button_frame_abt.grid(row=1,column=0, sticky="nsew")

    headingLabel = tk.Label(top_frame_upd, text="Developed by- Divay shanu \n Roll no. -1710991234 \n Batch -2017-2021 \n Section - I \n Subject - LOP \n Submitted To - Dr. Sarita",
                            bg="wheat1", fg="gray4",width=29, relief=SUNKEN,font=('ComicSansMs', 20, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=0,sticky='nsew')

    back_button = Button(Button_frame_abt, text="OUIT",command =lambda:[Popen([sys.executable, "./gui.py"]), abt.destroy()], highlightbackground='salmon3',
                      font="times 25 bold", relief=SUNKEN, bd=3,)
    back_button.grid(row=0, column=2, sticky='nsew', pady=(30, 30), padx=(160, 50))

    abt.mainloop()



def food_menu():
    root.destroy()
    Popen([sys.executable, "./food_menu.py"])

def today_offer():
    root.destroy()
    td_off = tk.Tk()
    td_off.title("Special Offer")
    td_off.geometry("405x200")
    td_off.minsize(405, 300)
    td_off.maxsize(405, 300)
    td_off.configure(background='aquamarine', bd=1, relief=SUNKEN)

    top_top_frame_off = Frame(td_off,bg='aquamarine', relief=SUNKEN)
    top_top_frame_off.grid(row=0, sticky="ew")

    marquee = Marquee(top_top_frame_off, text="Today's Special Offer",
                      borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    top_frame_off = Frame(td_off,bg='aquamarine', relief=SUNKEN)
    top_frame_off.grid(row=1, sticky="nsew")

    headingLabel = tk.Label(top_frame_off, text="Item",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=0,sticky='nsew')
    headingLabel = tk.Label(top_frame_off, text="Price",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=1,sticky='nsew')

    Bottom_frame_off = Frame(td_off,bg='aquamarine', relief=SUNKEN)
    Bottom_frame_off.grid(row=2, sticky="nsew")

    itemLabel00 = tk.Label(Bottom_frame_off, text="Onion Pizza",
                            bg="gray6", fg="white",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel00.grid(row=0,column=0,sticky='nsew')

    itemLabel01 = tk.Label(Bottom_frame_off, text="220₹",
                            bg="green yellow", fg="gray4",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel01.grid(row=0,column=1,sticky='nsew')

    itemLabel10 = tk.Label(Bottom_frame_off, text="Pasta",
                            bg="gray6", fg="white",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel10.grid(row=1,column=0,sticky='nsew')

    itemLabel11 = tk.Label(Bottom_frame_off, text="40₹",
                            bg="green yellow", fg="gray4",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel11.grid(row=1,column=1,sticky='nsew')
    itemLabel20 = tk.Label(Bottom_frame_off, text="Amritsari Naan",
                            bg="gray6", fg="white",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel20.grid(row=2,column=0,sticky='nsew')

    itemLabel21 = tk.Label(Bottom_frame_off, text="15₹",
                            bg="green yellow", fg="gray4",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel21.grid(row=2,column=1,sticky='nsew')

    itemLabel30 = tk.Label(Bottom_frame_off, text="Fruit Bear",
                            bg="gray6", fg="white",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel30.grid(row=3,column=0,sticky='nsew')

    itemLabel31 = tk.Label(Bottom_frame_off, text="30₹",
                            bg="green yellow", fg="gray4",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel31.grid(row=3,column=1,sticky='nsew')

    itemLabel40 = tk.Label(Bottom_frame_off, text="Burger",
                            bg="gray6", fg="white",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel40.grid(row=4,column=0,sticky='nsew')

    itemLabel41 = tk.Label(Bottom_frame_off, text="150₹",
                            bg="green yellow", fg="gray4",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    itemLabel41.grid(row=4,column=1,sticky='nsew')

    Blank_frame_off = Frame(td_off,bg='aquamarine', relief=SUNKEN)
    Blank_frame_off.grid(row=3,column=0, sticky="nsew")

    Button_frame_off = Frame(td_off,bg='red', relief=SUNKEN)
    Button_frame_off.grid(row=4,column=0, sticky="nsew")

    back_button = Button(Button_frame_off, text="OUIT",command =lambda:[Popen([sys.executable, "./gui.py"]), td_off.destroy()], highlightbackground='dark goldenrod',
                      font="times 25 bold", relief=SUNKEN, bd=3,)
    back_button.grid(row=0, column=1, sticky='nsew', pady=(30, 30), padx=(50, 50))

    back_button = Button(Button_frame_off, text="Order",command =food_menu, highlightbackground='dark goldenrod',
                      font="times 25 bold", relief=SUNKEN, bd=3,)
    back_button.grid(row=0, column=2, sticky='nsew', pady=(30, 30), padx=(100, 10))

    td_off.mainloop()

def acc_statement():
    root.destroy()
    acc_stat = tk.Tk()
    acc_stat.title("Account Statement")
    acc_stat.geometry("405x150")
    acc_stat.minsize(405, 150)
    acc_stat.maxsize(405, 150)
    acc_stat.configure(background='aquamarine', bd=1, relief=SUNKEN)

    top_frame_stat = Frame(acc_stat,bg='aquamarine', relief=SUNKEN)
    top_frame_stat.grid(row=0, sticky="nsew")

    headingLabel = tk.Label(top_frame_stat, text="Name",
                            bg="green", fg="gray4",width=14, relief=SUNKEN,font=('ComicSansMs', 20, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=0,sticky='nsew')
    headingLabel = tk.Label(top_frame_stat, text="Last Recharge",
                            bg="green", fg="gray4",width=15, relief=SUNKEN,font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0,column=1,sticky='nsew')

    Bottom_frame_stat = Frame(acc_stat,bg='aquamarine', relief=SUNKEN)
    Bottom_frame_stat.grid(row=1, sticky="nsew")

    Blank_frame_stat = Frame(acc_stat,bg='aquamarine', relief=SUNKEN)
    Blank_frame_stat.grid(row=2,column=0, sticky="nsew")

    Button_frame_stat = Frame(acc_stat,bg='red', relief=SUNKEN)
    Button_frame_stat.grid(row=3,column=0, sticky="nsew")

    stat_conn = sqlite3.connect('SquareOne.db')
    stat_id = stat_conn.execute('''SELECT id from IdName ''')
    x = ""
    for id in stat_id:
        x = id

    r_set=stat_conn.execute("SELECT Name, pre_trans from AccountHistory WHERE cardno = ? ",x)
    i=0
    for student in r_set: 
        for j in range(len(student)):
            e = Entry(Bottom_frame_stat, width=21,fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
            e.configure(state = "readonly", background='peach puff')
        i=i+1
    
    back_button = Button(Button_frame_stat, text="OUIT",command =lambda:[Popen([sys.executable, "./gui.py"]), acc_stat.destroy()], highlightbackground='orchid1',
                      font="times 25 bold", relief=SUNKEN, bd=3,)
    back_button.grid(row=0, column=2, sticky='nsew', pady=(30, 30), padx=(160, 50))



    acc_stat.mainloop()
    

if __name__ == "__main__":
     
    root = tk.Tk()
    root.title("Welcome to Chitkara Square One Homepage")
    root.configure(background='gray5', bd=1, relief=SUNKEN,)
    root.minsize(675, 500)
    root.maxsize(675, 500)
    root.geometry('675x500')

    top_frame = Frame(root, bg='gold', relief=SUNKEN)
    center = Frame(root, bg='#00cc00', relief=SUNKEN, bd=1)
    btm_frame = Frame(root, bg='black', relief=SUNKEN)

    left_center_frame = Frame(center, bg='gray5', relief=SUNKEN)
    center_center_frame = Frame(center, bg='black', relief=SUNKEN)
    right_center_frame = Frame(center, bg='gray5', relief=SUNKEN)
    

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=5, sticky="nsew")

    left_center_frame.grid(row=0, column=0, sticky="nse")
    center_center_frame.grid(row=0, column=1, sticky="nsew")
    right_center_frame.grid(row=0, column=2, sticky="nsw")



    headingLabel = tk.Label(top_frame, text="CHITKARA SQUARE ONE",
                            bg="gold", fg="black", relief=SUNKEN, width=29, height=3, font=('ComicSansMs', 34, 'italic bold'), anchor=CENTER)

    headingLabel.pack(fill=X)

    a_button = Button(left_center_frame, text="My Info",command = Information, highlightbackground='yellow2',
                      font="times 25 bold", relief=SUNKEN, bd=3,)
    a_button.grid(row=0, column=0, sticky='nsew', pady=(25, 25), padx=(20, 20))


    c_button = Button(left_center_frame, text="Balance",command = Bal, highlightbackground='yellow2',
                      font="times 25 bold", relief=SUNKEN, bd=2,)
    c_button.grid(row=2, column=0, sticky='nsew', pady=(25, 25), padx=(20, 20))

    d_button = Button(left_center_frame, text="Recharge",command = Acc_recharge, highlightbackground='yellow2',
                      font="times 25 bold", relief=SUNKEN, bd=2,)
    d_button.grid(row=3, column=0, sticky='nsew', pady=(25, 25), padx=(20, 20))

    e_button = Button(left_center_frame, text="About", command = about ,highlightbackground='yellow2',
                      font="times 25 bold", relief=SUNKEN, bd=2,)
    e_button.grid(row=4, column=0, sticky='nsew', pady=(25, 25), padx=(20, 20))



    headingLabel = tk.Label(center_center_frame, text="SELECT YOUR OPTION",
                            bg='misty rose', fg="black", relief=SUNKEN, width=29, height=3, font=('ComicSansMs', 16, 'italic bold'), anchor=CENTER)

    headingLabel.grid(row =0,column=0)

    headingLabel1 = tk.Label(center_center_frame, text="<----                                            \n                                   ---->",
                            bg='misty rose', fg="black", relief=SUNKEN, width=29, height=4, font=('ComicSansMs', 16, 'italic bold'), anchor=CENTER)


    headingLabel1.grid(row =1,column=0)

    headingLabel2 = tk.Label(center_center_frame, text="<----                                            \n                                   ---->",
                            bg='misty rose', fg="black", relief=SUNKEN, width=29, height=4, font=('ComicSansMs', 16, 'italic bold'), anchor=CENTER)


    headingLabel2.grid(row =2,column=0)
    headingLabel3 = tk.Label(center_center_frame, text="<----                                            \n                                   ---->",
                            bg='misty rose', fg="black", relief=SUNKEN, width=29, height=4, font=('ComicSansMs', 16, 'italic bold'), anchor=CENTER)


    headingLabel3.grid(row =3,column=0)

    f_button = Button(right_center_frame, text="Order Food",command = food_menu,highlightbackground='yellow2',
                      font="times 23 bold", relief=SUNKEN, bd=2,)
    f_button.grid(row=0, column=0, sticky='nsew', pady=(25, 25), padx=(10, 10))


    h_button = Button(right_center_frame, text="Special Offer",command = today_offer, highlightbackground='yellow2',
                      font="times 23 bold", relief=SUNKEN, bd=2,)
    h_button.grid(row=2, column=0, sticky='nsew', pady=(25, 25), padx=(10, 10))

    i_button = Button(right_center_frame, text="Account Statement",command = acc_statement, highlightbackground='yellow2',
                      font="times 21 bold", relief=SUNKEN, bd=2,)
    i_button.grid(row=3, column=0, sticky='nsew', pady=(25, 25), padx=(10, 10))

    j_button = Button(right_center_frame, text="Quit",command=quit ,highlightbackground='yellow2',
                      font="times 23 bold", relief=SUNKEN, bd=2,)
    j_button.grid(row=4, column=0, sticky='nsew', pady=(25, 25), padx=(10,10))


    status_label = Label(btm_frame, text=(f"{dt.datetime.now():%a, %b %d %Y}"),
                         relief=SUNKEN, font="ComicSansMs 10", fg='yellow2', bg='gray3', bd=0.5, anchor=W)
    status_label.pack(fill=X, side=BOTTOM)


    root.mainloop()

