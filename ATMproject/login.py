import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime as dt
from subprocess import Popen
import sys
from cv2 import cv2
import os
import csv
import pandas as pd
import time
import tkinter.font as font
import pyrebase
from firebase import firebase
from google.cloud import storage
from google.cloud.storage.blob import Blob
import tkinter.filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from subprocess import Popen
import sys
import sqlite3

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
    FaceRecognize = cv2.face.LBPHFaceRecognizer_create()
    FaceRecognize.read("AllData/TrainedData/DataTrained.yml")
    harcascadeFilePath = "AllData/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadeFilePath)
    datafile = pd.read_csv("AllData/StudentDataRecord.csv")
    collum_names = ['Id', 'Name', 'Date', 'Time']
    LoginStudent = pd.DataFrame(columns=collum_names)

        

    cap = cv2.VideoCapture(0)
    if(cap.isOpened() == False):
        messagebox.showerror(title="Error", message="There is some problem with your camera"
                                 )
        root.destroy()

    while True:
        _, img = cap.read()
        if(_ == False):
            messagebox.showerror(title="Error", message="You have to close video running on home page or select image checkbox"
                                     )
            root.destroy()
            break

        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        Id = 0
        Detectedfaces = faceCascade.detectMultiScale(grayImg, 1.2,10)
        for(x, y, width, height) in Detectedfaces:
            cv2.rectangle(img, (x, y), (x+width, y+height), (225, 0, 0), 2)
            Id, confidence = FaceRecognize.predict(
                grayImg[y:y+height, x:x+width])

            if(confidence <= 50):
                CurrentTime = time.time()
                CurrentDate = dt.datetime.fromtimestamp(
                    CurrentTime).strftime('%Y-%m-%d')
                timeStamp = dt.datetime.fromtimestamp(
                    CurrentTime).strftime('%H:%M:%S')
                name = datafile.loc[datafile['Id'] == Id]['Name'].values
                key = str(Id)+"-"+name
                LoginStudent.loc[len(LoginStudent)] = [
                    Id, name, CurrentDate, timeStamp]


            else:
                Id = 'Unknown'
                key = str(Id)

            cv2.putText(img, str(key), (x, y+height),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        LoginStudent = LoginStudent.drop_duplicates(
            subset=['Id'], keep='first')

        cv2.imshow('Face Recognizing', img)
            

        if cv2.waitKey(1) & 0xFF == ord('q'):

            if Id != 'Unknown':
                my_conn = sqlite3.connect('SquareOne.db')
                my_conn.execute(''' UPDATE IdName SET id = %s'''%(Id))
                my_conn.commit()

            if Id != 'Unknown':
                
                res = messagebox.askquestion(title="Congratulation", message="WELCOME TO SQUARE ONE \n Press Yes To Proceed")

                if res =="yes":
                    root.destroy()
                    Popen([sys.executable, "./mainpage.py"])
                else:
                    root.destroy()
                    Popen( [sys.executable, "./gui.py"])

            
            break        
    
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    root = Tk()
    root.title("Login")
    root.configure(background='gray5', bd=1, relief=SUNKEN,)
    root.geometry('698x287')
    root.minsize(698, 287)
    root.maxsize(698, 287)
    

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

    headingLabel = tk.Label(center, text="LOGIN  \n After Scan press 'Q' for Proceed",
                            bg="lavender", fg="yellow4", relief=SUNKEN, width=49, height=6, font=('ComicSansMs', 21, 'bold'), anchor=CENTER)

    headingLabel.pack(fill=X)

    l_button = Button(bottom_rside_frame, text="Scan Now", highlightbackground='gold', fg="black",
                      font="times 30 bold", relief=SUNKEN, bd=2, command=scanImage)
    l_button.grid(row=1, column=0, sticky='nsew', pady=(17, 15), padx=(280, 35))


    status_label = Label(btm_frame, text=(f"{dt.datetime.now():%a, %b %d %Y}"+",BY-Divay Shanu(1710991234)"),
                         relief=SUNKEN, font="ComicSansMs 10", fg='gold2', bg='gray3', bd=0.5, anchor=W)
    status_label.pack(fill=X, side=BOTTOM)

    root.mainloop()

