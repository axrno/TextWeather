import json
import requests
import schedule
import time
from twilio.rest import Client
from dotenv import load_dotenv
import os


key = os.getenv('API_KEY')
city = "San Jose"

def create_message(msg):
    account_sid = os.getenv('SID')
    auth_token = os.getenv('AUTH')
    twilio_number = os.getenv('TW_NUM')
    my_number = os.getenv('MY_NUM')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = msg,
        from_ = twilio_number,
        to = my_number
    )   
    print("message was sent")
    #print(message)


def send_weather():
    weather_data = current_weather(city, key)
    #print(json.dumps(weather_data, indent=2)) 

    temperature = weather_data['main']['temp']
    max_temp = weather_data['main']['temp_max']

    #print(f"the current temperature is {temperature} and max temp is {max_temp}")

    weather_text_msg = (
        f"Good Morning!\n"
        f"Current temperature is {temperature}°F\n"
        f"The max temperature will be {max_temp}°F\n"
    )

    create_message(weather_text_msg)
    

def current_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"
    data = requests.get(url).json()
    return data 
     

if __name__ == '__main__':
    send_weather()
