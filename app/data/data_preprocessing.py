import pandas as pd
import numpy as np, numpy.random
import csv
import random as rand

df_old = pd.read_csv(r'Businesses-Stakeholders.csv')

max_stakeholder_id = 50
max_business_id = 31030
num_row = 0

current_business_id = 0
while(current_business_id < 5):
    print("current_business_id: ", current_business_id)
    #assign multiple stakeholders to business 
    num_stakeholders = rand.randint(1, 5)
    
    #assign random stakeholders, no duplicates
    stakeholder_ids = np.random.choice(50, num_stakeholders, replace=False)
    
    #calculate random stakeholder rates
    stakeholder_rates = np.random.dirichlet(np.ones(num_stakeholders))
    string_stakeholder_rates = ', '.join(str("%.2f" % e) for e in np.nditer(stakeholder_rates))
    
    business_ids = []
    for i in range (len(stakeholder_ids)):
        business_ids.append(current_business_id)
        
    #put current_business_id in num_stakeholders amount of rows
    for i in range(len(stakeholder_ids)):
        new_df = pd.DataFrame({'business_id': business_ids,
                               'stakeholder_id': stakeholder_ids,
                               'stakeholder_rate': stakeholder_rates})
        #new_data = [current_business_id, stakeholder_ids[i], stakeholder_rates[i]]
        print(num_row, '\t', current_business_id, '\t', stakeholder_ids[i], '\t', stakeholder_rates[i])
        df_old.append(new_df, ignore_index=False)
        
        #df_old.concat = pd.concat(new_df, ignore_index=True)
        '''df_old.at[num_row, 'business_id'] = current_business_id
        df_old.at[num_row, 'stakeholder_id'] = stakeholder_ids[i]
        df_old.at[num_row, 'stakeholder_rate'] = stakeholder_rates[i]'''
    
        num_row += 1
        
        
    
    current_business_id += 1
    
    
    '''#assign number of stakeholders per company
    num_stakeholders = rand.randint(1, 5)
    
    #assign random stakeholders, no duplicates
    stakeholder_ids = np.random.choice(50, num_stakeholders, replace=False)
    string_stakeholder_ids = ', '.join(str("%.0f" % e) for e in np.nditer(stakeholder_ids))
    
    #calculate random stakeholder rates
    stakeholder_rates = np.random.dirichlet(np.ones(num_stakeholders))
    string_stakeholder_rates = ', '.join(str("%.2f" % e) for e in np.nditer(stakeholder_rates))
    
    #put each stakeholder ID string in column
    rak_businesses.set_value(i, 'stakeholder_ids', string_stakeholder_ids)
    #put each stakeholder rate string in column
    rak_businesses.set_value(i, 'Stakeholder Rates', string_stakeholder_rates)
    
    rak_businesses.to_csv('rak_businesses_modified.csv', index=False)'''
    
    
    

    #generate RAK latitude/longitude
    
    
print("done!")