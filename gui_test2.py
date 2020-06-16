from tkinter import *
import recint, montecarlo, trap, square
# import matplotlib


class GUI:
    # def calculate(self):
    #     if v is 0:
    #         test_object = recint.RecInt(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
    #         print(test_object.start())
    #     elif v is 1:
    #         test_object = montecarlo.MonteCarlo(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
    #         print(test_object.start())
    #     elif v is 2:
    #         test_object = trap.Trap(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
    #         print(test_object.start())
    #     elif v is 3:
    #         test_object = square.Square(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
    #         print(test_object.start())
    #     else:
    #         print("Give me data!")

    def __init__(self, master):
        self.master = master
        master.title("Calculus")
        master.geometry('850x650')
        frame_entry = Frame(master)
        v = IntVar()
        entry = Entry(frame_entry)
        entry_n_label = Label(self.frame_entry, text="n=")
        entry_n = Entry(self.frame_entry)
        entry_n.insert(END, '1000')
        
        frame_choose = Frame(master)
        frame_x = Frame(master)
        frame_plot = Frame(master)

        choose_label = Label(frame_choose, text="Choose method:")
        radio_recint = Radiobutton(frame_choose, variable=v, value=0, text="Recint")
        radio_montecarlo = Radiobutton(frame_choose,variable=v, value=1, text="Monte Carlo")
        radio_trap = Radiobutton(frame_choose,variable=v, value=2, text="Trap")
        radio_square = Radiobutton(frame_choose,variable=v, value=3, text="Square")
# Works:
    # def calculate(self):
    #     if self.v == 0:
    #         test_object = recint.RecInt(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
    #         print(test_object.start())
    #     elif self.v == 1:
    #         test_object = montecarlo.MonteCarlo(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
    #         print(test_object.start())
    #     elif self.v == 2:
    #         test_object = trap.Trap(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
    #         print(test_object.start())
    #     elif self.v == 3:
    #         test_object = square.Square(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
    #         print(test_object.start())
    #     else:
    #         print("Give me data!")


        # submit_button = Button(root, text="Submit", command=calculate)

        # entry_label = Label(self.frame_entry, text="Entry formula: ")

        x_label = Label(self.frame_x, text="Choose start&end points:")
        xp_label = Label(self.frame_x, text="xp=")
        xk_lable = Label(self.frame_x, text="xk=")
        xp_entry = Entry(self.frame_x)
        xk_entry = Entry(self.frame_x)
        x_label.grid(row = 0, column=0)
        xp_label.grid(row = 1, column=0)
        xk_lable.grid(row = 2, column=0)
        xp_entry.grid(row = 1, column=1)
        xk_entry.grid(row = 2, column=1)
        # submit_button.grid(row = 100, column = 4)

    def calculate(self):
        if self.v == 0:
            test_object = recint.RecInt(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
            print(test_object.start())
        elif self.v == 1:
            test_object = montecarlo.MonteCarlo(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
            print(test_object.start())
        elif self.v == 2:
            test_object = trap.Trap(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
            print(test_object.start())
        elif self.v == 3:
            test_object = square.Square(int(self.xp_entry.get()), int(self.xk_entry.get()), self.entry.get(), int(self.entry_n.get()))
            print(test_object.start())
        else:
            print("Give me data!")

        submit_button = Button(root, text="Submit", command=calculate)


        self.entry_label.grid()
        self.entry.grid()
        self.entry_n_label.grid()
        self.entry_n.grid()
        self.choose_label.grid()
        self.radio_recint.grid()
        self.radio_montecarlo.grid()
        self.radio_trap.grid()
        self.radio_square.grid()
        self.submit_button.grid(row = 100, column = 4)
        self.frame_x.grid(row=5)
        self.frame_entry.grid(row=4)
        self.frame_choose.grid(row = 0, column = 0)
        # self.label = Label(master, text="Th== is our first GUI!")
        # self.label.pack()
        #
        # self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()
        #
        self.close_button = Button(master, text="X", command=master.quit, bg = "red")
        # self.close_button.grid(row=0, column=1)

        #  recint:0
        #  montecarlo:1
        #  trap:2
        #  square:3

        # def calculate(self):
        #     if v is 0:
        #         test_object = recint.RecInt(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
        #         print(test_object.start())
        #     elif v is 1:
        #         test_object = montecarlo.MonteCarlo(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
        #         print(test_object.start())
        #     elif v is 2:
        #         test_object = trap.Trap(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
        #         print(test_object.start())
        #     elif v is 3:
        #         test_object = square.Square(int(xp_entry.get()), int(xk_entry.get()), entry.get(), int(entry_n.get()))
        #         print(test_object.start())
        #     else:
        #         print("Give me data!")


                

root = Tk()
my_gui = GUI(root)
root.mainloop()
