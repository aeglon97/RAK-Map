# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 08:31:52 2019

@author: Angelo Acebedo
"""
import logging
logging.basicConfig()
logging.basicConfig(level=logging.DEBUG)

import pandas as pd
import numpy as np
import requests, json
import geojson
#df = pd.read_csv('Rak Businesses.csv')
import os
import googlemaps
from datetime import datetime
import random

#dealing with environment variables
from os.path import join, dirname
from dotenv import load_dotenv

#dealing with environment variables 
'''path='./local.env'
load_dotenv(dotenv_path=path, verbose=True)
api_key = os.getenv('RAK_MAP_API_KEY')'''

'''geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

findplace_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
findplace_inputtype = 'textquery'
findplace_fields = 'formatted_address,name,opening_hours,geometry'

placedetail_url = 'https://maps.googleapis.com/maps/api/place/details/json?'
placedetail_fields = 'formatted_address,name,opening_hours,geometry'

findplace_results_json = requests.get(findplace_url + 'input=ras%20al%20khaimah' + '&inputtype=' + findplace_inputtype +
                              '&key=' + api_key).json()
findplace_id = findplace_results_json['candidates'][0].get('place_id', "")

#using place details to find opening hours
placedetail_results_json = requests.get(placedetail_url + 'placeid=' + findplace_id + '&fields=' + placedetail_fields + '&key=' + api_key).json()

print(placedetail_results_json)
for i in range(7):
    print(placedetail_results_json['result']['opening_hours']['periods'][i]['open']['day'] , '\t' ,
          placedetail_results_json['result']['opening_hours']['periods'][i]['open']['time'])

'''
#findplace_ob = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=falafel%20abu%20naeem&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=' + api_key)
#res_ob = requests.get(url + 'address=' + place + '&key=' + api_key)
#x = res_ob.json()

'''
RAK BOUNDS [lat, lng]
    Northeast: 26.0696541, 56.19553699999999
    Southwest: 25.3543, 55.7306787    
'''
from pprint import pprint

#read geoJSON coordinates
with open('rak_rect.geojson') as f:
    rak_coords_json = json.load(f)

rak_coords = rak_coords_json["features"][0]["geometry"]["coordinates"][0]
min_x = rak_coords[0][0]
min_y = rak_coords[0][1]
max_x = rak_coords[2][0]
max_y = rak_coords[2][1]

#TODO 1: generate random coordinate in RAK boundary
added = []
sampleSize = 15
count = 0

while count < sampleSize:
    r_x = random.uniform(min_x, max_x)
    r_y = random.uniform(min_y, max_y)
    r_coord = [r_x, r_y]
    if r_coord not in added:
        count += 1
        added.append(r_coord)
        
print(added)
    

    #TODO 2: check if in RAK
    
    #TODO 3: check if on a road

    #TODO 4: check if nearby other businesses
    
    #if coordinates pass all 3 tests, continue; else generate new point & repeat
    
#TODO 5: generate random opening hours