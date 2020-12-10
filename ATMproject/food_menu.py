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

def amt_cut(pr):
    my_conn = sqlite3.connect('SquareOne.db')
    my_curr = my_conn.cursor()
    my_id = my_conn.execute('''SELECT id from IdName ''')
    x = ""
    for id in my_id:
        x = id
    
    present_ammount = my_conn.execute("SELECT AccountBal from Student WHERE CardNo = ? ",x)

    for i in present_ammount:
        pr_amt = i[0]

    a = int(int(pr_amt)-50)
    b =int(pr)

    if a < b:
        messagebox.showerror(title="Error", message="You Don't have sufficient Balance in your Account Please Recharge first"
                                 )
        root.destroy()
    else:
            
        new_ammount = str(int(pr_amt)-int(pr))

       

        stwt = 'UPDATE Student SET AccountBal = ? WHERE CardNo = ?'
        my_curr.execute(stwt,(new_ammount,x[0]))
        my_conn.commit()

        messagebox.showerror(title="order Placed", message="Your order was Successfully Placed!! \n Thanks for ordering , Enjoy your Meal "
                                    )

        root.destroy()






if __name__ == "__main__":
    root = tk.Tk()
    root.title("Order Food")
    root.configure(background='gray5', bd=1, relief=SUNKEN)
    root.geometry('633x745')
    root.minsize(633, 745)
    #root.maxsize(633, 700)

    top_top_frame = Frame(root, bg='gold', relief=SUNKEN)
    top_top_frame.grid(row=0, sticky="ew")

    top_frame = Frame(root, bg='gold', relief=SUNKEN)
    top_frame.grid(row=1, sticky="ew")

    top_head_frame = Frame(root, bg='RosyBrown1', relief=SUNKEN)
    top_head_frame.grid(row=2, sticky="ew")

    top_list_frame = Frame(root, bg='gray7', relief=SUNKEN)
    top_list_frame.grid(row=3, sticky="ew")

    middle_frame = Frame(root, bg='gold', relief=SUNKEN)
    middle_frame.grid(row=4, sticky="ew")

    middle_head_frame = Frame(root, bg='RosyBrown1', relief=SUNKEN)
    middle_head_frame.grid(row=5, sticky="ew")

    middle_list_frame = Frame(root, bg='gray7', relief=SUNKEN)
    middle_list_frame.grid(row=6, sticky="ew")

    bottom_frame = Frame(root, bg='gold', relief=SUNKEN)
    bottom_frame.grid(row=7, sticky="ew")

    bottom_head_frame = Frame(root, bg='RosyBrown1', relief=SUNKEN)
    bottom_head_frame.grid(row=8, sticky="ew")

    bottom_list_frame = Frame(root, bg='gray7', relief=SUNKEN)
    bottom_list_frame.grid(row=9, sticky="ew")

    last_frame = Frame(root, bg='gray7', relief=SUNKEN)
    last_frame.grid(row=10, sticky="ew")

    headingLabel = tk.Label(top_top_frame, text="ORDER FOOD",
                            bg="gold", fg="black", relief=SUNKEN, width=39, height=3, font=('ComicSansMs', 24, 'bold'), anchor=CENTER)

    headingLabel.grid(row=0, sticky="nsew")

    bf_Label = tk.Label(top_frame, text="Soft Drinks / Drinks",
                            bg="bisque3", fg="black", relief=SUNKEN, width=48, height=2, font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    bf_Label.grid(row=0, sticky="nsew")

    itemLabel= tk.Label(top_head_frame, text="Item",
                            bg="RosyBrown1", fg="black",relief=RAISED, width=20, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    itemLabel.grid(row=1,column=0, sticky="nsew")

    PriceLabel= tk.Label(top_head_frame, text="Price",
                            bg="RosyBrown1", fg="black",relief=RAISED, width=20, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    PriceLabel.grid(row=1,column=1, sticky="nsew")

    oppLabel= tk.Label(top_head_frame, text="Order",
                            bg="RosyBrown1", fg="black",relief=RAISED, width=21, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    oppLabel.grid(row=1,column=2, sticky="nsew")

    bf_Label00 = tk.Label(top_list_frame, text="Pepsi / Cola / Dew",
                            bg="gray7", fg="white",relief = GROOVE, width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label00.grid(row=0,column=0 ,sticky="nsew")

    bf_Label01 = tk.Label(top_list_frame, text="40₹",
                            bg="gray7", fg="white",relief = GROOVE, width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label01.grid(row=0,column=1 ,sticky="nsew")

    order_button02 = Button(top_list_frame, text="Order", command = lambda: amt_cut(40) ,highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = GROOVE)
    order_button02.grid(row=0, column=2, sticky='nsew', pady=(5,2),padx=(80, 15))

    bf_Label10 = tk.Label(top_list_frame, text="Fruit Bear",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label10.grid(row=1,column=0 ,sticky="nsew")

    bf_Label11 = tk.Label(top_list_frame, text="30₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label11.grid(row=1,column=1 ,sticky="nsew")

    order_button12 = Button(top_list_frame, text="Order",command = lambda: amt_cut(30) ,  highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button12.grid(row=1, column=2, sticky='nsew',pady=(2,2), padx=(80, 15))

    bf_Label20 = tk.Label(top_list_frame, text="Water",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label20.grid(row=2,column=0 ,sticky="nsew")

    bf_Label21 = tk.Label(top_list_frame, text="15₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label21.grid(row=2,column=1 ,sticky="nsew")

    order_button22 = Button(top_list_frame, text="Order", command = lambda: amt_cut(15) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button22.grid(row=2, column=2, sticky='nsew',pady=(2,2), padx=(80, 15))

    bf_Label30 = tk.Label(top_list_frame, text="Milk",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label30.grid(row=3,column=0 ,sticky="nsew")

    bf_Label31 = tk.Label(top_list_frame, text="22₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label31.grid(row=3,column=1 ,sticky="nsew")

    order_button32 = Button(top_list_frame, text="Order", command = lambda: amt_cut(22) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button32.grid(row=3, column=2, sticky='nsew',pady=(2,5), padx=(80, 15))



    lu_Label = tk.Label(middle_frame, text="Fast Food",
                            bg="bisque3", fg="black", relief=SUNKEN, width=48, height=2, font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    lu_Label.grid(row=0, sticky="nsew")

    itemLabel= tk.Label(middle_head_frame, text="Item",
                            bg="RosyBrown1", fg="black", relief=RAISED, width=20, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    itemLabel.grid(row=0,column=0, sticky="nsew")

    PriceLabel= tk.Label(middle_head_frame, text="Price",
                            bg="RosyBrown1", fg="black", relief=RAISED, width=20, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    PriceLabel.grid(row=0,column=1, sticky="nsew")

    oppLabel= tk.Label(middle_head_frame, text="Order",
                            bg="RosyBrown1", fg="black", relief=RAISED, width=21, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    oppLabel.grid(row=0,column=2, sticky="nsew")

    bf_Label00 = tk.Label(middle_list_frame, text="Burger",
                            bg="gray7", fg="white",relief = GROOVE, width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label00.grid(row=0,column=0 ,sticky="nsew")

    bf_Label01 = tk.Label(middle_list_frame, text="150₹",
                            bg="gray7", fg="white",relief = GROOVE, width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label01.grid(row=0,column=1 ,sticky="nsew")

    order_button02 = Button(middle_list_frame, text="Order", command = lambda: amt_cut(150) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = GROOVE)
    order_button02.grid(row=0, column=2, sticky='nsew', pady=(5,2),padx=(80, 15))

    bf_Label10 = tk.Label(middle_list_frame, text="Onion Pizza",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label10.grid(row=1,column=0 ,sticky="nsew")

    bf_Label11 = tk.Label(middle_list_frame, text="220₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label11.grid(row=1,column=1 ,sticky="nsew")

    order_button12 = Button(middle_list_frame, text="Order", command = lambda: amt_cut(220) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button12.grid(row=1, column=2, sticky='nsew',pady=(2,2), padx=(80, 15))

    bf_Label20 = tk.Label(middle_list_frame, text="Pasta",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label20.grid(row=2,column=0 ,sticky="nsew")

    bf_Label21 = tk.Label(middle_list_frame, text="40₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label21.grid(row=2,column=1 ,sticky="nsew")

    order_button22 = Button(middle_list_frame, text="Order", command = lambda: amt_cut(40) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button22.grid(row=2, column=2, sticky='nsew',pady=(2,2), padx=(80, 15))

    bf_Label30 = tk.Label(middle_list_frame, text="Veg Wrap",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label30.grid(row=3,column=0 ,sticky="nsew")

    bf_Label31 = tk.Label(middle_list_frame, text="60₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label31.grid(row=3,column=1 ,sticky="nsew")

    order_button32 = Button(middle_list_frame, text="Order", command = lambda: amt_cut(60) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button32.grid(row=3, column=2, sticky='nsew',pady=(2,5), padx=(80, 15))

    dr_Label = tk.Label(bottom_frame, text="Breakfast / Lunch / Dinner",
                            bg="bisque3", fg="black", relief=SUNKEN, width=48, height=2, font=('ComicSansMs', 19, 'bold'), anchor=CENTER)

    dr_Label.grid(row=0, sticky="nsew")

    itemLabel= tk.Label(bottom_head_frame, text="Item",
                            bg="RosyBrown1", fg="black", relief=RAISED, width=20, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    itemLabel.grid(row=0,column=0, sticky="nsew")

    PriceLabel= tk.Label(bottom_head_frame, text="Price",
                            bg="RosyBrown1", fg="black", relief=RAISED, width=20, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    PriceLabel.grid(row=0,column=1, sticky="nsew")

    oppLabel= tk.Label(bottom_head_frame, text="Order",
                            bg="RosyBrown1", fg="black", relief=RAISED, width=21, height=1, font=('ComicSansMs', 14, 'bold'), anchor=CENTER)

    oppLabel.grid(row=0,column=2, sticky="nsew")

    bf_Label00 = tk.Label(bottom_list_frame, text="Soya Chaap / Mix Veg",
                            bg="gray7", fg="white",relief = GROOVE, width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label00.grid(row=0,column=0 ,sticky="nsew")

    bf_Label01 = tk.Label(bottom_list_frame, text="60₹",
                            bg="gray7", fg="white",relief = GROOVE, width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label01.grid(row=0,column=1 ,sticky="nsew")

    order_button02 = Button(bottom_list_frame, text="Order",command = lambda: amt_cut(60) ,  highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = GROOVE)
    order_button02.grid(row=0, column=2, sticky='nsew', pady=(5,2),padx=(80, 15))

    bf_Label10 = tk.Label(bottom_list_frame, text="Daal Fry x 2 / Butter Chiken",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label10.grid(row=1,column=0 ,sticky="nsew")

    bf_Label11 = tk.Label(bottom_list_frame, text="120₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label11.grid(row=1,column=1 ,sticky="nsew")

    order_button12 = Button(bottom_list_frame, text="Order", command = lambda: amt_cut(120) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button12.grid(row=1, column=2, sticky='nsew',pady=(2,2), padx=(80, 15))

    bf_Label20 = tk.Label(bottom_list_frame, text="Fried Rice / Plain Rice",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',13, 'bold'), anchor=CENTER)

    bf_Label20.grid(row=2,column=0 ,sticky="nsew")

    bf_Label21 = tk.Label(bottom_list_frame, text="35₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label21.grid(row=2,column=1 ,sticky="nsew")

    order_button22 = Button(bottom_list_frame, text="Order",command = lambda: amt_cut(35) ,  highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button22.grid(row=2, column=2, sticky='nsew',pady=(2,2), padx=(80, 15))

    bf_Label30 = tk.Label(bottom_list_frame, text="Amritsari Naan / Chapati x 3 / Paratha",
                            bg="gray7", fg="white",relief = RIDGE , width=22, font=('ComicSansMs',10, 'bold'), anchor=CENTER)

    bf_Label30.grid(row=3,column=0 ,sticky="nsew")

    bf_Label31 = tk.Label(bottom_list_frame, text="15₹",
                            bg="gray7", fg="white",relief = RIDGE ,width=22, font=('ComicSansMs', 13, 'bold'), anchor=CENTER)

    bf_Label31.grid(row=3,column=1 ,sticky="nsew")

    order_button32 = Button(bottom_list_frame, text="Order", command = lambda: amt_cut(15) , highlightbackground='dark goldenrod',
                      font="times 20 bold",relief = RIDGE )
    order_button32.grid(row=3, column=2, sticky='nsew',pady=(2,5), padx=(80, 15))

    status_label = Label(last_frame, text=(f"{dt.datetime.now():%a, %b %d %Y}"+",BY-Divay Shanu(1710991234)"),
                         relief=RAISED, font="ComicSansMs 10", fg='gold2', bg='gray3', bd=0.5, anchor=W)
    status_label.pack(fill=X, side=BOTTOM)


    root.mainloop()
    