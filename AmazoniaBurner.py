"""
The AmazoniaBurner module is used to simulate a wild fire using a celular automaton.

"""
__author__ = "Victor Dupré, Guillaume Mairesse and Andréas Pierre"

from tkinter import *
import argparse
import random

def showMap():
    """
    Show the map at the launch off the application.

    """
    for row in range(rows):
        for col in range(cols):
            if(data[row][col]=='a'):
                ids[row][col] = canvas.create_rectangle(col * cell_size,
                                                        row * cell_size,
                                                        (col + 1) * cell_size,
                                                        (row + 1) * cell_size,
                                                        fill="green")
            elif(data[row][col]=='v'):
                ids[row][col] = canvas.create_rectangle(col * cell_size,
                                                        row * cell_size,
                                                        (col + 1) * cell_size,
                                                        (row + 1) * cell_size,
                                                        fill="white")

def updateMap():
    """
    Update the map.
    
    """
    for row in range(rows):
        for col in range(cols):
            if(data[row][col]=='a'):
                canvas.itemconfig(ids[row][col],fill="green")
            elif(data[row][col]=='f'):
                canvas.itemconfig(ids[row][col],fill="red")
            elif(data[row][col]=='c'):
                canvas.itemconfig(ids[row][col],fill="grey")
            elif(data[row][col]=='v'):
                canvas.itemconfig(ids[row][col],fill="white")


def click_callback(event):
    """
    Set or extinguish fire at the position where the user has clicked.
    
    """
    row = int(event.y / cell_size)
    col = int(event.x / cell_size)
    if(data[row][col]=='a'):
        data[row][col] = 'f'
        canvas.itemconfig(ids[row][col], fill="red")
    elif(data[row][col]=='f'):
        data[row][col] = 'a'
        canvas.itemconfig(ids[row][col], fill="green")

def launch():
    """
    Used to launch and animate the simulation.
    
    """
    future_data = [['v' for i in range(cols)] for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if(data[row][col]=='a'):
                k = 0
                if(row!=rows-1 and data[row+1][col]=='f'):
                    k+=1
                if(row!=0 and data[row-1][col]=='f'):
                    k+=1
                if(col!=cols-1 and data[row][col+1]=='f'):
                    k+=1
                if(col!=0 and data[row][col-1]=='f'):
                    k+=1
                if(rule==1 and k>=1):
                    future_data[row][col] = 'f'
                elif(rule==2 and random.random()<(1-1/(k+1))):
                    future_data[row][col] = 'f'
                else:
                    future_data[row][col] = 'a'
            elif(data[row][col]=='f'):
                future_data[row][col] = 'c'
            elif(data[row][col]=='c'):
                future_data[row][col] = 'v'
            elif(data[row][col]=='v'):
                future_data[row][col] = 'v'
    for row in range(rows):
        for col in range(cols):
            data[row][col] = future_data[row][col]
    updateMap()
    root.after(int(duration*1000),launch)


if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-rows", help="to choose the number of rows (default is 10)",default=10)
    parser.add_argument("-cols", help="to choose the number of columns (default is 10)",default=10)
    parser.add_argument("-duration", help="to choose the duration of the animation (default is 2)",default=2)
    parser.add_argument("-cell_size", help="to choose the size of the cells (default is 35)",default=35)
    parser.add_argument("-afforestation", help="to choose the percentage of afforestation (default is 0.6)",default=.6)
    parser.add_argument("-rule", help="to choose the rule (default is 1)",default=1, choices=['1','2',])
    args=parser.parse_args()

    rows = int(args.rows)
    cols = int(args.cols)
    duration= float(args.duration)
    cell_size = int(args.cell_size)
    afforestation = float(args.afforestation)
    rule = int(args.rule)

    root = Tk()
    root.title("AmazoniaBurner")
    root.resizable(width = False, height = False)

    canvas_width = cols * cell_size
    canvas_height = rows * cell_size
    canvas = Canvas(root, width = canvas_width, height = canvas_height)
    canvas.grid(column=0, row=0)

    data = [['v' for i in range(cols)] for i in range(rows)]
    ids = [[0 for i in range(cols)] for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if(random.random()<afforestation):
                data[row][col] = 'a'
            
    showMap()

    canvas.bind('<Button-1>',click_callback)
    
    btnLaunch = Button(root, text = "Launch", command = launch)
    btnLaunch.grid(column=0,row=1)

    root.mainloop()
