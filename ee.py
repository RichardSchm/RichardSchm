import tkinter as tk
import random
#after,update
canvas = tk.Canvas(width=400,height=300)

x1,y1=10,10
x2,y2=390,290

canvas.create_rectangle(10,10,390,290)

def gulicka(c):
    if c <= 4000:
        x = random.randint(10,390)
        y= random.randint(10,290)
        canvas.create_oval(x-5,y-5,x+5,y+5,fill="#ffffff")
    elif 4000 < c < 8000:
        x = random.randint(10,390)
        y= random.randint(145,290)
        canvas.create_oval(x-5,y-5,x+5,y+5,fill="#aa0000")
    else:
        x = random.randint(10,130)
        y = random.randint(10,290)
        if 150-x>y-145 and x<y:
            canvas.create_oval(x-5,y-5,x+5,y+5,fill="#0000aa")
for i in range(10000):
    gulicka(i)

canvas.pack()
canvas.mainloop()
