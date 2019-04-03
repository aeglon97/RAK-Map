import pandas as pd
import numpy as np, numpy.random
import csv
import random as rand

df = pd.read_csv('Businesses-Stakeholders.csv')

max_stakeholder_id = 50
max_business_id = 31030
num_row = 1

current_business_id = 1
while(current_business_id <= max_business_id):
    print("current_business_id: ", current_business_id)
    #assign multiple stakeholders to business 
    num_stakeholders = rand.randint(1, 5)
    
    #assign random stakeholders, no duplicates
    stakeholder_ids = np.random.choice(max_stakeholder_id, num_stakeholders, replace=False)
    
    #calculate random stakeholder rates
    stakeholder_rates = np.random.dirichlet(np.ones(num_stakeholders))
    string_stakeholder_rates = ', '.join(str("%.2f" % e) for e in np.nditer(stakeholder_rates))
    
    business_ids = []
    for i in range (len(stakeholder_ids)):
        business_ids.append(current_business_id)
        
    #put current_business_id in num_stakeholders amount of rows
    for i in range(len(stakeholder_ids)):
        #print(num_row, '\t', current_business_id, '\t', stakeholder_ids[i], '\t', stakeholder_rates[i])
        row = [current_business_id, stakeholder_ids[i], stakeholder_rates[i]]
        df.loc[len(df)] = row
    
        num_row += 1
        
    current_business_id += 1
    
    df.to_csv("Businesses-Stakeholders.csv", index=False)
print("done!")