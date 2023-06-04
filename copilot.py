
import requests
import json
import sys
from tabulate import tabulate
api_key="6f122da60c2410800e7748f053614a06"
#take input from user for city name
city=input("Enter city name: ")
"""the format of the url is https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}.
now make a string called url and place city in city_name and api_key in api_key"""
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#now make a request to the url
response=requests.get(url)
#now load the response in json format
x=response.json()
"""write a try block which should get the response by using response.get_status_code().
in the except block catch for requests.exceptions.HTTPError.
in the same except block if status code is 404 then print city not found and exit the program.
if status code is 401 then print invalid api key and exit the program.
if status code is 429 then print you have exceeded the limit and exit the program.
else print something went wrong along with exception and exit the program."""
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    if response.status_code==404:
        print("City not found")
        sys.exit()
    elif response.status_code==401:
        print("Invalid api key")
        sys.exit()
    elif response.status_code==429:
        print("You have exceeded the limit")
        sys.exit()
    else:
        print("Something went wrong")
        sys.exit()
"""now get data from the json file and store it in variables.
get the temperature and convert it into celsius and store it in a variable.
get the humidity and store it in humidity variable.
get the wind speed and store it in wind_speed variable.
get the description and store it in description variable."""
temperature=x["main"]["temp"]
temperature=temperature-273.15
humidity=x["main"]["humidity"]
wind_speed=x["wind"]["speed"]
description=x["weather"][0]["description"]
"""now using tabulate module create a table with 3 columns and 5 rows.
the first column should contain "Temperature","Humidity","Wind Speed","Description".
the second column should contain the values of temperature,humidity,wind_speed,description.
the third column should contain the units of temperature,humidity,wind_speed,description.
the heading of first column should be "Weather Parameter of {city}".
the heading of second column should be "Values".
the heading of third column should be "Units".
the table should be in grid format."""
table=[["Temperature",temperature,"Celsius"],["Humidity",humidity,"%"],["Wind Speed",wind_speed,"m/s"],["Description",description,""]]
print(tabulate(table,headers=["Weather Parameter of "+city,"Values","Units"],tablefmt="grid"))



