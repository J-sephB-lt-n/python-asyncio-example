"""
Parameters controlling aspects of the load test
"""

endpoint_process_time_nsecs = {
    # passed to time.sleep() to increase the
    # endpoint response time
    "/get_task": 1,
    "/get_gold": 1,
    "/get_oil": 1,
    "/get_water": 1,
    "/deposit_resource": 1,
}
