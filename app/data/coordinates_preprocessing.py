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
import gmplot
import pprint
#dealing with environment variables 
path='./local.env'
load_dotenv(dotenv_path=path, verbose=True)
api_key = os.getenv('RAK_MAP_API_KEY')

geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

'''
findplace_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'
findplace_inputtype = 'textquery'
findplace_fields = 'formatted_address,name,opening_hours,geometry'

placedetail_url = 'https://maps.googleapis.com/maps/api/place/details/json?'
placedetail_fields = 'formatted_address,name,opening_hours,geometry'

findplace_results_json = requests.get(findplace_url + 'input=falafel%20abu%20naeem' + '&inputtype=' + findplace_inputtype +
                              '&key=' + api_key).json()
findplace_id = findplace_results_json['candidates'][0].get('place_id', "")

#using place details to find opening hours
placedetail_results_json = requests.get(placedetail_url + 'placeid=' + findplace_id + '&fields=' + placedetail_fields + '&key=' + api_key).json()

print(placedetail_results_json)
for i in range(7):
    print(placedetail_results_json['result']['opening_hours']['periods'][i]['open']['day'] , '\t' ,
          placedetail_results_json['result']['opening_hours']['periods'][i]['open']['time'])

'''
'''
RAK BOUNDS [lat, lng]
    Northeast: 26.0696541, 56.19553699999999
    Southwest: 25.3543, 55.7306787    
'''

#read geoJSON coordinates
with open('rak_rect.geojson') as f:
    rak_coords_json = json.load(f)

rak_coords = rak_coords_json["features"][0]["geometry"]["coordinates"][0]
min_y = rak_coords[0][0]
min_x = rak_coords[0][1]
max_y = rak_coords[2][0]
max_x = rak_coords[2][1]

#TODO 1: generate random coordinate in RAK boundary
added = []
latitude_list = []
longitude_list = []
sampleSize = 15
count = 0

def generateJSON(r_coord):
    params = 'latlng=' + str(r_coord[0]) + ',' + str(r_coord[1])
    query = geocode_url + params + '&key=' + api_key
    result_json = requests.get(query).json()
    return result_json

def isInRAK(result_json):
    #print('=====checking if in RAK=======')
    if (result_json and 'compound_code' in result_json['plus_code']):
        address = result_json['plus_code']['compound_code']
        print(address)
        if ('Ras al Khaimah' not in address):
            #print("this is not in RAK.")
            return False
        else:
            #print("this is in RAK.")
            return True
    
def isOnRoad(result_json):
    print('=====checking if by road=====')
    if 'geometry' in result_json['results'][1]:
        geometry = result_json['results'][1]['geometry']
        pprint.pprint(geometry)
    
def meetsConstraints(r_coord):
    print('-----------------------')
    result_json = generateJSON(r_coord)
    if isInRAK(result_json):
        return True
    return False
    #isOnRoad(result_json)
    
    #check if on road
    


while count < sampleSize:
    r_x = random.uniform(min_x, max_x)
    r_y = random.uniform(min_y, max_y)
    r_coord = (r_x, r_y)
    if r_coord not in added and meetsConstraints(r_coord):
        count += 1
        added.append(r_coord)

for i in added:
    print(i[0], i[1])     
#gmap1 = gmplot.GoogleMapPlotter(latitude_list[0], longitude_list[1], 13, api_key)
#gmap1.scatter(latitude_list, longitude_list, '# FF0000', size=40, marker = False)

#gmap1.draw('C:\\Users\\EGA\\Desktop\\map1.html')
    #TODO 2: check if in RAK
    
    #TODO 3: check if nearby a road

     #TODO 4: check if nearby other businesses
    
    #if coordinates pass all 3 tests, continue; else generate new point & repeat
#TODO 5: generate random opening hours