"""


"""
__author__ = "Victor Dupré, Guillaume Mairesse and Andréas Pierre"

from tkinter import *
import argparse
import random

def afficherCarte(carte,ids):
    for row in range(len(carte)):
        for col in range(len(carte[row])):
            if(carte[row][col]=='a'):
                ids[row][col] = canvas.create_rectangle(col * cell_size,
                                                        row * cell_size,
                                                        (col + 1) * cell_size,
                                                        (row + 1) * cell_size,
                                                        fill="green")
            elif(carte[row][col]=='f'):
                ids[row][col] = canvas.create_rectangle(col * cell_size,
                                                        row * cell_size,
                                                        (col + 1) * cell_size,
                                                        (row + 1) * cell_size,
                                                        fill="red")
            elif(carte[row][col]=='c'):
                ids[row][col] = canvas.create_rectangle(col * cell_size,
                                                        row * cell_size,
                                                        (col + 1) * cell_size,
                                                        (row + 1) * cell_size,
                                                        fill="grey")
            elif(carte[row][col]=='v'):
                ids[row][col] = canvas.create_rectangle(col * cell_size,
                                                        row * cell_size,
                                                        (col + 1) * cell_size,
                                                        (row + 1) * cell_size,
                                                        fill="white")

def click_callback(event):
    row = int(event.y / cell_size)
    col = int(event.x / cell_size)
    if(carte[row][col]=='a'):
        carte[row][col] = 'f'
        canvas.itemconfig(ids[row][col], fill="red")
    elif(carte[row][col]=='f'):
        carte[row][col] = 'a'
        canvas.itemconfig(ids[row][col], fill="green")



if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-rows", help="to choose the number of rows (default is 10)",default=10)
    parser.add_argument("-cols", help="to choose the number of columns (default is 10)",default=10)
    parser.add_argument("-duration", help="to choose the duration of the animation (default is 2)",default=2)
    parser.add_argument("-cell_size", help="to choose the size of the cells (default is 35)",default=35)
    parser.add_argument("-afforestation", help="to choose the percentage of afforestation (default is 0.6)",default=.6)
    parser.add_argument("-rule", help="to choose the rule (default is 1)",default=1, choices=[1,2,])
    args=parser.parse_args()

    rows = int(args.rows)
    cols = int(args.cols)
    cell_size = int(args.cell_size)
    afforestation = float(args.afforestation)
    rule = int(args.rule)

    root = Tk()
    root.title("AmazoniaBurner")
    root.resizable(width = False, height = False)

    canvas_width = cols * cell_size
    canvas_height = rows * cell_size
    canvas = Canvas(root, width = canvas_width, height = canvas_height)
    canvas.pack()

    carte = [['v' for i in range(10)] for i in range(10)]
    ids = [[0 for i in range(10)] for i in range(10)]
    for row in range(rows):
        for col in range(cols):
            if(random.random()<afforestation):
                carte[row][col] = 'a'
            
    afficherCarte(carte,ids)

    canvas.bind('<Button-1>',click_callback)

    root.mainloop()
