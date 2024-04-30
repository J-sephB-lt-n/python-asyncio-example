"""
Defines endpoint /get_task
"""

import random
import time

import flask

bp = flask.Blueprint("get_task", __name__)


@bp.route("/get_task", methods=["GET"])
def get_task():
    time.sleep(1)
    return flask.Response(
        random.choice(("get_gold", "get_oil", "get_water")), status=200
    )
