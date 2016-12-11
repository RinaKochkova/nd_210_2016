import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()

cursor.execute('SELECT vote FROM votes')
vote =[]
for row in cursor.fetchall():
    vote.append(row[0])
absent = vote.count('none')
all =len(vote)
acc = vote.count('accept')
den = vote.count('decline')
ref = vote.count('abstain')
app = all -absent
cursor.close()
connection.close()

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
stat = [1,app,acc/app,den/app,ref/app,absent/all,app/all]
cursor.execute('INSERT INTO duma_overallstats  VALUES ( ?,?,?,?,?,?,?)',stat)
connection.commit()
cursor.close()
connection.close()

