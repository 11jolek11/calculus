import recint, montecarlo, trap, matplotlib
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('850x650')
window.title("Calculus")

frame_entry = Frame(window)
frame_choose = Frame(window)
frame_x = Frame(window)
frame_plot = Frame(window)

entry = Entry(frame_entry)
formula = entry.get()
radio_recint = Radiobutton(frame_choose, text="Recint")
# print(radio_recint.state())
radio_montecarlo = Radiobutton(frame_choose)
radio_trap = Radiobutton(frame_choose)

entry.pack()
radio_recint.pack()
frame_entry.pack()
frame_choose.pack()

window.mainloop()

