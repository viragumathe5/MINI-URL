import sys
from tkinter import *
from webbrowser import *



tab = Tk()
g1int= StringVar()
tab.title("MINI URL")
tab.geometry('300x150')


def opn_url():
    g2int = g1int.get()
    type(g2int)
    
    try:
        webbrowser.open(g2int)
        
    except:
        tab_1 = tk()
        tab_1.title('error')
        tab_1.geometry('150x150')
        lbl_2 = Label(tab_1, text = "Invalid inputs").pack()
      


lbl_1 = Label(tab, text = "GET SITE").pack()
g_entry = Entry(tab, textvariable = g1int).pack()
button_1 = Button(tab, text = "SEARCH", fg = "red", command = opn_url).pack()

tab.mainloop()
