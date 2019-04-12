#!/usr/bin/python
 
from tkinter import *
from tkinter import ttk

main = Tk()
main.title('Notebook Demo')
main.geometry('600x600')

# gives weight to the cells in the grid
rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
 
# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')
 
# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)

from valves import ValvePage
from lights import LightPage
# from climate import ClimatePage

ValvePage(page1)
nb.add(page1, text='Valves')
 
# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
LightPage(page2)
nb.add(page2, text='Lights')

page3 = ttk.Frame(nb)
ValvePage(page3)
nb.add(page3, text='Climate')

main.mainloop()