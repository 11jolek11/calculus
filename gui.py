from tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculus")
        master.geometry('850x650')
        frame_entry = Frame(master)

        entry = Entry(frame_entry)
        
        frame_choose = Frame(master)
        frame_x = Frame(master)
        frame_plot = Frame(master)
        formula = entry.get()

        radio_recint = Radiobutton(frame_choose, text="Recint")
        # print(radio_recint.state())
        radio_montecarlo = Radiobutton(frame_choose)
        radio_trap = Radiobutton(frame_choose)
        
        radio_recint.grid(row=1)
        frame_entry.grid(row=2)
        frame_choose.grid(row=3)
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
