# create_db.py

import sqlite3

conn = sqlite3.connect("people.db")
print("Database created and opened successfully")

# создание таблицы с заданными полями
columns = [
	"id INTEGER PRIMARY KEY",
	"lname VARCHAR UNIQUE",
	"fname VARCHAR",
	"timestamp DATETIME",
 ]
create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
conn.execute(create_table_cmd)
print("Table created successfully")

# записываемые в базу данных персонажи
people = [
	"1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
	"2, 'Ruprecht', 'Knecht', '2022-10-08 09:15:13'",
	"3, 'Bunny', 'Easter', '2022-10-08 09:15:27'",
]
for person in people:
	insert_cmd = f"INSERT INTO person VALUES ({person})"
	conn.execute(insert_cmd)
conn.commit()
print("Records created successfully")

# проверка: вывод данных из таблицы базы данных
cur = conn.cursor()
cur.execute("SELECT * FROM person")
people = cur.fetchall()
for person in people:
	print(person)