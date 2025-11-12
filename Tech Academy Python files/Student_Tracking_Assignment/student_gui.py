# Python Ver:   3.12
#
# Author:       Kirsten Osborne
#
# Purpose:      Student Tracking System GUI module.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

# Import our other modules
import student_main
import student_func


def load_gui(self):
    """
    Define the default tkinter widgets and their initial
    configuration and place them using the grid geometry.
    """
    
    # Title label
    self.lbl_title = tk.Label(self.master, text='Student Tracking', font=('Arial', 16, 'bold'))
    self.lbl_title.grid(row=0, column=0, columnspan=2, padx=(27, 0), pady=(20, 20), sticky=N+W)
    
    # Form labels
    self.lbl_fname = tk.Label(self.master, text='First Name:')
    self.lbl_fname.grid(row=1, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
    
    self.lbl_lname = tk.Label(self.master, text='Last Name:')
    self.lbl_lname.grid(row=2, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
    
    self.lbl_phone = tk.Label(self.master, text='Phone Number:')
    self.lbl_phone.grid(row=3, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
    
    self.lbl_email = tk.Label(self.master, text='Email:')
    self.lbl_email.grid(row=4, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
    
    self.lbl_course = tk.Label(self.master, text='Current Course:')
    self.lbl_course.grid(row=5, column=0, padx=(27, 0), pady=(10, 0), sticky=N+W)
    
    # Entry fields
    self.txt_fname = tk.Entry(self.master, text='')
    self.txt_fname.grid(row=1, column=1, padx=(10, 40), pady=(10, 0), sticky=E+W)
    
    self.txt_lname = tk.Entry(self.master, text='')
    self.txt_lname.grid(row=2, column=1, padx=(10, 40), pady=(10, 0), sticky=E+W)
    
    self.txt_phone = tk.Entry(self.master, text='')
    self.txt_phone.grid(row=3, column=1, padx=(10, 40), pady=(10, 0), sticky=E+W)
    
    self.txt_email = tk.Entry(self.master, text='')
    self.txt_email.grid(row=4, column=1, padx=(10, 40), pady=(10, 0), sticky=E+W)
    
    self.txt_course = tk.Entry(self.master, text='')
    self.txt_course.grid(row=5, column=1, padx=(10, 40), pady=(10, 0), sticky=E+W)
    
    # Submit button
    self.btn_submit = tk.Button(self.master, width=12, height=2, text='Submit', 
                                command=lambda: student_func.addStudent(self))
    self.btn_submit.grid(row=6, column=0, columnspan=2, padx=(27, 0), pady=(20, 10), sticky=W)
    
    # Student list section label
    self.lbl_list = tk.Label(self.master, text='Student List:', font=('Arial', 12, 'bold'))
    self.lbl_list.grid(row=0, column=2, padx=(20, 0), pady=(20, 10), sticky=N+W)
    
    # Define the listbox with a scrollbar
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set, height=15, width=50)
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=4, rowspan=6, padx=(0, 20), pady=(0, 0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=6, columnspan=2, padx=(20, 0), pady=(0, 0), sticky=N+E+S+W)
    
    # Delete button
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', 
                                command=lambda: student_func.onDelete(self))
    self.btn_delete.grid(row=7, column=2, padx=(20, 0), pady=(10, 10), sticky=W)
    
    # Create database and load students
    student_func.create_db(self)
    student_func.onRefresh(self)


if __name__ == "__main__":
    pass
