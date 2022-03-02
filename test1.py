import tkinter as tk
import random

canvas = tk.Canvas(width=500, height=500)
canvas.pack()

def rgb(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}"

def robot(x,y):
    x_hlava1 = x
    x_hlava2 = x+100
    y_hlava1 = y
    y_hlava2 = y+100

    canvas.create_rectangle(x_hlava1,y_hlava1 ,x_hlava2,y_hlava2, fill="gray")
    canvas.create_line((x_hlava2-x_hlava1)/2+x_hlava1,y_hlava1 ,(x_hlava2-x_hlava1)/2+x_hlava1,y_hlava1/2, fill="gray", width=5)


    canvas.create_rectangle(x_hlava1,y_hlava2, x_hlava1-50,y_hlava2+150, fill=rgb(50,50,50))
    canvas.create_rectangle(x_hlava2,y_hlava2, x_hlava2+50,y_hlava2+150, fill=rgb(50,50,50))
    
    canvas.create_rectangle(x_hlava2,y_hlava2, x_hlava1,y_hlava2+150, fill=rgb(80,80,80))

    canvas.create_text((x_hlava2-x_hlava1)/2+x_hlava1,(y_hlava2+250-y_hlava1)/2+y_hlava1, text=random.randrange(1,1000), font=("Arial", 20), fill="white")
    canvas.create_rectangle((x_hlava2-x_hlava1)/2+x_hlava1,y_hlava2+150,(x_hlava2-x_hlava1)/2+x_hlava1-50,y_hlava2+300,fill="gray")
    canvas.create_rectangle((x_hlava2-x_hlava1)/2+x_hlava1,y_hlava2+150,(x_hlava2-x_hlava1)/2+x_hlava1+50,y_hlava2+300,fill="gray")

robot(100,100)
canvas.mainloop()
