from tkinter import *
import recint, montecarlo, trap, square
from tkinter.ttk import *

root = Tk()
root.title("Calculus")
root.geometry('350x350')

v = IntVar()

# Frame choose and buttons inside init
frame_choose = Frame(root)
frame_choose.grid()
choose_label = Label(frame_choose, text="Choose method:")
choose_label.grid()
radio_recint = Radiobutton(frame_choose, variable=v, value=0, text="Recint")
radio_recint.grid()
radio_montecarlo = Radiobutton(frame_choose,variable=v, value=1, text="Monte Carlo")
radio_montecarlo.grid()
radio_trap = Radiobutton(frame_choose,variable=v, value=2, text="Trap")
radio_trap.grid()
radio_square = Radiobutton(frame_choose,variable=v, value=3, text="Square")
radio_square.grid()


# Frame x and entries inside init

frame_x = Frame(root)
frame_x.grid()
frame_x_title = Frame(frame_x)
frame_x_title.grid(row = 0)
x_label = Label(frame_x_title, text="Choose start&end points:")
x_label.grid()
xp_label = Label(frame_x, text="xp=")
xp_label.grid(row = 1, column=0)
xp_entry = Entry(frame_x)
xp_entry.grid(row = 1, column=1)
xk_lable = Label(frame_x, text="xk=")
xk_lable.grid(row = 2, column=0)
xk_entry = Entry(frame_x)
xk_entry.grid(row = 2, column=1)


# Frame Entry and n iniside init

frame_entry = Frame(root)
frame_entry.grid()
entry_label = Label(frame_entry, text="Entry formula: ")
entry_label.grid(row = 0)
entry_formula = Entry(frame_entry).insert(END, "Remember! You need specify every single math operation!")
entry_formula.grid(row = 1)
entry_n_label = Label(frame_entry, text="n=")
entry_n_label.grid()
entry_n = Entry(frame_entry)
entry_n.insert(END, '1000')
entry_n.grid()


# Test: radiobuttons:
# choose_label.grid()
# radio_recint.grid()
# radio_montecarlo.grid()
# radio_trap.grid()
# radio_square.grid()
# frame_choose.grid()

# Test: X Entries:

# x_label.grid()
# frame_x_title.grid()

# xp_label.grid(row = 1, column=0)
# xp_entry.grid(row = 1, column=1)

# xk_lable.grid(row = 2, column=0)
# xk_entry.grid(row = 2, column=1)

# x_label.grid()
# frame_x_title.grid(row = 0)

# frame_x.grid()

# Test: n & formula entrie:
# frame_entry.grid()


# entry_label.grid(row = 0)
# entry_formula.grid(row = 1)

# entry_n_label.grid()
# entry_n.grid()

# frame_entry.grid()


mainloop()
