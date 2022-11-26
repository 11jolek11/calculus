from tkinter import *
from tkinter.ttk import *

import montecarlo
import recint
import square
import trap


class gui:
    def __init__(self):
        root = Tk()
        root.title("Calculus")
        root.geometry('350x350')

        v = IntVar()

        # Frame 'choose' and radiobuttons inside Initialization
        frame_choose = Frame(root)
        frame_choose.grid(row=0, column=0)
        choose_label = Label(frame_choose, text="Choose method:")
        choose_label.grid()
        radio_recint = Radiobutton(frame_choose, variable=v, value=0, text="Recint")
        radio_recint.grid()
        radio_montecarlo = Radiobutton(frame_choose, variable=v, value=1, text="Monte Carlo")
        radio_montecarlo.grid()
        radio_trap = Radiobutton(frame_choose, variable=v, value=2, text="Trap")
        radio_trap.grid()
        radio_square = Radiobutton(frame_choose, variable=v, value=3, text="Square")
        radio_square.grid()

        # Frame "x" and entries inside init

        frame_x = Frame(root)
        frame_x.grid(row=1, column=1)
        frame_x_title = Frame(frame_x)
        frame_x_title.grid()
        x_label = Label(frame_x_title, text="Choose start&end points:")
        x_label.grid()
        xp_label = Label(frame_x, text="xp=")
        xp_label.grid()
        xp_entry = Entry(frame_x)
        xp_entry.grid()
        xk_label = Label(frame_x, text="xk=")
        xk_label.grid()
        xk_entry = Entry(frame_x)
        xk_entry.grid()

        # Frame "entry" and "n" entry inside init

        frame_entry = Frame(root)
        frame_entry.grid(row=0, column=1)
        entry_label = Label(frame_entry, text="Entry formula: ")
        entry_label.grid()
        # entry_formula = Entry(frame_entry).insert(END, "Remember! You need specify every single math operation!")
        entry_formula = Entry(frame_entry)
        entry_formula.insert(END, "Remember! You need specify every single math operation!")
        entry_formula.grid()
        entry_n_label = Label(frame_entry, text="n=")
        entry_n_label.grid()
        entry_n = Entry(frame_entry)
        entry_n.insert(END, '1000')
        entry_n.grid()
        mainloop()


if __name__ == "__main__":
    test_object = gui()
