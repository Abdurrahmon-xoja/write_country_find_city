import json
user_country = input('write country: ')

with open('country-list-with-ids.json', 'r') as file:
    data = json.load(file)

def faind_country (country_name):
    for country in data:
        if country['country'] == country_name:
            return country['capital']

print(faind_country(user_country))
