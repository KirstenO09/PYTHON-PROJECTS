import sqlite3

connection = sqlite3.connect("D:/Python/Tech Academy Python files/sqlite_assignment/test_database.db")
c = connection.cursor()
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
c.dxecute("INSERT INTO People VALUES('Ron','Obvious', 42")
connection = sqlite3.connect(':memory:')
c.execute("DROP TABLE IF EXISTS People")

connection.close

with sqlite3.connect("test_database.db") as connection:
    # perform any SQL operations using connection here
