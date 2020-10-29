import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime as dt
from subprocess import Popen
import sys




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

def scanImage():
    pass


if __name__ == "__main__":
    
    root = Tk()
    root.title("Login")
    root.configure(background='gray5', bd=1, relief=SUNKEN,)
    root.minsize(700, 300)
    root.maxsize(700, 300)
    root.geometry('700x300')

    top_frame = Frame(root, bg='black', relief=SUNKEN)
    center = Frame(root, bg='black', relief=SUNKEN, bd=2)
    bottom_rside_frame = Frame(root, bg='black', relief=SUNKEN)
    btm_frame = Frame(root, bg='black', relief=SUNKEN)

    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=4, sticky="ew")
    bottom_rside_frame.grid(row=3, sticky="ew")

    marquee = Marquee(top_frame, text="WELCOME TO CHITKARA UNIVERSITY ATM",
                      borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    headingLabel = tk.Label(center, text="LOGIN",
                            bg="green", fg="white", relief=SUNKEN, width=49, height=6, font=('ComicSansMs', 21, 'italic bold'), anchor=CENTER)

    headingLabel.pack(fill=X)

    l_button = Button(bottom_rside_frame, text="Scan Now", highlightbackground='#00cc00', fg="black",
                      font="times 30 bold", relief=SUNKEN, bd=2, command=scanImage)
    l_button.grid(row=1, column=0, sticky='nsew', pady=(17, 15), padx=(280, 35))


    status_label = Label(btm_frame, text=(f"{dt.datetime.now():%a, %b %d %Y}"),
                         relief=SUNKEN, font="ComicSansMs 10", fg='linen', bg='gray3', bd=0.5, anchor=W)
    status_label.pack(fill=X, side=BOTTOM)

    root.mainloop()

