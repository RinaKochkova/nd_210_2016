import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()

def get_data():
    dep_tab = []#список id, имен и фракций депутатов
    fr_tab = []#список id и названий фракций
    vote_tab = []#список статистики голосования по каждому депутату

    cursor.execute('SELECT * FROM factions')
    for row in cursor.fetchall():
        fr_tab.append([row[0],row[1]])#заполняю список id и названий фракций

    cursor.execute('SELECT * FROM deputies')
    for row in cursor.fetchall():
        dep_tab.append([row[0],row[1],row[2]])#заполняю список  депутатов




    duma_deputy = []

    for i in range(len(dep_tab)):
        cursor.execute('SELECT vote FROM votes WHERE deputy_id = {0}'.format(dep_tab[i][0]))
        dep_votes = list(cursor.fetchall())  # ('vote', )
        dep_votes = list(map(lambda x: x[0], dep_votes))
        lifetime = len(dep_votes)
        absent_number = dep_votes.count('none')
        accept = dep_votes.count('accept')
        denied =dep_votes.count('decline')
        refrain = dep_votes.count('abstain')
        appearance = lifetime - absent_number
        accept_percantage = accept / appearance  # процент голосов "за"
        denied_percantage = denied / appearance  # "против"
        refrain_percantage = refrain / appearance  # "воздержался"
        absent_percantaige = absent_number / lifetime  # "отсутствовал"
        appearance_percantaige = appearance / lifetime  # "не голосовал"
        protest_level = 0  # надо допилить
        faction_protest_level = 0
        duma_deputy.append((int(i+1), dep_tab[i][1], lifetime, appearance, absent_number, accept_percantage,
                            denied_percantage, refrain_percantage, absent_percantaige, appearance_percantaige,
                            protest_level, faction_protest_level, int(dep_tab[i][2])))
        print(i)
    return (duma_deputy)

duma_deputy_stat = get_data()
print(duma_deputy_stat)
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.executemany('INSERT INTO duma_deputy VALUES ( ?,?,?,?,?,?,?,?,?,?,?,?,?)',duma_deputy_stat) #запихали в таблицу
connection.commit()
cursor.close()
connection.close()