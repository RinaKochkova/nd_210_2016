import sqlite3
import json
import urllib.request
import os.path

conn = sqlite3.connect('duma.db')  # создание коннекта
c = conn.cursor()  # создание курсора


def drop_table_deputies():  # удаление таблицы, если она есть
    conn.execute('DROP TABLE IF EXISTS deputies')


def drop_table_factions():
    conn.execute('DROP TABLE IF EXISTS factions')


def drop_table_laws():
    conn.execute('DROP TABLE IF EXISTS laws')


def drop_table_votes():
    conn.execute('DROP TABLE IF EXISTS votes')


def create_table_deputies():  # создание таблицы, если её нет
    c.execute(
        """CREATE TABLE IF NOT EXISTS deputies(deputy_id INTEGER PRIMARY KEY, name VARCHAR(50), faction_id INTEGER, FOREIGN KEY(faction_id) REFERENCES factions(faction_id))""")


def create_table_factions():
    c.execute("""CREATE TABLE IF NOT EXISTS factions(faction_id INTEGER PRIMARY KEY, title VARCHAR(4))""")


def create_table_laws():
    c.execute(
        """CREATE TABLE IF NOT EXISTS laws(law_id INTEGER PRIMARY KEY, title VARCHAR(1000), aszdUrl VARCHAR(200), date_time DATE)""")


def create_table_votes():
    c.execute(
        """CREATE TABLE IF NOT EXISTS votes(deputy_id INTEGER, vote VARCHAR(7), law_id INTEGER, FOREIGN KEY (deputy_id) REFERENCES deputies(deputy_id), FOREIGN KEY (law_id) REFERENCES laws(law_id))""")


def data_entry_deputies(listed_data):  # добавление информации в таблицу из списка
    c.executemany("INSERT INTO deputies VALUES(deputy_id, name, faction_id)", listed_data)
    conn.commit()


def data_entry_factions(listed_data_factions):
    c.executemany("INSERT INTO factions VALUES(faction_id, title)", listed_data_factions)
    conn.commit()


def data_entry_laws(listed_data_laws):
    c.executemany('INSERT INTO laws VALUES(law_id, title, aszdUrl, date_time)', listed_data_laws)
    conn.commit()


def data_entry_votes(listed_data_votes):
    c.executemany('INSERT INTO votes VALUES(deputy_id, vote, law_id)', listed_data_votes)
    conn.commit()


def read_from_deputies():  # вывод всей таблицы на экран
    c.execute("SELECT * FROM deputies")
    for row in c.fetchall():
        print(row)


def read_from_factions():
    c.execute("SELECT * FROM factions")
    for row in c.fetchall():
        print(row)


def read_from_laws():
    c.execute("SELECT * FROM laws")
    for row in c.fetchall():
        print(row)


def get_data():
        urlData1 = "D:\\poll1"
        urlJson = 75687
        listed_data_laws = []
        listed_data_votes = []
        listed_data_deputies = set()
        listed_data_factions = set()
        percent = 0
        while urlJson <= 96003:
            new_percent = round((((urlJson - 75687) / (96003 - 75687)) * 100), 1)
            if new_percent != percent:
                print(str(new_percent) + "%")
                percent = new_percent
            urlJson += 1
            urlData2 = (urlData1 + "\\" + str(urlJson) + ".json")
            if os.path.isfile(urlData2):
                with open(urlData2, encoding='utf-8') as f:
                    data1 = json.loads(f.read())
                    listed_data_laws.append([data1['id'], data1['title'], data1['asozdUrl'], data1['datetime']])
                    q = data1['id']
                    for d in data1['votes']:
                        listed_data_votes.append([d['deputy']['id'], d['result'], q])
                        listed_data_deputies.add((d['deputy']['id'], d['deputy']['name'], d['deputy']['faction']['id']))
                        listed_data_factions.add((d['deputy']['faction']['id'], d['deputy']['faction']['title']))
        return listed_data_laws, listed_data_votes, listed_data_deputies, listed_data_factions


laws_data, votes_data, deputies_data, factions_data = get_data()

drop_table_laws()
create_table_laws()
data_entry_laws(laws_data)
print('TABLE LAWS IS DONE')

drop_table_votes()
create_table_votes()
data_entry_votes(votes_data)
print('TABLE VOTES IS DONE')

drop_table_deputies()
create_table_deputies()
data_entry_deputies(deputies_data)
print('TABLE DEPUTIES IS DONE')

drop_table_factions()
create_table_factions()
data_entry_factions(factions_data)
print('TABLE FACTIONS IS DONE')

c.close()
conn.close()



