import tkinter as tk
from tkinter import *
import webbrowser

#Define the main application class
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #Create and place the Entry widget for user input
        self.label = Label(self.master, text="Enter custom text:")
        self.label.grid(row=0, column=0, padx=(10,10), pady=(10,0), sticky=W)

        self.txtEntry = Entry(self.master, width=100)
        self.txtEntry.grid(row=1, columnspan=3, padx=(10,10), pady=(0,10))

        # Button to generate default HTML page
        

        self.btnDefault = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btnDefault.grid(row=2, column=1, padx=(10,10), pady=(5,5))
        # Button to generate custom HTML page using user input
        self.btnCustom = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btnCustom.grid(row=2, column=2, padx=(20,10), pady=(5,5))

    # Function to generate default HTML page

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Function to generate custom HTML page using user input
    def customHTML(self):
        userText = self.txtEntry.get()
        if not userText.strip():
            userText = "Stay tuned for our amazing summer sale!"  # fallback if input is empty
        htmlContent = f"<html>\n<body>\n<h1>{userText}</h1>\n</body>\n</html>"
        with open("index.html", "w") as htmlFile:
            htmlFile.write(htmlContent)
        webbrowser.open_new_tab("index.html")

            

if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


