import tkinter, random

canvas = tkinter.Canvas(width=400,height=400)

canvas.create_line(0,200,400,200)
canvas.create_line(200,0,200,400)



def vlajka(pos,farba):
    a,b,c=farba
    x,y = pos
    x -= 10
    y -= 10
    width = 20
    height = 12
    canvas.create_rectangle(x,y,x+width,y+height/3, fill=a)
    canvas.create_rectangle(x,y+height/3,x+width,y+height/3*2, fill=b)
    canvas.create_rectangle(x,y+height/3*2,x+width,y+height, fill=c)

def main(e):
    if 0 < e.x < 200:
        if 0 < e.y < 200:
            vlajka((e.x,e.y),("blue","red", "green"))
        else:
            vlajka((e.x,e.y),("red","orange", "green"))
    else:
        if 0 < e.y < 200:
            vlajka((e.x,e.y),("orange","lime", "green"))
        else:
            vlajka((e.x,e.y),("green","orange", "green"))


canvas.bind("<Button-1>", main)




canvas.pack()
canvas.mainloop()
