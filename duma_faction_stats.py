import sqlite3

connection = sqlite3.connect('duma.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM factions')

faction_tab = []

for row in cursor.fetchall():
    faction_tab.append((int(row[0]),row[1]))#считал таблицу фракций

cursor.execute('SELECT faction_id FROM deputies')

f_d_tab = []

for row in cursor.fetchall():
    f_d_tab.append((int(row[0])))#считал столбец ид фракций депутатов из списка депутатов

num_de_in_fact = []

for i in range(len(faction_tab)):
    a = f_d_tab.count(faction_tab[i][0])
    num_de_in_fact.append( (faction_tab[i][0],a) )#посчитал количество депутатов во фракциях

cursor.close()
connection.close()
############################################################################################

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

cursor.execute('SELECT accept,denied,refrain,absent_percentage,appearance_percentage,protest_level,faction_id FROM duma_deputy')

duma_faction = []

for row in cursor.fetchall():
    duma_faction.append((row[0],row[1],row[2],row[3],row[4],row[5],row[6]))#считал из таблицы статистики голосования депутатов эту статистику

duma_faction_stat =[]
about_logo_color1_color2 = [(int(72100024),'Всеросси́йская полити́ческая па́ртия «Еди́ная Росси́я» — крупнейшая политическая партия Российской Федерации, «партия власти».','http://www.ymniki.ru/assets/images/2011/edros.jpg','#f8f8ff','#120a8f'),
                            (int(72100004),'Коммунисти́ческая па́ртия Росси́йской Федера́ции (сокращённо КПРФ) — официально зарегистрированная левая политическая партия в Российской Федерации.','http://sakhalife.ru/wp-content/uploads/2016/03/emblema-kprf.jpg','#f8f8ff ','#cc0000'),
                            (int(72100005),'ЛДПР (историческое название — Либерально-демократическая партия России) — официально зарегистрированная центристская политическая партия в Российской Федерации.','http://ldpr.ru/static/public/images/party-emblem.png','#120a8f ','#ffd700'),
                            (int(72100027),'«Справедли́вая Росси́я» (СР, эсеры) — официально зарегистрированная левоцентристская политическая партия в России, декларирующая идеологию социал-демократии и модернизированного социализма.','http://logomogo.ru/uploads/logo-spravedlivaya-rossiya.png','#ff9900 ','#9c0303')]

count = 0
for i in range(len(faction_tab)):
    num_dep = 0
    count = count + 1
    for num in range(len(num_de_in_fact)):
        if faction_tab[i][0] == num_de_in_fact[num][0]:
            num_dep = num_de_in_fact[num][1]
    av_accept = 0
    av_denied = 0
    av_refrain =0
    av_appearance =0
    av_absent = 0
    protest_level = 0
    for j in range(len(duma_faction)):
        if faction_tab[i][0] == duma_faction[j][6]:
            av_accept     = av_accept     + duma_faction[i][0]
            av_denied     = av_denied     + duma_faction[i][1]
            av_refrain    = av_refrain    + duma_faction[i][2]
            av_absent     = av_absent     + duma_faction[i][3]
            av_appearance = av_appearance + duma_faction[i][4]
            protest_level = protest_level + duma_faction[i][5]
    av_accept = av_accept / num_dep
    av_denied = av_denied / num_dep
    av_refrain = av_refrain / num_dep
    av_absent = av_absent /num_dep
    av_appearance =av_appearance /num_dep
    protest_level = protest_level / num_dep
    for num in about_logo_color1_color2:
        if  faction_tab[i][0] == num[0]:
            duma_faction_stat.append((faction_tab[i][0],faction_tab[i][1],num[1],num[2],num[3],num[4],av_accept,av_denied,av_refrain,av_appearance,av_absent,protest_level))

for row in duma_faction_stat:
    print(row)

cursor.executemany('INSERT INTO duma_faction VALUES ( ?,?,?,?,?,?,?,?,?,?,?,?)',duma_faction_stat) #запихали в таблицу
connection.commit()
cursor.close()
connection.close()