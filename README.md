# ISS Tracker 🚀

This Python script tracks the position of the International Space Station (ISS) and sends you an email alert when it's flying above your location **at night**, so you can go outside and try to spot it!

## 🌍 Features

- Uses the [Open Notify ISS API](http://api.open-notify.org/) to track the ISS.
- Uses the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to determine if it’s currently night.
- Sends an email alert via Gmail when the ISS is visible overhead.
- Runs continuously, checking every 60 seconds.

## 📦 Requirements

Install dependencies using pip:
```bash
pip install requests python-dotenv
