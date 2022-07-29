from tkinter import *
from tkinter import ttk


### How this function works:
###     bind the Text widget to Keys
###     when the key is pressed,
###     window._after_id becomes the window.after function and in 5 seconds
###     it executes dissapear function
###     window._after_id is a variable which will store a future 'after' call
def all_events(event):
    ## if id is not none, earlier after call is canceled.
    if window._after_id is not None:
        window.after_cancel(window._after_id)

    window._after_id = window.after(5000,disappear)


def disappear():
    text_area.delete('1.0',END)
    print(window._after_id)

window = Tk()
window.title('destorying text')
window.config(background='pink')

title = ttk.Label(window,text='Welcome, Eveytime you stop writing you have 5 second\n'
                              'until all your work is deleted')
title.grid(row=0)
text_area = Text(window,background='pink')
text_area.grid(row=1,pady=20,padx=20)
text_area.bind('<Key>',all_events)

window._after_id = None
window.mainloop()
