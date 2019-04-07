# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 08:31:52 2019

@author: Angelo Acebedo
"""
import pandas as pd
import numpy as np
import requests, json

#df = pd.read_csv('Rak Businesses.csv')
import os
import googlemaps
from datetime import datetime


#dealing with environment variables
from os.path import join, dirname
from dotenv import load_dotenv

#dealing with environment variables 
path='./local.env'
load_dotenv(dotenv_path=path, verbose=True)
test_var = os.getenv('RAK_MAP_API_KEY')

url = 'https://maps.googleapis.com/maps/api/geocode/json?'

place = input()

res_ob = requests.get(url + 'address=' + place + '&key=' + test_var)
x = res_ob.json()

print(x)

'''
RAK BOUNDS [lat, lng]
    Northeast: 26.0696541, 56.19553699999999
    Southwest: 25.3543, 55.7306787
    
'''

#TODO 1: generate random coordinate in RAK boundary
    
    #TODO 2: check if not on road
    
    #TODO 3: check if on land

    #TODO 4: check if nearby other businesses
    
#TODO 5: extract opening hours of business
    
#TODO 6: find any other interesting parameters



