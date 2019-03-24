# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np, numpy.random
import csv
import random as rand

rak_businesses = pd.read_csv(r'rak_businesses.csv')

for i in range(len(rak_businesses)):
    #assign number of stakeholders per company
    num_stakeholders = rand.randint(1, 5)
    
    #assign random stakeholders, no duplicates
    stakeholder_ids = np.random.choice(50, num_stakeholders, replace=False)
    string_stakeholder_ids = ', '.join(str("%.0f" % e) for e in np.nditer(stakeholder_ids))
    
    #calculate random stakeholder rates
    stakeholder_rates = np.random.dirichlet(np.ones(num_stakeholders))
    string_stakeholder_rates = ', '.join(str("%.2f" % e) for e in np.nditer(stakeholder_rates))
    
    #put each stakeholder ID string in column
    rak_businesses.set_value(0, 'pk_stakeholder_ids', string_stakeholder_ids)
    
    #put each stakeholder rate string in column
    rak_businesses.set_value(0, 'Stakeholder Rates', string_stakeholder_rates)
    
    rak_businesses.to_csv('rak_businesses_modified.csv', index=False)

print("done!")