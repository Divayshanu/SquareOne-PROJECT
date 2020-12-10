import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk
import datetime as dt
from subprocess import Popen
import sys
import firebase_admin
from firebase_admin import credentials


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

def register():
    Atm_root.destroy()
    Popen([sys.executable, "./register.py"])


def login():
    Atm_root.destroy()
    Popen( [sys.executable, "./login.py"])


if __name__ == "__main__":

    
    Atm_root = Tk()

    Atm_root.geometry("1000x750")
    Atm_root.configure(background='gray5', bd=1, relief=SUNKEN)
    Atm_root.minsize(1000, 750)
    Atm_root.maxsize(1000, 750)
    Atm_root.title("Chitkara ATM")

    photo1 = PhotoImage(file="cu_image1.png")
    photo2 = PhotoImage(file="menu_1.png")

    t_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    t_frame.grid(row=0, column=0, sticky="nsew")

    Atm_root.grid_rowconfigure(1, weight=1)
    Atm_root.grid_columnconfigure(0, weight=1)

    marquee = Marquee(t_frame, text="WELCOME TO CHITKARA UNIVERSITY ATM",
                      borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    p_frame = Frame(Atm_root, bg="black", relief=SUNKEN, bd=1)
    p_frame.grid(row=1, column=0, sticky='nsew')

    p_lable = Label(p_frame, image=photo1, bg="white",
                    borderwidth=3)
    p_lable.pack(side="top", fill=BOTH,)

    t1_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    t1_frame.grid(row=2, column=0, sticky="nsew")

    marquee = Marquee(t1_frame, text="CHITKARA UNIVERSITY FOOD COURT",
                      borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    r_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    r_frame.grid(row=4, column=0, sticky='nsew')

    r_frame.grid_rowconfigure(1, weight=1)
    r_frame.grid_columnconfigure(0, weight=1)

    bottom_lside_frame = Frame(r_frame, bg="black", relief=SUNKEN)
    bottom_lside_frame.grid(row=0, column=0, sticky='nsew')

    lp_lable = Label(bottom_lside_frame, image=photo2,
                   bg="white", borderwidth=3)
    lp_lable.pack(side=LEFT, fill=X)

    bottom_rside_frame = Frame(r_frame, bg="black", relief=SUNKEN)
    bottom_rside_frame.grid(row=0, column=1, sticky='nsew')

    r_button = Button(bottom_rside_frame, text="REGISTER", highlightbackground='#ffff00', fg="black",
                      font="times 30 bold", relief=SUNKEN, bd=2, command=register)
    r_button.grid(row=0, column=0, sticky='nsew', pady=(50, 30), padx=(5, 5))

    l_button = Button(bottom_rside_frame, text="LOGIN", highlightbackground='#00cc00', fg="black",
                      font="times 30 bold", relief=SUNKEN, bd=2, command=login)
    l_button.grid(row=1, column=0, sticky='nsew', pady=(30, 30), padx=(5, 5))

    q_button = Button(bottom_rside_frame, text="EXIT", highlightbackground='#b30000', fg="black",
                      font="times 30 bold", relief=SUNKEN, bd=2, command=quit)

    q_button.grid(row=2, column=0, sticky='nsew', pady=(30, 50), padx=(5, 5))

    d_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    d_frame.grid(row=5,  sticky='nsew')

    status_label = Label(d_frame, text=(f"{dt.datetime.now():%a, %b %d %Y}"+",BY-Divay Shanu(1710991234)"),
                         relief=SUNKEN, font="ComicSansMs 10", fg='gold2', bg='gray3', bd=0.5, anchor=W)
    status_label.pack(fill=X, side=BOTTOM)

    Atm_root.mainloop()
