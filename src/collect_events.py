# --COLLECT EVENTS CLASS : Creates the events dictionary and imports it to the JSON file for use
# Run this file before running the main file

# Import the necessary packages
import datetime as _dt
from typing import Dict, Iterator
import scraper as _scraper
import json as _json

# Date ranges from the specified start uptil the end of the year                                                           
# Iterator loops through the date range 
def _date_range(start_date:_dt.date, end_date:_dt.date) -> Iterator[_dt.date]:

    # Loop from beginning to the end of the year
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n) # Allows us to increment the date by n from start date


# Creates an event dictionary from 1st January 2020 uptil 31st December 2020
def create_events_dict() -> Dict:
    events = dict() # Initialize an empty dictionary
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1) # Excludes this date, ( until 2020, 12, 31)

    for date in _date_range(start_date, end_date):
        month = date.strftime("%B").lower() # Extract the month from date. Change it to lower case

        if month not in events:
            events[month] = dict() # Initialize an empty dictionary for that month if not created
        events[month][date.day] = _scraper.events_of_the_day(month, date.day)

    return events


# Main class to create the JSON file
if __name__ == "__main__":
    events = create_events_dict()
    with open("events.json", mode="w", encoding="utf-8") as events_file:
        _json.dump(events, events_file, ensure_ascii=False)



