import sqlite3

def get_dep_list(db_cursor):
    db_cursor.execute('SELECT deputy_id FROM deputies ')
    dp_list = list(map(lambda x: x[0], db_cursor.fetchall()))
    return dp_list

def get_dep_votes(db_cursor, dep_id):
    db_cursor.execute('SELECT vote FROM votes WHERE deputy_id = {0}'.format(dep_id))
    vote_list = list(map(lambda x: x[0], db_cursor.fetchall()))
    return vote_list

def get_stats():
    connection = sqlite3.connect('duma.db')
    cursor = connection.cursor()

    stats = list()

    for id in get_dep_list():
        print(id, end=' ', flush=True)
        cursor.execute('SELECT name, faction_id FROM deputies WHERE deputy_id = {0}'.format(id))
        name, faction_id = cursor.fetchall()[0]
        dep_votes = get_dep_votes(cursor, id)
        lifetime = len(dep_votes)
        absent_num = dep_votes.count('none')
        appearance = lifetime - absent_num
        accept = dep_votes.count('accept') / appearance
        denied = dep_votes.count('decline') / appearance
        refrain = dep_votes.count('abstain') / appearance
        absent_per = absent_num / lifetime
        appearance_per = appearance / lifetime
        protest_level = 0
        protest_faction = 0

        stats.append((name, lifetime, appearance, absent_num, accept, denied, refrain, absent_per, appearance_per, protest_level, protest_faction, faction_id))

    return stats
