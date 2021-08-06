import asyncio, time
from fastapi import FastAPI, Path
from datetime import datetime
import statistics

app = FastAPI()

@app.get("/delay/{delay1}/{delay2}")
async def get_delay(
    delay1: float = Path(..., title="Nonblocking time taken to respond"),
    delay2: float = Path(..., title="Blocking time taken to respond"),
):
    total_start_time = datetime.now()
    times = []
    for i in range(100):
        start_time = datetime.now()
        await asyncio.sleep(delay1)
        time.sleep(delay2)
        time_delta= (datetime.now()-start_time).microseconds
        times.append(time_delta)

    times_average = statistics.mean(times)

    return {"delays":[delay1,delay2],"total_time_taken":(datetime.now()-total_start_time).microseconds,"times_avarage":times_average,"times":times}