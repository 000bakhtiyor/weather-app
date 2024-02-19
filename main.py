from flask import Flask
from flask import render_template, request
from os import environ
import requests

weather_api_key = environ.get("WeatherApi")
app = Flask(__name__)

URL = f"http://api.weatherapi.com/v1/current.json?key="

def get_data_from_url(city_name):
    req = requests.get(URL+f"{weather_api_key}&q={city_name}&aqi=no")
    return req.json()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        city_name = request.form.get("city-name")
        data = get_data_from_url(city_name)
        print(data)
        return render_template("home.html", data=data)
        