"""
Defines endpoint /get_gold
"""

import json
import random
import time

import flask

bp = flask.Blueprint("get_gold", __name__)


@bp.route("/get_gold", methods=["GET"])
def get_gold():
    time.sleep(1)
    return flask.Response(
        json.dumps(
            {
                "resource": "gold",
                "amount": random.randint(0, 1),
            }
        ),
        status=200,
    )
