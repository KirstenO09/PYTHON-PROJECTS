# Python Ver:   3.12
#
# Author:       Kirsten Osborne
#
# Purpose:      Student Tracking System. Demonstrating OOP, Tkinter GUI module,
#               and SQLite3 database integration.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Import our other modules
import student_gui
import student_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(700, 400)
        self.master.maxsize(700, 400)
        
        # Center the window on screen
        student_func.center_window(self, 700, 400)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        
        # Protocol to catch if user clicks the upper corner "X"
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        
        # Load in the GUI widgets from a separate module
        student_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
