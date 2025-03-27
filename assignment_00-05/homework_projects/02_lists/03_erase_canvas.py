# Problem Statement:

# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CELL_SIZE = 30
ERASER_SIZE = 30

def erase(event):
    """Erase cells in contact with the eraser"""
    x, y = event.x, event.y
    canvas.create_rectangle(x, y, x + ERASER_SIZE, y + ERASER_SIZE, fill="white", outline="white")

root = tk.Tk()
root.title("Eraser on Canvas")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

canvas.bind("<B1-Motion>", erase)

root.mainloop()
