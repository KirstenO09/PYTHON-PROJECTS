# Python Ver:   3.12
#
# Author:       Kirsten Osborne
#
# Purpose:      Student Tracking System functions module.
#
# Tested OS:    This code was written and tested to work with Windows 10.

import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Import our other modules
import student_main
import student_gui


def center_window(self, w, h):
    """Center the application window on the user's screen"""
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    """Confirm before closing the application"""
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)


def create_db(self):
    """Create the database and table if they don't exist"""
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()


def addStudent(self):
    """Add a new student to the database"""
    # Get values from entry fields
    var_fname = self.txt_fname.get().strip().title()
    var_lname = self.txt_lname.get().strip().title()
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    
    # Validate that all fields have data
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and \
       (len(var_email) > 0) and (len(var_course) > 0):
        
        conn = sqlite3.connect('db_students.db')
        with conn:
            cursor = conn.cursor()
            # Insert the new student into the database
            cursor.execute("""INSERT INTO tbl_students (col_fname, col_lname, col_phone, col_email, col_course) 
                           VALUES (?,?,?,?,?)""", (var_fname, var_lname, var_phone, var_email, var_course))
            conn.commit()
        conn.close()
        
        # Clear the form and refresh the list
        onClear(self)
        onRefresh(self)
        messagebox.showinfo("Success", "Student added successfully!")
    else:
        messagebox.showerror("Missing Information", "Please ensure that all fields are filled out.")


def onDelete(self):
    """Delete the selected student from the database"""
    try:
        # Get the selected item from the listbox
        var_select = self.lstList1.get(self.lstList1.curselection())
        
        # Extract the student ID from the selection (format: "ID: 1 - John Doe...")
        student_id = var_select.split(':')[1].split('-')[0].strip()
        
        confirm = messagebox.askokcancel("Delete Confirmation", 
                                        "The selected student will be permanently deleted from the database.\n\nProceed with deletion?")
        if confirm:
            conn = sqlite3.connect('db_students.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute("""DELETE FROM tbl_students WHERE ID = ?""", (student_id,))
                conn.commit()
            conn.close()
            
            # Refresh the list
            onRefresh(self)
            messagebox.showinfo("Success", "Student deleted successfully!")
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a student from the list to delete.")


def onClear(self):
    """Clear all entry fields"""
    self.txt_fname.delete(0, END)
    self.txt_lname.delete(0, END)
    self.txt_phone.delete(0, END)
    self.txt_email.delete(0, END)
    self.txt_course.delete(0, END)


def onRefresh(self):
    """Refresh the student list from the database"""
    self.lstList1.delete(0, END)
    conn = sqlite3.connect('db_students.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT ID, col_fname, col_lname, col_phone, col_email, col_course 
                       FROM tbl_students ORDER BY col_lname, col_fname""")
        students = cursor.fetchall()
        
        for student in students:
            # Format: "ID: 1 - John Doe | Phone: 555-1234 | Email: john@email.com | Course: Python"
            display_text = "ID: {} - {} {} | Phone: {} | Email: {} | Course: {}".format(
                student[0], student[1], student[2], student[3], student[4], student[5])
            self.lstList1.insert(END, display_text)
    conn.close()


if __name__ == "__main__":
    pass
