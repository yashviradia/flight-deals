import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_AUTHORIZATION = os.environ.get("SHEETY_AUTHORIZATION")
SHEETY_HEADERS = {
    "Authorization": SHEETY_AUTHORIZATION,
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEETY_HEADERS
            )
            print(response.text)

