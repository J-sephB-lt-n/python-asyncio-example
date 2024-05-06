"""
Parameters controlling aspects of the load test
"""
from typing import Final

N_WORKERS: Final[int] = 5
N_TASKS_PER_WORKER: Final[int] = 10

ENDPOINT_PROCESS_TIME_NSECS = {
    # passed to time.sleep() to increase the
    # endpoint response time
    "/get_task": 0,
    "/get_gold": 0,
    "/get_oil": 0,
    "/get_water": 0,
    "/deposit_resource": 0,
}
