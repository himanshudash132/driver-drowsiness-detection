import tkinter as tk
import customtkinter as ctk
#  python app.py

import torch
import numpy as np

import cv2
from PIL import Image, ImageTk

app = tk.Tk()
app.geometry("600x600")
app.title("drowsiness detection app 1.0")
ctk.set_appearance_mode("dark")


vidFrame = tk.Frame(height=480, width=600)
vidFrame.pack()
vid = ctk.CTkLabel(vidFrame)
vid.pack()

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp7/weights/last.pt', force_reload=True)
cap = cv2.VideoCapture(0)
def detect():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())

    imgarr =  Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(imgarr)
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10, detect)

detect()
app.mainloop()
