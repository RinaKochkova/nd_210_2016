import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()

duma_deputyvote = []
cursor.execute('SELECT * FROM votes') # извлекли таблицу голосов депутатов по всем законопроектам
count = 1
for row in cursor.fetchall():
    duma_deputyvote.append((count,row[1],row[0],row[2]))#запихали значения в список
    count = count + 1
cursor.close()
connection.close()
print('duma_tab_datd is end')

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.executemany('INSERT INTO duma_deputyvote VALUES(?,?,?,?)',duma_deputyvote)#запихали список в таблицу другой бд
connection.commit()
cursor.close()
connection.close()