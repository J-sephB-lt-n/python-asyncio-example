"""
Defines endpoint /get_oil
"""

import json
import random
import time

import flask

bp = flask.Blueprint("get_oil", __name__)


@bp.route("/get_oil", methods=["GET"])
def get_oil():
    time.sleep(1)
    return flask.Response(
        json.dumps(
            {
                "resource": "oil",
                "amount": random.randint(0, 5),
            }
        ),
        status=200,
    )
