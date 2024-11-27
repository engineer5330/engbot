import sqlite3


connection = sqlite3.connect('engineeriys.db')
cursor = connection.cursor()

cursor.execute('INSERT INTO users (name, password, datareg, iddis, idteller) VALUES (?, ?, ?, ?, ?)', ('newuser', '1234', "2001-12-12", "eng1234", "eng12341"))

connection.commit()
connection.close()