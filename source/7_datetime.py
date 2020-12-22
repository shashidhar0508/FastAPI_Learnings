from fastapi import FastAPI, Body
from pydantic import BaseModel

from datetime import datetime, time, timedelta

app = FastAPI()


@app.post("/date_time")
def date_time(start_date: datetime = Body(None),
              end_date: datetime = Body(None),
              repeat_at: time = Body(None),
              process_after: timedelta = Body(None)):
    start_process = start_date + process_after
    duration = end_date - start_process
    """
    We can see the above example as Example value in docs
    """
    return {"start_Date": start_date,
            "end_Date": end_date,
            "repeat_at": repeat_at,
            "process_after": process_after,
            "start_process": start_process,
            "duration": duration,
            "process_after": process_after.seconds
            }
