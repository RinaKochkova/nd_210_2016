import sqlalchemy
import datetime
import re
import hdal.utils

#_engine = sqlalchemy.create_engine('sqlite:///' + app.config['DATABASE'])
# TODO grab db name from configuration
_engine = sqlalchemy.create_engine('sqlite:///' + 'duma.db')

_meta = sqlalchemy.MetaData()
_meta.bind = _engine;
_meta.reflect()

deputies = _meta.tables['deputies']
factions = _meta.tables['factions']
bills = _meta.tables['laws']
votes = _meta.tables['votes']

bills.columns['date_time'].type = sqlalchemy.dialects.sqlite.DATETIME(storage_format="%(year)04d-%(month)02d-%(day)02dT%(hour)02d:%(minute)02d:%(second)02d",
                                                                      regexp=r"(\d+)-(\d+)-(\d+)T(\d+):(\d+):(\d+).....")
