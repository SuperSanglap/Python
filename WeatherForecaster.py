import requests

api_address = f'https://api.openweathermap.org/data/2.5/weather?appid=8ca2a3710e7d7e8b5960f4b78c99beed&q='
while True:
    try:
        location = str(input('location:- '))
        url = api_address + location
        json_data = requests.get(url).json()
        formatted_data = json_data['weather'] [0] ['description']
        print(formatted_data)
    except:
        print('Error!')