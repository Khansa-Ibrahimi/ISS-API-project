import requests
import smtplib
import datetime as dt
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Set your geographical location. Use LATLONG.NET to get the coordinates
MY_LAT = 19.075983
MY_LNG = 72.877655

# Function to check if the ISS is overhead (within +5 and -5 of current location)
def is_overhead():
    # Call ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    # Fetching data
    data = response.json()
    lat = float(data["iss_position"]["latitude"])
    lng = float(data["iss_position"]["longitude"])

    # Check if ISS near current location
    if MY_LAT-5 <= lat <= MY_LAT+5 and MY_LNG-5 <= lng <= MY_LNG+5:
        return True

# Function to check if it is currently night
def sunset():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0
    }

    # Call Sunrise-Sunset API
    response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    # Fetching data
    data=response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get current time
    time_now = dt.datetime.now().hour

    # It's night before sunrise and after sunset
    if sunrise >= time_now or sunset <= time_now:
        return True

# Infinite loop that checks every 60 seconds
while True:
    time.sleep(60)

     # If the ISS is overhead and it is night, send an email alert
    if is_overhead() and sunset():
        with smtplib.SMTP("smtp.gamil.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up!\n\nThe ISS is above you!!!!"
            )
        print("Email Send")
