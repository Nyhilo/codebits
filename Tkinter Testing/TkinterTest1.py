from tkinter import *

tk = Tk()
canvas_width = 400
canvas_height = 200
square_size = 20

w = Canvas(tk, width=canvas_width, height=canvas_height)
w.pack()

def draw_rectangle(posx, posy, color):
    # x = posx * square_size
    # y = posy * square_size
    w.create_rectangle(posx, posy, 10, 10, fill=color)


def main():
    hexes = ["#4e10e9", 
             "#e3a90a", 
             "#4f15de", 
             "#8bc703", 
             "#174a26"]

    index = 0
    while index < len(hexes):
        print(index, len(hexes), hexes[index])
        w.create_rectangle(index*10,index*10,20,20,fill=hexes[index])
        index += 1

    mainloop()


if __name__ == '__main__':
    main()