from tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculus")
        master.geometry('850x650')
        frame_entry = Frame(master)
        frame_choose = Frame(master)
        frame_x = Frame(master)
        frame_plot = Frame(master)

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
        # self.label = Label(master, text="This is our first GUI!")
        # self.label.pack()
        #
        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()
        #
        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()


root = Tk()
my_gui = GUI(root)
root.mainloop()
