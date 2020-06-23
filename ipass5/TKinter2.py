from tkinter import *
from ipass5.TKinter import GUI


class MainGUI:
    def __init__(self):
        self.root = Tk()

        self.label1 = Label(self.root, text='Advanced SIR model for disease spread.',
                            font=('Calibri', 20)).grid(row=0, columnspan=2)
        self.label2 = Label(self.root, text='Would you like to enter the population manually or to choose a country and'
                                            ' a year corresponding to a population?').grid(row=1, columnspan=2)
        self.buttonManually = Button(self.root, text='Manually', command=self.open_manually).grid(row=2, column=0)
        self.buttonAutomatic = Button(self.root, text='Automatic', command=self.open_automatic).grid(row=2, column=1)

    def open_automatic(self):
        automatic = GUI(0)
        automatic.run()

    def open_manually(self):
        manually = GUI(1)
        manually.run()

    def close(self):
        self.root.destroy()

    def run(self):
        self.root.geometry('610x400')
        self.root.iconbitmap('COVID-19_icon.ico')
        self.root.mainloop()

if __name__ == '__main__':
    b = MainGUI()
    b.run()
