#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd                              # Loads the pandas library 

cars = pd.read_csv('cars.csv')                   # Reads and loads the CSV file into a dataframe named 'cars'


# In[3]:


# Problem 2 

# a. Display the first five rows with odd-numbered columns of cars 

cars.iloc[:5, 0::2]   # Uses integer-location indexing 
                      # :5     - Gets the first five rows 
                      # 0::2   - Gets every second column of the dataframe


# In[4]:


# b. Display the row that contains the 'Model' of 'Mazda RX4' 
cars[cars['Model'] == 'Mazda RX4']    # Locates the row where the model is equal to 'Mazda RX4' as index is used


# In[5]:


# c. Number of cylinders 'Camaro Z28' have
cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].item()   # Locates first the model Camaro Z28 
                                                        # .item() returns the number of cylinder from that model 


# In[6]:


# d. Number of cylinders and the gear type of car models Mazda RX4 Wag, Ford Pantera L, and Honda Civic have
cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']] 

# .isin()                    -  to locate the needed models 
# ['Model', 'cyl', 'gear']   -  to select the needed columns from the dataframe


# In[ ]:





# In[ ]:




