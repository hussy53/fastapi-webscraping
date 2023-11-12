# --MAIN CLASS

# Import the necessary packages
from fastapi import FastAPI
import services as _services

# Initialize the app
app = FastAPI()

# Root webpage
@app.get("/")
async def root():
    return {
        "Welcome to these cool historical events page"
    }

# Fetches all the historical events stored in the json file
@app.get("/events")
async def all_events():
    return _services.get_all_events()

# Fetches all the historical events that happened today
@app.get("/events/today")
async def events_of_today():
    return _services.get_today()

# Fetches all the historical events that happened on the specified month
@app.get("/events/{month}")
async def events_of_month(month:str):
    return _services.get_month_events(month)

# Fetches all the historical events that happened on the specified month & day
@app.get("/events/{month}/{day}")
async def events_of_day(month:str, day:int):
    return _services.get_day_events(month, day)



