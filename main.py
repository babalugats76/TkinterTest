# import what you use from Tkinter module
from tkinter import Tk, Frame, Button

# create top-level, instance of Tk
# represents the "main" window
root = Tk()

# configure as appropriate
# represents the "main" window
root.configure(background='black')
root.minsize(width=400, height=300)

# alternatively
root.title('My Awesome App...')
root['height'] = 300

# create widgets (Python objects)
# when instantiating, you must provide reference to parent

# use widget reference from Interwebs
# https://tcl.tk/man/tcl8.6/TkCmd/ttk_frame.htm

content = Frame(root, background='blue', borderwidth=5, relief='sunken')
content.pack(fill='both', expand=True, padx=5, pady=5)

# callback function - attach to button below

def btn_handler():
    print('handler fired...')

# https://tcl.tk/man/tcl8.6/TkCmd/ttk_button.htm

firstBtn = Button(content, text="Press Me", command=btn_handler) # create button
firstBtn['width'] = 15  # specified in text units = weird!
firstBtn.pack(fill="none", expand=True) # add to content frame

# Launch the main event loop
# Handles interactions, fires callbacks, etc.
root.mainloop()
