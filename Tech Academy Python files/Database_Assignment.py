# Import the sqlite3 module to work with SQLite databases

import sqlite3

# Connect to (or create) the database named 'files.db'
conn = sqlite3.connect('files.db')

# Create a table with two fields: an auto-incrementing ID and a text field for file names
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
conn.close()

# Reconnect to the same database to insert data
conn = sqlite3.connect('files.db')

# Define the list of file names as provided in the assignment
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data,pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
     # Loop through each file name in the list

for file in fileList:
    # Check if the file ends with '.txt'
        if file.endswith('.txt'):
            # Insert the qualifying file name into the database
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (file,))
            
        conn.commit()
conn.close()            

# Reconnect to the database to retrieve and print the stored .txt file names
conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    # Select all file names from the table
    
    cur.execute("SELECT col_file FROM tbl_files")
    varFiles = cur.fetchall() # Fetch all matching rows

     # Print each qualifying text file name legibly
    for item in varFiles:
        print(f"Text File: {item[0]}!")

