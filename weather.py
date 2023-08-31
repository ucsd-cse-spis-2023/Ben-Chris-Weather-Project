from flask import Flask
app = Flask(__name__)
# import request
# from dotenv import load_dotenv
# import os

# load_dotenv()
# API_KEY = os.getenv ('API_KEY')

@app.route("/")
def hello():
   return "Hello World!"

#def get_lan_lon(city_name, state_code, country_code, API_KEY):
    #response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}')

    #print(response)
    #print('Hello World')
#get_lan_lon('Toronto', 'ON', 'Canada', API_KEY)


if __name__ == "__main__":
   app.run(host='0.0.0.0')