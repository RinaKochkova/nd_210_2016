import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()

cursor.execute('SELECT vote FROM votes')
overall_stat = []
for row in cursor.fetchall():
    overall_stat.append(row)

accept_per = 0
denied_per = 0
refrain_per = 0
absent_per = 0
appearance_per = 0
for row in overall_stat:
    if row[0] == 'none':
        absent_per = absent_per + 1
    elif row[0] == 'accept':
        accept_per = accept_per + 1
    elif row[0] == 'decline':
        denied_per = denied_per + 1
    elif row[0] == 'abstain':
        refrain_per = refrain_per +1
appearance = len(overall_stat) - absent_per
accept_per = accept_per / appearance
denied_per = denied_per / appearance
refrain_per = refrain_per/appearance
absent_per =  absent_per/ len(overall_stat)
appearance_per = appearance / len(overall_stat)

cursor.close()
connection.close()

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
data = [1,appearance,accept_per,denied_per,refrain_per,absent_per,appearance_per]
cursor.execute('INSERT INTO duma_overallstats VALUES (?,?,?,?,?,?,?)',data)
connection.commit()
cursor.close()
connection.close()