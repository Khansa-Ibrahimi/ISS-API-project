# ISS Tracker 🚀

This Python script tracks the position of the International Space Station (ISS) and sends you an email alert when it's flying above your location **at night**, so you can go outside and try to spot it!

## 📌 Features

- Uses the [Open Notify ISS API](http://api.open-notify.org/) to track the ISS.
- Uses the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine if it’s currently night.
- Sends an email alert via Gmail when the ISS is visible overhead.
- Runs continuously, checking every 60 seconds.

## 📦 Requirements

Install dependencies using pip:
```bash
pip install requests python-dotenv
```
## ⚙️ Setup Instructions
1. Clone this repository
```bash
git clone https://github.com/Khansa-Ibrahimi/ISS-API-project.git
cd ISS-API-project
```

2. Create a .env file in the project directory:
```bash
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_app_password
```
**Note:** 
If you are using Gmail, you need to:
- Enable 2-Step Verification
- Create an App Password and use that password in the .env file.

3. Run the script

## 🌍 Customize Your Location
To track the ISS based on your location, modify these variables in the script:
```bash
MY_LAT = 19.075983   # Your latitude
MY_LNG = 72.877655   # Your longitude
```
You can find your coordinates on Google Maps or latlong.net.


