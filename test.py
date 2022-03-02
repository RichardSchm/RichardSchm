import tkinter as tk
import random

canvas = tk.Canvas(width=500,height=500)

canvas.pack()
def rgb(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}"
#print(rgb(200,200,200))
#gulička
def gulicka(x1,y1):
    x2=x1+30
    y2=y1+30
    canvas.create_oval(x1,y1,x2,y2,fill=rgb(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
for i in range(5):
    gulicka(20,40*i+20)

#čiary
def ciara(x2,y2, size):
    y1=y2-size
    canvas.create_line(x2,y1,x2,y2)

for x in range(4):
    ciara(70+x*5,150, 100-x*5)
#Nextčiary
def nextciary(x1,y1, size):
    x2 = x1 + 100
    y2 = y1 + size/5
    canvas.create_line(x1,y1,x2,y2)
for z in range(4):
    nextciary(150,50+z*4, 70+z*7)
#schody
def schod(x1,y1,size):
    x2= x1+size
    y2= y1+size
    canvas.create_line(x1,y1,x2,y1,x2,y1,x2,y2)
i = 0
for i in range(10):
    schod(200+i*10, 200+i*10, 10)
canvas.mainloop()
