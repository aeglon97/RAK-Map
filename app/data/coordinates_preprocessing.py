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
from numpy import array
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


def generateJSON(r_coord):
    params = 'latlng=' + str(r_coord[0]) + ',' + str(r_coord[1])
    query = geocode_url + params + '&key=' + api_key
    result_json = requests.get(query).json()
    return result_json

def isInRAK(result_json):
    #print('=====checking if in RAK=======')
    if (result_json and result_json['plus_code'] and 
        'compound_code' in result_json['plus_code']):
        address = result_json['plus_code']['compound_code']
        if ('Ras al Khaimah' not in address):
            #print("this is not in RAK.")
            return False
        #print("this is in RAK.")
        return True
    else:
        return False
    
def isOnRoad(result_json):
    print('=====checking if by road=====')
    if 'geometry' in result_json['results'][1]:
        geometry = result_json['results'][1]['geometry']
        pprint.pprint(geometry)
    
def meetsConstraints(r_coord):
    # print('-----------------------')
    result_json = generateJSON(r_coord)
    if isInRAK(result_json):
        return True
    return False
    #isOnRoad(result_json)
    
    #check if on road
    
df = pd.read_csv('rect_points_1.csv')

'''for i in range(200000):
    row = [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
    if row not in added:
        added.append(row)
        df.loc[i] = row

df.to_csv('rect_points_1.csv')'''
count = 50000
df_in_rak = pd.read_csv('rect_points_2.csv')

while count < len(df):
    row = (df.iloc[count, 1], df.iloc[count, 2])
    
    if meetsConstraints(row) :
        df_in_rak.loc[count] = row
    count += 1
        
df_in_rak.to_csv('rect_points_2.csv', index=False)