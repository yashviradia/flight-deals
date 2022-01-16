import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MY_EMAIL = os.environ.get("FROM_ADDR")
PASSWORD = os.environ.get("PASSWORD")
TO_ADDRS = os.environ.get("TO_ADDRS")


class NotificationManager:

    def send_notification(self, message):
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_ADDRS,
            msg=message
        )
        connection.close()

