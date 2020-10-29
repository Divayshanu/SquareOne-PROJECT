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
        AttendanceOfStudent = pd.DataFrame(columns=collum_names)

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
            Detectedfaces = faceCascade.detectMultiScale(grayImg, 1.2, 5)
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
                    AttendanceOfStudent.loc[len(AttendanceOfStudent)] = [
                        Id, name, CurrentDate, timeStamp]

                else:
                    Id = 'Unknown'
                    key = str(Id)

                cv2.putText(img, str(key), (x, y+height),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            AttendanceOfStudent = AttendanceOfStudent.drop_duplicates(
                subset=['Id'], keep='first')

            cv2.imshow('Face Recognizing', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):

                break

        CurrentTime = time.time()
        CurrentDate = dt.datetime.fromtimestamp(
            CurrentTime).strftime('%Y-%m-%d')
        timeStamp = dt.datetime.fromtimestamp(
            CurrentTime).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")

        fileName = "AllData/StudentAttendance/StudentAttendance_" + \
            CurrentDate+"_"+Hour+"-"+Minute+".csv"
        AttendanceOfStudent.to_csv(fileName, index=True)
        Firebase = pyrebase.initialize_app(firebaseConfig)
        storage = Firebase.storage()
        bllob = storage.child('uploads/' + fileName).put(fileName)

        StudentData = {'name': "Date: "+CurrentDate+" Time: "+Hour+"-"+Minute+"--"+Second, 'url': "https://firebasestorage.googleapis.com/v0/b/ <gs://fir-demo-cc179.appspot.com/> %2FAttendance%5CAttendance_" +
                       CurrentDate+"_"+Hour+"-"+Minute+".csv?alt=media&token="+bllob['downloadTokens']}

        UploadDataToDatabase = firebase.post('/uploads', StudentData)
        retrivedData = AttendanceOfStudent
        StudentsPresent.configure(text=retrivedData)
        cap.release()
        cv2.destroyAllWindows()

    
firebaseConfig = {
        "apiKey": "AIzaSyABckEgLXuIltOAfKIjBH4paT3oimwelKI",
        "authDomain": "python-firebasesdkinteexample.firebaseapp.com",
        "databaseURL": "https://python-firebasesdkinteexample.firebaseio.com",
        "projectId": "python-firebasesdkinteexample",
        "storageBucket": "python-firebasesdkinteexample.appspot.com",
        "messagingSenderId": "687025953277",
        "appId": "1:687025953277:web:cafc0f5714677498562194",
        "measurementId": "G-C426GLDT23"
    }

firebase = firebase.FirebaseApplication(
        "https://python-firebasesdkinteexample.firebaseio.com/", None)
BlobStorage = Blob.from_string(
        "gs://python-firebasesdkinteexample.appspot.com")


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

