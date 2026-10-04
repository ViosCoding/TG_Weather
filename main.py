import os
import requests






API_KEY = os.getenv('API_KEY')

def rain_message():
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_ID')

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f'{time}: 🌧️ bring an umbrella!'
    }
    # requests.get(url, params=payload)
    tg_response = requests.post(url, data=payload) 
    return tg_response.json()



def wont_rain_message():
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_ID')

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f'{time}: 🌧️ bring an umbrella!'
    }
    # requests.get(url, params=payload)
    tg_response = requests.post(url, data=payload)
    return tg_response.json()



# declare parameters
weather_params = {
    'lat': 33.665044686516104,
    'lon': -84.45852607616257,
    "appid": API_KEY,
    'units': 'imperial',
    'cnt': 4  # optional param to dictate amount of items pulled from api

}





# region client = Client(message_params)

# establish different endpoints
ONE_DAY_API_URL = f'https://api.openweathermap.org/data/4.0/onecall/current'
FIVE_DAY_API_URL = f'https://api.openweathermap.org/data/2.5/forecast'



response = requests.get(FIVE_DAY_API_URL, params=weather_params)
response.raise_for_status()
data = response.json()
# print(data)


# message = client.messages.create(
#   from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
#   body="It's going to rain today. Remember to bring an umbrella",
#   to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
# )
# region readable json formatting
# TODO ----- format data to easily readable json/ creates string ony for reading
# formatted_data = json.dumps(data, indent=2)
# print(formatted_data)
# endregion




# region check rain for the next 12 hours using main name (api pulls every 3 hours)

will_rain = False
for forecast in data['list']:  # list is the key that contains list of dictionaries
    # print(forecast)
    id = forecast['weather'][0]['id']
    time = forecast['dt_txt'][11:16]  # [11:16] slices what's returned
    if int(id) < 700:
        will_rain = True
    if will_rain:
        rain_message()

    else:
        wont_rain_message()


