import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()

cursor.execute('SELECT law_id ,f_i,all_v - all_abs, all_a,all_d,all_r ,all_abs ,all_v - all_abs,all_v FROM '
               '(((((((SELECT law_id FROM laws) AS law_tab) '
               'LEFT JOIN (SELECT faction_id AS f_i, COUNT(faction_vote.vote) AS all_v ,law_id AS l_v FROM faction_vote WHERE faction_vote.faction_id =72100004 GROUP BY faction_vote.law_id)  AS all_votes ON law_tab.law_id = all_votes.l_v)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_a,law_id AS l_a FROM faction_vote WHERE faction_vote.vote = "accept" AND faction_vote.faction_id =72100004 GROUP BY faction_vote.law_id) AS overall_accept ON law_tab.law_id = overall_accept.l_a)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_d,law_id AS l_d FROM faction_vote WHERE faction_vote.vote = "decline"  AND faction_vote.faction_id =72100004 GROUP BY faction_vote.law_id) AS overall_denied ON law_tab.law_id = overall_denied.l_d)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_r,law_id AS l_r FROM faction_vote WHERE faction_vote.vote = "abstain"  AND faction_vote.faction_id =72100004 GROUP BY faction_vote.law_id) AS overall_refrain ON law_tab.law_id = overall_refrain.l_r)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_abs,law_id AS l_abs FROM faction_vote WHERE faction_vote.vote = "none" AND faction_vote.faction_id =72100004 GROUP BY  faction_vote.law_id) AS overall_abstain ON law_tab.law_id = overall_abstain.l_abs) AS stat')
stat =[]
count = 0
for row in list(cursor.fetchall()):
    if row[2] == None:
        appearance = 0
    else:
        appearance =row[2]

    if row[3] == None:
        accept = 0
    else:
        accept =row[3]

    if row[4] == None:
        denied = 0
    else:
        denied =row[4]

    if row[5] == None:
        refrain = 0
    else:
        refrain =row[5]

    if row[6] == None:
        absent = 0
    else:
        absent =row[6]

    if appearance == 0:
        dev_app = 1
    else:
        dev_app = appearance

    count =count+1

    stat.append((count,appearance,accept/dev_app,denied/dev_app,refrain/dev_app,absent,72100004,row[0]))
cursor.execute('SELECT law_id ,f_i,all_v - all_abs, all_a,all_d,all_r ,all_abs ,all_v - all_abs,all_v FROM '
               '(((((((SELECT law_id FROM laws) AS law_tab) '
               'LEFT JOIN (SELECT faction_id AS f_i, COUNT(faction_vote.vote) AS all_v ,law_id AS l_v FROM faction_vote WHERE faction_vote.faction_id =72100005 GROUP BY faction_vote.law_id)  AS all_votes ON law_tab.law_id = all_votes.l_v)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_a,law_id AS l_a FROM faction_vote WHERE faction_vote.vote = "accept" AND faction_vote.faction_id =72100005 GROUP BY faction_vote.law_id) AS overall_accept ON law_tab.law_id = overall_accept.l_a)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_d,law_id AS l_d FROM faction_vote WHERE faction_vote.vote = "decline"  AND faction_vote.faction_id =72100005 GROUP BY faction_vote.law_id) AS overall_denied ON law_tab.law_id = overall_denied.l_d)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_r,law_id AS l_r FROM faction_vote WHERE faction_vote.vote = "abstain"  AND faction_vote.faction_id =72100005 GROUP BY faction_vote.law_id) AS overall_refrain ON law_tab.law_id = overall_refrain.l_r)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_abs,law_id AS l_abs FROM faction_vote WHERE faction_vote.vote = "none" AND faction_vote.faction_id =72100005 GROUP BY  faction_vote.law_id) AS overall_abstain ON law_tab.law_id = overall_abstain.l_abs) AS stat')
for row in list(cursor.fetchall()):
    if row[2] == None:
        appearance = 0
    else:
        appearance =row[2]

    if row[3] == None:
        accept = 0
    else:
        accept =row[3]

    if row[4] == None:
        denied = 0
    else:
        denied =row[4]

    if row[5] == None:
        refrain = 0
    else:
        refrain =row[5]

    if row[6] == None:
        absent = 0
    else:
        absent =row[6]

    if appearance == 0:
        dev_app = 1
    else:
        dev_app = appearance

    count = count + 1
    stat.append((count, appearance, accept / dev_app, denied / dev_app, refrain / dev_app, absent, 72100005, row[0]))
