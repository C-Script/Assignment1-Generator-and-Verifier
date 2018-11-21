from tkinter import *
from tkinter import ttk
from main import main

window= Tk() #has the property of all stuff in tkinter

window.style=ttk.Style()

window.title ("CRC")

window.wm_state('zoomed')

label=Label(text='Get Generator input from a text file',font='sans-serif 20 bold'
            ,fg='#666666',pady=30
)

label.pack()
label.grid(column=0, row=0)
window.columnconfigure(0, weight=1)



button=Button (master=window,text='Select File',command=lambda :main(window),bg='#EA5E3D',activebackground='#000000',fg='#FFFFFF',activeforeground='#FFFFFF',font="Helvetica 20",width=30,height=1)
button.grid(column=0,row=1)


window.mainloop()
