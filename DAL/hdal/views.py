from werkzeug import exceptions
from flask import jsonify, request
from sqlalchemy import and_
from hdal.hdal import app
from hdal.db import votes, factions, deputies, bills
from hdal.utils import json_list, json_object
import sqlalchemy
from datetime import datetime


@app.route('/')
def view_root():
    raise exceptions.BadRequest()

@app.errorhandler(404)
def view_err_404(error):
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(400)
def view_err_400(error):
    return jsonify({'error': 'Bad Request'}), 400

@app.route('/deputy/')
@json_list
def view_deputy():
    nameContains = request.args.get('nameContains', None)
    nameStarts = request.args.get('nameStarts', None)
    faction_id = request.args.get('faction_id', None)
    bill_id = request.args.get('bill_id', None)
    vote = request.args.get('vote', None)
    if vote and not bill_id or vote not in ['accept', 'abstain', 'decline', 'none', None]:
        raise exceptions.BadRequest()
    if vote is None:
        vote = 'accept'
    target = deputies
    if bill_id:
        target = target.join(votes)
    target = target.join(factions)
    query = target.select().with_only_columns([deputies.c.deputy_id, deputies.c.name, deputies.c.faction_id, factions.c.title.label('faction_title')])
    if nameContains:
        query = query.where(deputies.c.name.contains(nameContains))
    if nameStarts:
        query = query.where(deputies.c.name.startswith(nameStarts))
    if faction_id:
        query = query.where(deputies.c.faction_id == faction_id)
    if bill_id:
        query = query.where(and_(votes.c.law_id == bill_id, votes.c.vote == vote))
    return query.execute().fetchall()

@app.route('/deputy/<int:id>')
@json_object
def view_deputy_id(id):
    target = deputies.join(factions)
    query = target.select().with_only_columns([deputies.c.deputy_id, deputies.c.name, deputies.c.faction_id, factions.c.title.label('faction_title')])
    query = query.where(deputies.c.deputy_id == id)
    return query.execute().fetchone()

@app.route('/bill/')
@json_list
def view_bill():
    offset = request.args.get('offset', 0)
    count = request.args.get('count', 100)
    from_ = request.args.get('from', None)
    to = request.args.get('to', None)

    target = bills
    query = target.select().with_only_columns([bills.c.law_id.label('bill_id'), bills.c.title, bills.c.date_time.label('datetime')])
    try:
        if from_:
            query = query.where(bills.c.date_time > datetime.strptime(from_, "%Y%m%d%H%M%S"))
        if to:
            query = query.where(bills.c.date_time < datetime.strptime(to, "%Y%m%d%H%M%S"))
    except ValueError:
        raise exceptions.BadRequest()
    query = query.order_by(bills.c.date_time)
    query = query.offset(offset)
    query = query.limit(count)
    result = query.execute().fetchall()
    result = [dict(row) for row in result]
    for i in range(len(result)):
        result[i]['datetime'] = result[i]['datetime'].strftime("%Y%m%d%H%M%S")
    return result

@app.route('/bill/<int:id>')
@json_object
def view_bill_id(id):
    target = bills
    query = target.select().with_only_columns([bills.c.title, bills.c.law_id.label('bill_id'), bills.c.date_time.label('datetime')])
    query = query.where(bills.c.law_id == id)
    return query.execute().fetchone()

@app.route('/faction/')
@json_list
def view_faction():
    target = factions
    query = target.select().with_only_columns([factions.c.faction_id, factions.c.title.label('faction_title')])
    return query.execute().fetchall()

@app.route('/faction/<int:id>')
@json_object
def view_faction_id(id):
    target = factions
    query = target.select().with_only_columns([factions.c.faction_id, factions.c.title.label('faction_title')])
    query = query.where(factions.c.faction_id == id)
    return query.execute().fetchone()
