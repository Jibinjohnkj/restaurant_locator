# restaurant_locator
A simple script to recommend the top three restaurants nearest to the visitor’s current location


Note
----
This script requires python 3.8


Installation
------------
pip install -r requirements.txt

python run.py

Introduction
------------

A CSV file (sf-restaurants.csv) contains a list of restaurants in San Francisco with their latitudes and longitudes, ratings (on a scale of 1 to 5) and their time-slots of operation. A restaurant can serve breakfast (8 am - 11 am), lunch (12 pm - 3 pm), or dinner (6:30 pm to 9:30 pm). 

For someone visiting San Francisco, the script prints out the top three restaurants nearest to the visitor’s current location (in a 1-mile radius) for the current time-slot, based on restaurant ratings. 

The visitor’s current location (latitude and longitude), and time of the day (24-hour format) is provided in a CSV file(visitor-locations-times.csv).