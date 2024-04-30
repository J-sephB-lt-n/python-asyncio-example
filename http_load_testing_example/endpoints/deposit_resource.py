"""
Defines endpoint /deposit_resource
"""

import json
import random
import time

import flask

bp = flask.Blueprint("deposit_resource", __name__)


@bp.route("/deposit_resource", methods=["POST"])
def deposit_resource():
    input_json = flask.request.get_json()
    time.sleep(1)
    return flask.Response(
        json.dumps(
            {
                "resource": input_json["resource"],
                "deposit_status": "SUCCESS",
                "amount": input_json["amount"],
            }
        ),
        status=200,
    )
