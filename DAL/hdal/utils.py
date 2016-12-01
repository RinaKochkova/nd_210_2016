from functools import wraps
from flask import jsonify
from werkzeug import exceptions

def json_object(handler):
    @wraps(handler)
    def w(*args, **kwargs):
        result = handler(*args, **kwargs)
        if not result:
            raise exceptions.NotFound()
        return jsonify(dict(result))
    return w

def json_list(handler):
    @wraps(handler)
    def w(*args, **kwargs):
        result = handler(*args, **kwargs)
        if not result:
            raise exceptions.NotFound()
        return jsonify([dict(row) for row in result])
    return w
