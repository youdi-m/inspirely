from tkinter import *

# initialize the window
root = Tk()
root.title("Paint Program")

# initialize the canvas
canvas_width = 500
canvas_height = 500
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# initialize the variables
color = "black"
line_width = 2
drawing = False

# define the functions
def start_draw(event):
    global drawing
    drawing = True

def draw(event):
    global drawing, color, line_width
    if drawing:
        if canvas.old_coords:
            x1, y1 = canvas.old_coords
        else:
            x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y
        canvas.create_line(x1, y1, x2, y2, width=line_width, fill=color)
        canvas.old_coords = x2, y2

def stop_draw(event):
    global drawing
    drawing = False
    canvas.old_coords = None

def change_color(c):
    global color
    color = c

def change_line_width(w):
    global line_width
    line_width = w

def clear_canvas():
    canvas.delete("all")

# create the buttons
color_btn1 = Button(root, bg="black", width=3, command=lambda: change_color("black"))
color_btn1.pack(side=LEFT)
color_btn2 = Button(root, bg="red", width=3, command=lambda: change_color("red"))
color_btn2.pack(side=LEFT)
color_btn3 = Button(root, bg="blue", width=3, command=lambda: change_color("blue"))
color_btn3.pack(side=LEFT)
color_btn4 = Button(root, bg="green", width=3, command=lambda: change_color("green"))
color_btn4.pack(side=LEFT)

width_btn1 = Button(root, text="Thin", command=lambda: change_line_width(2))
width_btn1.pack(side=LEFT)
width_btn2 = Button(root, text="Medium", command=lambda: change_line_width(5))
width_btn2.pack(side=LEFT)
width_btn3 = Button(root, text="Thick", command=lambda: change_line_width(10))
width_btn3.pack(side=LEFT)

clear_btn = Button(root, text="Clear", command=clear_canvas)
clear_btn.pack(side=LEFT)

# bind the canvas to the draw functions
canvas.bind("<ButtonPress-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_draw)

# start the program
root.mainloop()