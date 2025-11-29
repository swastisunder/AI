'''
Create a Python dictionary of 3 cities and their populations. Save it to "cities.json"
1. Then load the JSON and print each city and its population.
2. Ask the user for a new city & its population - update this info in the json file.
'''

import json

cities = {
    "surat":5,
    "aksa":2,
    "bhopal":3
}

with open('cities.json','w')as f:
    json.dump(cities,f,indent=4,sort_keys=True)
    
print('Initial data saved to cities.json\n')

with open('cities.json','r')as f:
    print(json.load(f))

new_city = input("Enter a new city: ")
pop = int(input("Enter populations for new city: "))
cities[new_city]=pop

with open('cities.json','w')as f:
    json.dump(cities,f,indent=4,sort_keys=True)
    
print('New added\n')

with open('cities.json','r')as f:
    print(json.load(f))