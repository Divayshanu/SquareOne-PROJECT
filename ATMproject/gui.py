import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk

class Marquee(Canvas):
    def __init__(self, parent, text, margin=3, borderwidth=2, relief='flat', bg="red", fps=300):
        Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief, bg="red")
        self.fps = fps
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))
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

    Atm_root.geometry("1000x700")
    Atm_root.configure(background='gray5', bd=1, relief=SUNKEN)
    Atm_root.minsize(1000, 700)
    Atm_root.maxsize(1000, 700)
    Atm_root.title("Chitkara ATM")
    Atm_root.iconbitmap('ATM-icon.icns')

    photo = PhotoImage(file="cu_image1.png")

    t_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    t_frame.grid(row=0, column=0, sticky="nsew")

    Atm_root.grid_rowconfigure(1, weight=1)
    Atm_root.grid_columnconfigure(0, weight=1)
    

    marquee = Marquee(t_frame, text="WELCOME TO CHITKARA UNIVERSITY ATM", borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    p_frame = Frame(Atm_root, bg="black", relief=SUNKEN, bd=1)
    p_frame.grid(row=1, column=0, sticky='nsew')

    p_lable = Label(p_frame,image=photo, bg="white", borderwidth=3)
    p_lable.pack(side="top", fill=X)

    l_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    l_frame.grid(row=3, column=0)

    t1_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    t1_frame.grid(row=2, column=0, sticky="nsew")

    marquee = Marquee(t1_frame, text="CHITKARA UNIVERSITY FOOD COURT", borderwidth=2, relief="sunken", bg="red")
    marquee.pack(side="top", fill=X, expand=True)

    l_lable = Label(l_frame,text="KHAO...", font=("times", 50, "bold"), padx=10,pady=10, borderwidth=2, relief="sunken", bg="red", fg="white")
    l_lable.pack(fill=X)

    l1_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    l1_frame.grid(row=4, column=0, sticky='w')

    l1_lable = Label(l1_frame,text="PIYO...", font=("times", 50, "bold"), padx=150, pady=10, borderwidth=2, relief="sunken", bg="red", fg="white")
    l1_lable.pack()

    l2_frame = Frame(Atm_root, bg="black", relief=SUNKEN)
    l2_frame.grid(row=4, column=0, sticky='e')

    l2_lable = Label(l2_frame,text="AISH KRO...", font=("times", 50, "bold"), padx=90, pady=10, relief="sunken", bg="red", fg="white")
    l2_lable.pack()

    r_frame = Frame(Atm_root, bg="gray5", relief=SUNKEN)
    r_frame.grid(row=5, column=0, sticky='sew')

    r_button = Button(r_frame, text="REGISTER", bg="gray5", fg="red", font="times 50 bold", relief=SUNKEN, bd=4, command=register)
    r_button.pack()

    lg_frame = Frame(Atm_root, bg="gray5", relief=SUNKEN)
    lg_frame.grid(row=5, column=0)

    l_button = Button(lg_frame, text="LOGIN", bg="blue", fg="white", font="times 50 bold", relief=SUNKEN, bd=4, command=register)


    q_frame = Frame(Atm_root, bg="gray5", relief=SUNKEN)
    q_frame.grid(row=5, column=0, sticky='e')

    q_button = Button(q_frame, text="QUIT", bg="red", fg="white", font="times 50 bold", relief=SUNKEN, bd=4, command=quit)

    q_button.pack()

    Atm_root.mainloop()