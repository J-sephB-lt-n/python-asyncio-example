"""
Defines endpoint /get_water
"""

import json
import random
import time

import flask

bp = flask.Blueprint("get_water", __name__)


@bp.route("/get_water", methods=["GET"])
def get_water():
    time.sleep(1)
    return flask.Response(
        json.dumps(
            {
                "resource": "water",
                "amount": random.randint(0, 10),
            }
        ),
        status=200,
    )
