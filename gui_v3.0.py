from tkinter import *
import recint, montecarlo, trap, square
from tkinter.ttk import *

root = Tk()
root.title("Calculus")
root.geometry('350x350')

v = IntVar()

# Frame 'choose' and buttons inside init
frame_choose = Frame(root)
frame_choose.pack()
choose_label = Label(frame_choose, text="Choose method:")
choose_label.pack()
radio_recint = Radiobutton(frame_choose, variable=v, value=0, text="Recint")
radio_recint.pack()
radio_montecarlo = Radiobutton(frame_choose,variable=v, value=1, text="Monte Carlo")
radio_montecarlo.pack()
radio_trap = Radiobutton(frame_choose,variable=v, value=2, text="Trap")
radio_trap.pack()
radio_square = Radiobutton(frame_choose,variable=v, value=3, text="Square")
radio_square.pack()


# Frame "x" and entries inside init

frame_x = Frame(root)
frame_x.pack()
frame_x_title = Frame(frame_x)
frame_x_title.pack()
x_label = Label(frame_x_title, text="Choose start&end points:")
x_label.pack()
xp_label = Label(frame_x, text="xp=")
xp_label.pack()
xp_entry = Entry(frame_x)
xp_entry.pack()
xk_lable = Label(frame_x, text="xk=")
xk_lable.pack()
xk_entry = Entry(frame_x)
xk_entry.pack()


# Frame "entry" and n iniside init

frame_entry = Frame(root)
frame_entry.pack()
entry_label = Label(frame_entry, text="Entry formula: ")
entry_label.pack()
entry_formula = Entry(frame_entry).insert(END, "Remember! You need specify every single math operation!")
entry_formula.pack()
entry_n_label = Label(frame_entry, text="n=")
entry_n_label.pack()
entry_n = Entry(frame_entry)
entry_n.insert(END, '1000')
entry_n.pack()


# Test: radiobuttons:
# choose_label.pack()
# radio_recint.pack()
# radio_montecarlo.pack()
# radio_trap.pack()
# radio_square.pack()
# frame_choose.pack()

# Test: X Entries:

# x_label.pack()
# frame_x_title.pack()

# xp_label.pack(row = 1, column=0)
# xp_entry.pack(row = 1, column=1)

# xk_lable.pack(row = 2, column=0)
# xk_entry.pack(row = 2, column=1)

# x_label.pack()
# frame_x_title.pack(row = 0)

# frame_x.pack()

# Test: n & formula entrie:
# frame_entry.pack()


# entry_label.pack(row = 0)
# entry_formula.pack(row = 1)

# entry_n_label.pack()
# entry_n.pack()

# frame_entry.pack()


mainloop()
