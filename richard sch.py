import tkinter as tk
import random

wid=600
hei=600

canvas = tk.Canvas(width=wid, height=hei)
canvas.pack()
def text(ang):
    canvas.create_text(wid/2, hei/2,text="ŤAHAŤ", font=("Arial", 30), angle=ang)

for i in range(4):
    text(45*i)
    canvas.update()
    canvas.after(500)

