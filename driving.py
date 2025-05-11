import sqlite3

# establish connection to films.db database
connection = sqlite3.connect("country.db")
cursor = connection.cursor()

choice = input("")
outputa = cursor.execute(f"{choice}")
connection.commit()
outputb = outputa.fetchall()
print(outputb[0])