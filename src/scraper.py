# --SCRAPPER CLASS : Web scrapes the website https://www.onthisday.com/
# This class is used in colle_events.py

# Import the necessary packages
from typing import List
import requests as _requests
import bs4 as _bs4

# Generates a url for a particular day
def _generate_url(month:str, day:int) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

# Parses a page using beautiful soup
def _get_page(url:str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

# Retreives the extracted events of the day
def events_of_the_day(month:str, day:int) -> List[str]:
    url = _generate_url(month, day) # Generate a url
    get_page = _get_page(url) # Retreive the page using the url
    raw_events = get_page.find_all(class_="event") # Extract the events defined in class "event"
    events = [event.text for event in raw_events] # Put the extracted events in a list
    return events



