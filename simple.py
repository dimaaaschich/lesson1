from pprint import pprint
weather = {'city': 'Москва',
           'temperature': 20
}
print(weather['city'])

weather['temperature'] = weather['temperature'] - 5
pprint(weather)
print(weather.get('country', 'Россия'))
weather['date'] = '27.05.2019'
pprint(weather)
print(len(weather))