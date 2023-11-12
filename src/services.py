# --SERVICES CLASS : Helper dictionary class
# This class is used by main.py

# Import the necessary packages
from typing import Dict
import json as _json
import datetime as _dt

# Returns a dictionary of all the events from the json file
def get_all_events() -> Dict:
    # Opens up "events.json" file and loads it up on the local host
    with open("events.json",  encoding="utf-8") as events_file:
        data = _json.load(events_file)    
    return data

# Returns a dictionary of all the events of the specified month from the json file
def get_month_events(month:str) -> Dict:
    events = get_all_events()
    # Catch the error if misspelled
    try:
        return events[month]
    
    except KeyError:
        return "The month might have been misspelled. It doesn't exist"

# Returns a dictionary of all the events of the specified day from the json file    
def get_day_events(month:str, day:int) -> Dict:
    events = get_month_events(month) # Get all the events for that month

    # Catch the error if misspelled
    try:
        return events[str(day)] # day is in str format in json file
        
    except KeyError:
        return "The day is out of range."

# Returns a dictionary of all the events that has happened today from the json file
def get_today():
    events = get_all_events()
    today = _dt.date.today()
    month = today.strftime("%B").lower()
    day = str(today.day)
    return events[month][day]


