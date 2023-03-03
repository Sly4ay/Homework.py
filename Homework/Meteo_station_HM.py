import requests
from bs4 import BeautifulSoup

url = "https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/"
dataline = requests.get(url)
soup = BeautifulSoup(dataline.text, 'html.parser')
table = soup.find('table', {'class': 'table-striped'})
rows = table.tbody.find_all('tr')

weather_data = []

for row in rows:
    columns = row.find_all('td')
    location = columns[0].text.strip()
    temp = columns[2].text.strip()
    wind_speed = columns[3].text.strip()
    weather_data.append([location, temp, wind_speed])

user_choice = input("Введите название метеостанции: ")

for location, temp, wind_speed in weather_data:
    if user_choice.lower() in location.lower():
        print("Местоположение: ", location)
        print("Температура: ", temp)
        print("Скорость ветра: ", wind_speed)