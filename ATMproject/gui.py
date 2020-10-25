import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk
import datetime as dt


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
    pass


if __name__ == "__main__":

    Atm_root = Tk()

    Atm_root.geometry("1000x750")
    Atm_root.configure(background='gray5', bd=1, relief=SUNKEN)
    Atm_root.minsize(1000, 750)
    Atm_root.maxsize(1000, 750)
    Atm_root.title("Chitkara ATM")
    # Atm_root.iconbitmap('ATM-icon.icns')

    photo = PhotoImage(file="cu_image1.png")

    # top frame
    t_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    t_frame.grid(row=0, column=0, sticky="nsew")

    Atm_root.grid_rowconfigure(1, weight=1)
    Atm_root.grid_columnconfigure(0, weight=1)

    marquee = Marquee(t_frame, text="WELCOME TO CHITKARA UNIVERSITY ATM",
                      borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    # photo frame
    p_frame = Frame(Atm_root, bg="black", relief=SUNKEN, bd=1)
    p_frame.grid(row=1, column=0, sticky='nsew')

    p_lable = Label(p_frame, image=photo, bg="white",
                    borderwidth=3)
    p_lable.pack(side="top", fill=BOTH,)

    t1_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    t1_frame.grid(row=2, column=0, sticky="nsew")

    marquee = Marquee(t1_frame, text="CHITKARA UNIVERSITY FOOD COURT",
                      borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    # bottom frame
    r_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    r_frame.grid(row=4, column=0, sticky='nsew')

    r_frame.grid_rowconfigure(1, weight=1)
    r_frame.grid_columnconfigure(0, weight=1)

    bottom_lside_frame = Frame(r_frame, bg="black", relief=SUNKEN)
    bottom_lside_frame.grid(row=0, column=0, sticky='nsew')
    # bottom_lside_frame.pack(side=LEFT, fill=BOTH)

    lp_lable = Label(bottom_lside_frame, image=photo,
                     bg="white", borderwidth=3)
    lp_lable.pack(side=LEFT, fill=X)

    bottom_rside_frame = Frame(r_frame, bg="black", relief=SUNKEN)
    bottom_rside_frame.grid(row=0, column=1, sticky='nsew')
    # bottom_rside_frame.pack(side=RIGHT, fill=BOTH)

    r_button = Button(bottom_rside_frame, text="REGISTER", bg="yellow", fg="black",
                      font="times 30 bold", relief=SUNKEN, bd=4, command=register)
    r_button.grid(row=0, column=0, sticky='nsew', pady=(35, 15), padx=(5, 5))

# lg_frame = Frame(Atm_root, bg="gray5", relief=SUNKEN)
# lg_frame.grid(row=5, column=0)

    l_button = Button(bottom_rside_frame, text="LOGIN", bg="green", fg="white",
                      font="times 30 bold", relief=SUNKEN, bd=4, command=register)
    l_button.grid(row=1, column=0, sticky='nsew', pady=(17, 15), padx=(5, 5))

    # q_frame = Frame(Atm_root, bg="gray5", relief=SUNKEN)
    # q_frame.grid(row=5, column=0, sticky='e')

    q_button = Button(bottom_rside_frame, text="EXIT", bg="red", fg="white",
                      font="times 30 bold", relief=SUNKEN, bd=4, command=quit)

    q_button.grid(row=2, column=0, sticky='nsew', pady=(17, 1), padx=(5, 5))

    d_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    d_frame.grid(row=5,  sticky='nsew')

    status_label = Label(d_frame, text=(f"{dt.datetime.now():%a, %b %d %Y}"),
                         relief=SUNKEN, font="ComicSansMs 10", fg='linen', bg='gray3', bd=0.5, anchor=W)
    status_label.pack(fill=X, side=BOTTOM)

    Atm_root.mainloop()