cursor.execute('SELECT law_id ,f_i,all_v - all_abs, all_a,all_d,all_r ,all_abs ,all_v - all_abs,all_v FROM '
               '(((((((SELECT law_id FROM laws) AS law_tab) '
               'LEFT JOIN (SELECT faction_id AS f_i, COUNT(faction_vote.vote) AS all_v ,law_id AS l_v FROM faction_vote WHERE faction_vote.faction_id =72100024 GROUP BY faction_vote.law_id)  AS all_votes ON law_tab.law_id = all_votes.l_v)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_a,law_id AS l_a FROM faction_vote WHERE faction_vote.vote = "accept" AND faction_vote.faction_id =72100024 GROUP BY faction_vote.law_id) AS overall_accept ON law_tab.law_id = overall_accept.l_a)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_d,law_id AS l_d FROM faction_vote WHERE faction_vote.vote = "decline"  AND faction_vote.faction_id =72100024 GROUP BY faction_vote.law_id) AS overall_denied ON law_tab.law_id = overall_denied.l_d)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_r,law_id AS l_r FROM faction_vote WHERE faction_vote.vote = "abstain"  AND faction_vote.faction_id =72100024 GROUP BY faction_vote.law_id) AS overall_refrain ON law_tab.law_id = overall_refrain.l_r)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_abs,law_id AS l_abs FROM faction_vote WHERE faction_vote.vote = "none" AND faction_vote.faction_id =72100024 GROUP BY  faction_vote.law_id) AS overall_abstain ON law_tab.law_id = overall_abstain.l_abs) AS stat')
for row in list(cursor.fetchall()):
    if row[2] == None:
        appearance = 0
    else:
        appearance =row[2]

    if row[3] == None:
        accept = 0
    else:
        accept =row[3]

    if row[4] == None:
        denied = 0
    else:
        denied =row[4]

    if row[5] == None:
        refrain = 0
    else:
        refrain =row[5]

    if row[6] == None:
        absent = 0
    else:
        absent =row[6]

    if appearance == 0:
        dev_app = 1
    else:
        dev_app = appearance

    count = count + 1
    stat.append((count, appearance, accept / dev_app, denied / dev_app, refrain / dev_app, absent, 72100024, row[0]))
cursor.execute('SELECT law_id ,f_i,all_v - all_abs, all_a,all_d,all_r ,all_abs ,all_v - all_abs,all_v FROM '
               '(((((((SELECT law_id FROM laws) AS law_tab) '
               'LEFT JOIN (SELECT faction_id AS f_i, COUNT(faction_vote.vote) AS all_v ,law_id AS l_v FROM faction_vote WHERE faction_vote.faction_id =72100027 GROUP BY faction_vote.law_id)  AS all_votes ON law_tab.law_id = all_votes.l_v)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_a,law_id AS l_a FROM faction_vote WHERE faction_vote.vote = "accept" AND faction_vote.faction_id =72100027 GROUP BY faction_vote.law_id) AS overall_accept ON law_tab.law_id = overall_accept.l_a)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_d,law_id AS l_d FROM faction_vote WHERE faction_vote.vote = "decline"  AND faction_vote.faction_id =72100027 GROUP BY faction_vote.law_id) AS overall_denied ON law_tab.law_id = overall_denied.l_d)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_r,law_id AS l_r FROM faction_vote WHERE faction_vote.vote = "abstain"  AND faction_vote.faction_id =72100027 GROUP BY faction_vote.law_id) AS overall_refrain ON law_tab.law_id = overall_refrain.l_r)'
               'LEFT JOIN (SELECT COUNT(faction_vote.vote) AS all_abs,law_id AS l_abs FROM faction_vote WHERE faction_vote.vote = "none" AND faction_vote.faction_id =72100027 GROUP BY  faction_vote.law_id) AS overall_abstain ON law_tab.law_id = overall_abstain.l_abs) AS stat')

for row in list(cursor.fetchall()):
    if row[2] == None:
        appearance = 0
    else:
        appearance =row[2]

    if row[3] == None:
        accept = 0
    else:
        accept =row[3]

    if row[4] == None:
        denied = 0
    else:
        denied =row[4]

    if row[5] == None:
        refrain = 0
    else:
        refrain =row[5]

    if row[6] == None:
        absent = 0
    else:
        absent =row[6]

    if appearance == 0:
        dev_app = 1
    else:
        dev_app = appearance

    count = count + 1
    stat.append((count, appearance, accept / dev_app, denied / dev_app, refrain / dev_app, absent, 72100027, row[0]))

cursor.close()
connection.close()

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.executemany('INSERT INTO duma_factionvotes  VALUES (?,?,?,?,?,?,?,?)',stat)  # запихали в таблицу
connection.commit()
cursor.close()
connection.close()
