import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MY_EMAIL = os.environ.get("FROM_ADDR")
PASSWORD = os.environ.get("PASSWORD")
TO_ADDRS = os.environ.get("TO_ADDRS")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"


class NotificationManager:

    def send_emails(self, emails, message, google_flight_link):
        connection = smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)

        for email in emails:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode("utf-8")
            )
            connection.close()

