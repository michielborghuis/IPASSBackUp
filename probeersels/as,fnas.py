from tkinter import *

import ipass5.populations

root = Tk()

country_list = ipass5.populations.list_of_countries()
clickedCountry = StringVar()
clickedCountry.set("Netherlands")
dropCountry = OptionMenu(root, clickedCountry, *country_list)
dropCountry.grid(row=10, column=1)
year_list = ipass5.populations.list_of_years()
clickedYear = StringVar()
clickedYear.set("2019")
dropYear = OptionMenu(root, clickedYear, *year_list)
dropYear.grid(row=11, column=1)

root.geometry('800x400')
root.mainloop()
