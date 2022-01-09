from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch

# this should be in new file
import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

MY_EMAIL = os.environ.get("FROM_ADDR")
PASSWORD = os.environ.get("PASSWORD")
TO_ADDRS = os.environ.get("TO_ADDRS")


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))
new_flight_price = []

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

