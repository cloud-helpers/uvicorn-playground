#
# File: https://github.com/cloud-helpers/uvicorn-playground/blob/master/uvicorn-delay.py
#

import asyncio
import time
import fastapi
import datetime
import statistics

app = fastapi.FastAPI()

@app.get("/delay/{delay1}/{delay2}")
async def get_delay(
    delay1: float = fastapi.Path(...,
                                 title="Nonblocking time taken to respond"),
    delay2: float = fastapi.Path(...,
                                 title="Blocking time taken to respond"),
):
    total_start_time = datetime.datetime.now()
    times = []
    for i in range (100):
        start_time = datetime.datetime.now()
        await asyncio.sleep (delay1)
        time.sleep (delay2)
        time_delta = datetime.datetime.now() - start_time
        time_delta_ms = time_delta.microseconds
        times.append (time_delta_ms)

    #
    times_average = statistics.mean (times)

    #
    total_taken_time = datetime.datetime.now() - total_start_time
    total_taken_time_ms = total_taken_time.microseconds

    #
    response = {
        "delays": [delay1, delay2],
        "total_time_taken_ms": total_taken_time_ms,
        "times_avarage_ms": times_average,
        "times": times}

    #
    return response
