from flask import Flask, render_template, request
from weather import main as get_weather  # assuming this is a module you've written
import requests  # add this line for making external HTTP requests
import os  # add this line for environment variables

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')  # assuming you have set an environment variable named 'API_KEY'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city = None
    state = None
    country = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        # Change the following line
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={API_KEY}&units=metric').json()
        
        if response.get('cod') == 200:
            weather_data = {
                'main': response['weather'][0]['main'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temperature': response['main']['temp'],
                'humidity': response['main']['humidity'],
                'pressure': response['main']['pressure'],
                'wind_speed': response['wind']['speed']
            }
    return render_template('index.html', weather_data=weather_data, city=city, state=state, country=country)

if __name__ == '__main__':
    app.run(debug=True)
