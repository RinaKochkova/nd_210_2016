import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()

def drop_table_faction_vote():  # удаление таблицы, если она есть
    cursor.execute('DROP TABLE IF EXISTS faction_vote')
def create_table_deputies():  # создание таблицы, если её нет
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS faction_vote(faction_id INTEGER, vote VARCHAR(50), law_id INTEGER)""")


drop_table_faction_vote()
create_table_deputies()
dvl=[]

cursor.execute('SELECT * FROM votes')
for row in cursor.fetchall():
    dvl.append([row[0],row[1],row[2]])

duma_faction_votes = []
for i in range(len(dvl)):
    cursor.execute('SELECT faction_id FROM deputies WHERE deputy_id = {0}'.format(dvl[i][0]))
    fac = list(cursor.fetchall())
    fact = list(map(lambda x: x[0], fac))
    duma_faction_votes.append((fact[0],dvl[i][1],dvl[i][2]))
cursor.executemany('INSERT INTO faction_vote VALUES ( ?,?,?)',duma_faction_votes)  # запихали в таблицу
cursor.close()
connection.commit()
connection.close()

