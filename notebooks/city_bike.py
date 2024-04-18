#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests


# In[3]:


import pandas as pd


# In[5]:


url = 'https://api.citybik.es/v2/networks'

# Send Request
response = requests.get(url)
data = response.json()

# Get and print a list of cities
cities = [network['location']['city'] for network in data['networks']]
print("List of cities supported by the CityBikes API.")
for city in sorted(set(cities)):
    print(city)


# In[7]:


# city_name = 'Koln'
city_name = 'Köln'

city_name in cities


# In[8]:


# Find the specified city in the returned network
city_url = None
for network in data['networks']:
    if city_name.lower() in network['location']['city'].lower():
        city_url = network['href']
        break
    
# If city found, send request for site information
if city_url:
    city_response = requests.get(f'https://api.citybik.es{city_url}')
    city_data = city_response.json()

    # Extract site information
    stations = city_data['network']['stations']

    # Parsing site data
    station_data = []
    for station in stations:
        station_info = {
            'latitude': station['latitude'],
            'longitude': station['longitude'],
            'num_bikes': station['free_bikes']
        }
        station_data.append(station_info)
else:
    print("Wrong")


# In[9]:


df = pd.DataFrame(station_data)
df


# In[18]:


df.to_csv('part1_station_data.csv', index=False)


# In[ ]:




