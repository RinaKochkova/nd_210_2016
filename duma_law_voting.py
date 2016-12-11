import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()

cursor.execute('SELECT law_id ,title ,date_time ,all_v - all_abs ,all_a,all_d ,all_r ,all_abs ,all_v - all_abs,all_v FROM '
               '(((((((SELECT law_id,title,date_time FROM laws) AS law_tab) '
               'LEFT JOIN (SELECT COUNT(votes.vote) AS all_v ,law_id AS l_v FROM votes GROUP BY votes.law_id)  AS all_votes ON law_tab.law_id = all_votes.l_v)'
               'LEFT JOIN (SELECT COUNT(votes.vote) AS all_a,law_id AS l_a FROM votes WHERE votes.vote = "accept" GROUP BY votes.law_id) AS overall_accept ON law_tab.law_id = overall_accept.l_a)'
               'LEFT JOIN (SELECT COUNT(votes.vote) AS all_d,law_id AS l_d FROM votes WHERE votes.vote = "decline" GROUP BY votes.law_id) AS overall_denied ON law_tab.law_id = overall_denied.l_d)'
               'LEFT JOIN (SELECT COUNT(votes.vote) AS all_r,law_id AS l_r FROM votes WHERE votes.vote = "abstain" GROUP BY votes.law_id) AS overall_refrain ON law_tab.law_id = overall_refrain.l_r)'
               'LEFT JOIN (SELECT COUNT(votes.vote) AS all_abs,law_id AS l_abs FROM votes WHERE votes.vote = "none" GROUP BY  votes.law_id) AS overall_abstain ON law_tab.law_id = overall_abstain.l_abs) AS stat')
stat =[]
for row in list(cursor.fetchall()):
    if row[3] == None:
        appearance = 0
    else:
        appearance =row[3]

    if row[4] == None:
        accept = 0
    else:
        accept =row[4]

    if row[5] == None:
        denied = 0
    else:
        denied =row[5]

    if row[6] == None:
        refrain = 0
    else:
        refrain =row[6]

    if row[7] == None:
        absent = 0
    else:
        absent =row[7]

    if appearance == 0:
        dev_app = 1
    else:
        dev_app = appearance
    if row[9]==None:
        dev_allvote = 1
    else:
        dev_allvote =row[9]

    stat.append((row[0],row[1],row[2],appearance,accept/dev_app,denied/dev_app,refrain/dev_app,absent/dev_allvote,appearance/dev_allvote))

cursor.close()
connection.close()

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.executemany('INSERT INTO duma_lawvoting  VALUES ( ?,?,?,?,?,?,?,?,?)',stat)  # запихали в таблицу
connection.commit()
cursor.close()
connection.close()






